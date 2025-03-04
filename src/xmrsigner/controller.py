import logging
import traceback

from PIL import Image
from typing import List, Optional, Dict, Union
from time import sleep
from sys import exit

from xmrsigner.gui.renderer import Renderer
from xmrsigner.hardware.buttons import HardwareButtons
from xmrsigner.views.screensaver import ScreensaverScreen
from xmrsigner.views.view import Destination, NotYetImplementedView, UnhandledExceptionView

from xmrsigner.helpers.network import Network
from xmrsigner.helpers.wallet import MoneroWalletRPCManager
from xmrsigner.helpers.monero import TxDescription
from xmrsigner.models.seed import Seed
from xmrsigner.models.seed_storage import SeedJar
from xmrsigner.models.settings import Settings
from xmrsigner.models.singleton import Singleton
from xmrsigner.views.view import RemoveMicroSDWarningView

from monero.wallet import Wallet as MoneroWallet


MICROSECONDS_PER_MINUTE = 60 * 1000
IS_EMULATOR = False


logger = logging.getLogger(__name__)


class BackStack(List[Destination]):
    def __repr__(self):
        if len(self) == 0:
            return "[]"
        out = "[\n"
        for index, destination in reversed(list(enumerate(self))):
            out += f"    {index:2d}: {destination}\n"
        out += "]"
        return out


class Controller(Singleton):
    """
        The Controller is a globally available singleton that maintains XmrSigner state.

        It only makes sense to ever have a single Controller instance so it is
        implemented here as a singleton. One departure from the typical singleton pattern
        is the addition of a `configure_instance()` call to pass run-time settings into
        the Controller.

        Any code that needs to interact with the one and only Controller can just run:
        ```
        from xmrsigner.controller import Controller
        controller = Controller.get_instance()
        ```
        Note: In many/most cases you'll need to do the Controller import within a method
        rather than at the top in order avoid circular imports.
    """

    VERSION = "0.9.2"

    buttons: HardwareButtons = None
    jar: SeedJar = None
    settings: Settings = None
    renderer: Renderer = None

    block_height: Optional[int] = None  # helper var

    selected_seed: Optional[Seed] = None
    transaction: Optional[bytes] = None
    outputs: Optional[bytes] = None
    tx_description: TxDescription = None

    _wallet_rpc_manager: Optional[MoneroWalletRPCManager] = None
    wallets: Dict[Network, MoneroWallet] = {}
    wallet_seeds: Dict[Network, Seed] = {}

    unverified_address = None

    image_entropy_preview_frames: List[Image] = None
    image_entropy_final_image: Image = None

    # Destination placeholder for when we need to jump out to a side flow but intend to
    # return navigation to the main flow (e.g. TX flow, load something,
    # then resume TX flow).
    FLOW__SYNC = "sync"
    FLOW__TX = "tx"
    FLOW__VERIFY_MULTISIG_ADDR = "multisig_addr"
    FLOW__VERIFY_SINGLESIG_ADDR = "singlesig_addr"
    FLOW__ADDRESS_EXPLORER = "address_explorer"
    FLOW__SIGN_MESSAGE = "sign_message"
    resume_main_flow: str = None

    back_stack: BackStack = None
    screensaver: ScreensaverScreen = None


    @classmethod
    def get_instance(cls):
        # This is the only way to access the one and only instance
        if cls._instance:
            return cls._instance
        else:
            # Instantiate the one and only Controller instance
            return cls.configure_instance()

    @classmethod
    def shutdown(cls) -> None:
        print('shutdown...')
        if cls._instance._wallet_rpc_manager:
            cls._instance._wallet_rpc_manager.cleanup()

    @classmethod
    def configure_instance(cls, disable_hardware=False):
        """
            - `disable_hardware` is only meant to be used by the test suite so that it
            can keep re-initializing a Controller in however many tests it needs to. But
            this is only possible if the hardware isn't already being reserved. Without
            this you get:

            RuntimeError: Conflicting edge detection already enabled for this GPIO channel

            each time you try to re-initialize a Controller.
        """
        from xmrsigner.hardware.microsd import MicroSD

        # Must be called before the first get_instance() call
        if cls._instance:
            raise Exception("Instance already configured")

        # Instantiate the one and only Controller instance
        controller = cls.__new__(cls)
        cls._instance = controller

        # Input Buttons
        if disable_hardware:
            controller.buttons = None
        else:
            controller.buttons = HardwareButtons.get_instance()

        # models
        controller.jar = SeedJar()
        controller.settings = Settings.get_instance()
        controller.microsd = MicroSD.get_instance()
        controller.microsd.start_detection()

        # Store one working incomming data in memory
        controller.outputs = None
        controller.transaction = None
        controller.selected_seed = None
        controller.tx_description = None

        # Configure the Renderer
        Renderer.configure_instance()

        controller.back_stack = BackStack()

        # Other behavior constants
        controller.screensaver_activation_ms = 2 * MICROSECONDS_PER_MINUTE
    
        return cls._instance


    @property
    def camera(self):
        from .hardware.camera import Camera
        return Camera.get_instance()

    @property
    def seeds(self) -> Optional[List[Seed]]:
        return self.jar.seeds

    def has_seed(self, seed: Seed) -> bool:
        return seed in self.jar.seeds

    def get_seed_num(self, seed: Seed) -> Optional[int]:
        idx = self.jar.seeds.index(seed)
        if idx >= 0:
            return idx
        return None

    def get_seed(self, seed_num: int) -> Seed:
        if seed_num < len(self.jar.seeds):
            return self.jar.seeds[seed_num]
        else:
            raise Exception(f"There is no seed_num {seed_num}; only {len(self.jar.seeds)} in memory.")

    def replace_seed(self, seed_num: int, seed: Seed) -> None:
        if seed_num < len(self.jar.seeds):
            self.jar.seeds[seed_num] = seed
        else:
            raise Exception(f"There is no seed_num {seed_num}; only {len(self.jar.seeds)} in memory.")

    def discard_seed(self, seed_num: int):
        if seed_num < len(self.jar.seeds):
            del self.jar.seeds[seed_num]
        else:
            raise Exception(f"There is no seed_num {seed_num}; only {len(self.jar.seeds)} in memory.")

    @property
    def wallet_rpc_manager(self):
        if not self._wallet_rpc_manager:
            self._wallet_rpc_manager = MoneroWalletRPCManager.get_instance()
        return self._wallet_rpc_manager

    def get_wallet_seed(self, network: Union[str, Network]) -> Optional[Seed]:
        network = Network.ensure(network)
        if network in self.wallet_seeds:
            return self.wallet_seeds[network]
        return None

    def set_wallet_seed(self, network: Union[str, Network], seed: Seed) -> None:
        network = Network.ensure(network)
        self.wallet_seeds[network] = seed

    def clear_wallet_seed(self, network: Union[str, Network]) -> None:
        network = Network.ensure(network)
        if network in self.wallet_seeds:
            del self.wallet_seeds[network]

    def get_wallet(self, network: Union[str, Network]) -> Optional[MoneroWallet]:
        network = Network.ensure(network)
        if network in self.wallets:
            return self.wallets[network]
        return None

    def set_wallet(self, network: Union[str, Network], wallet: MoneroWallet) -> None:
        network = Network.ensure(network)
        self.wallets[network] = wallet

    def clear_wallet(self, network: Union[str, Network]) -> None:
        network = Network.ensure(network)
        if network in self.wallets:
            del self.wallets[network]

    def pop_prev_from_back_stack(self):
        if len(self.back_stack) > 0:
            # Pop the top View (which is the current View_cls)
            self.back_stack.pop()

            if len(self.back_stack) > 0:
                # One more pop back gives us the actual "back" View_cls
                return self.back_stack.pop()
        return Destination(None)

    def clear_back_stack(self):
        self.back_stack = BackStack()

    def start(self) -> None:
        """
            The main loop of the application.
        """
        from xmrsigner.views.view import MainMenuView, BackStackView
        from xmrsigner.views.screensaver import OpeningSplashScreen

        OpeningSplashScreen().start()

        """ Class references can be stored as variables in python!

            This loop receives a View class to execute and stores it in the `View_cls`
            var along with any input arguments in the `init_args` dict.

            The `View_cls` is instantiated with `init_args` passed in and then run(). It
            returns either a new View class to execute next or None.

            Example:
                class MyView(View)
                    def run(self, some_arg, other_arg):
                        print(other_arg)

                class OtherView(View):
                    def run(self):
                        return (MyView, {"some_arg": 1, "other_arg": "hello"})

            When `OtherView` is instantiated and run, we capture its return values:

                (View_cls, init_args) = OtherView().run()

            And then we can instantiate and run that View class:

                View_cls(**init_args).run()
        """
        try:
            next_destination = Destination(MainMenuView) if not IS_EMULATOR else Destination(RemoveMicroSDWarningView, view_args={'next_view': MainMenuView}, clear_history=True)
            while True:
                # Destination(None) is a special case; render the Home screen
                if next_destination.View_cls is None:
                    next_destination = Destination(MainMenuView)

                if next_destination.View_cls == MainMenuView:
                    # Home always wipes the back_stack
                    self.clear_back_stack()
                    
                    # Home always wipes the back_stack/state of temp vars
                    self.resume_main_flow = None
                    self.unverified_address = None
                    self.address_explorer_data = None
                    self.selected_seed = None
                    self.outputs = None
                    self.transaction = None
                    self.tx_description = None
                
                print(f'back_stack: {self.back_stack}')

                try:
                    print(f'Executing {next_destination}')
                    next_destination = next_destination.run()
                except Exception as e:
                    # Display user-friendly error screen w/debugging info
                    next_destination = self.handle_exception(e)

                if not next_destination:
                    # Should only happen during dev when you hit an unimplemented option
                    next_destination = Destination(NotYetImplementedView)

                if next_destination.skip_current_view:
                    # Remove the current View from history; it's forwarding us straight
                    # to the next View so it should be as if this View never happened.
                    current_view = self.back_stack.pop()
                    print(f'Skipping current view: {current_view}')

                # Hang on to this reference...
                clear_history = next_destination.clear_history

                if next_destination.View_cls == BackStackView:
                    # "Back" arrow was clicked; load the previous view
                    next_destination = self.pop_prev_from_back_stack()

                # ...now apply it, if needed
                if clear_history:
                    self.clear_back_stack()

                # The next_destination up always goes on the back_stack, even if it's the
                #   one we just popped.
                # Do not push a "new" destination if it is the same as the current one on
                # the top of the stack.
                if len(self.back_stack) == 0 or self.back_stack[-1] != next_destination:
                    print(f'Appending next destination: {next_destination}')
                    self.back_stack.append(next_destination)
                else:
                    print(f'NOT appending {next_destination}')
                
                print('-' * 30)

        finally:
            if self.is_screensaver_running:
                self.screensaver.stop()

            # Clear the screen when exiting
            print('Clearing screen, exiting')
            Renderer.get_instance().display_blank_screen()

    @property
    def is_screensaver_running(self):
        return self.screensaver is not None and self.screensaver.is_running


    def start_screensaver(self):
        print("Controller: Starting screensaver")
        if not self.screensaver:
            self.screensaver = ScreensaverScreen(HardwareButtons.get_instance())

        # Start the screensaver, but it will block until it can acquire the Renderer.lock.
        self.screensaver.start()
        print("Controller: Screensaver started")

    def handle_exception(self, e) -> Destination:
        """
            Displays a user-friendly error screen and includes debugging info to help
            devs diagnose what went wrong.

            Shows:
                * Exception type
                * python file, line num, method name
                * Exception message
        """
        logger.exception(e)

        # The final exception output line is:
        # "foo.bar.ExceptionType: The exception message"
        # So we extract the Exception type and trim off any "foo.bar." namespacing:
        last_line = traceback.format_exc().splitlines()[-1]
        exception_type = last_line.split(":")[0].split(".")[-1]
        exception_msg = last_line.split(":")[1]

        # Scan for the last debugging line that includes a line number reference
        line_info = None
        for i in range(len(traceback.format_exc().splitlines()) - 1, 0, -1):
            traceback_line = traceback.format_exc().splitlines()[i]
            if ", line " in traceback_line:
                line_info = traceback_line.split("/")[-1].replace("\"", "").replace("line ", "")
                break
        
        error = [
            exception_type,
            line_info,
            exception_msg,
        ]
        return Destination(UnhandledExceptionView, view_args={"error": error}, clear_history=True)
