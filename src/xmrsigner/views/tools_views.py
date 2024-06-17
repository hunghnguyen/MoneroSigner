from dataclasses import dataclass
from hashlib import sha256
from os import popen
from time import time, sleep

from PIL import Image
from PIL.ImageOps import autocontrast

from monero.seed import Seed as MoneroSeed

from xmrsigner.gui.components import FontAwesomeIconConstants, GUIConstants, IconConstants
from xmrsigner.gui.screens import (
    RET_CODE__BACK_BUTTON,
    ButtonListScreen,
)
from xmrsigner.gui.screens.tools_screens import (
    ToolsCalcFinalWordFinalizePromptScreen,
    ToolsCalcFinalWordScreen,
    ToolsCoinFlipEntryScreen,
    ToolsDiceEntropyEntryScreen,
    ToolsImageEntropyFinalImageScreen,
    ToolsImageEntropyLivePreviewScreen,
    ToolsCalcFinalWordDoneScreen,
    ToolsAddressExplorerAddressTypeScreen
)
from xmrsigner.helpers import mnemonic_generation
from xmrsigner.helpers import polyseed_mnemonic_generation
from xmrsigner.models.seed import Seed
from xmrsigner.models.polyseed import PolyseedSeed
from xmrsigner.models.settings_definition import SettingsConstants
from xmrsigner.models.encode_qr import EncodeQR
from xmrsigner.models.qr_type import QRType
from xmrsigner.views.seed_views import (
    SeedDiscardView,
    SeedFinalizeView,
    SeedMnemonicEntryView,
    SeedWordsWarningView,
    SeedOptionsView
)
from xmrsigner.views.view import (
    View,
    Destination,
    BackStackView
)


class ToolsMenuView(View):

    def __init__(self, secure_only: bool = False):
        super().__init__()
        self.secure_only = secure_only

    def run(self):
        IMAGE = (" New seed", FontAwesomeIconConstants.CAMERA)
        DICE = ("New seed", FontAwesomeIconConstants.DICE)
        KEYBOARD = ("Pick own words", FontAwesomeIconConstants.KEYBOARD)  # TODO: expire 2024-06-21, I think there should be a warning that this way most probale will lead to low entropy, should only be used if user is really knowing what he is doing... Maybe an alternative would be to use it as input entropy with pseudo entropy to generate a new "now magically random" (of course not, but at least with less probability of user picking the most prefered words out of the list and shootig himself in the foot.
        EXPLORER = "Address Explorer"
        ADDRESS = "Verify address"
        if self.secure_only or self.settings.get_value(SettingsConstants.SEETING__LOW_SECURITY) == SettingsConstants.OPTION__DISABLED:
            button_data = [IMAGE, DICE, EXPLORER, ADDRESS]
        else:
            button_data = [IMAGE, DICE, KEYBOARD, EXPLORER, ADDRESS]
        selected_menu_num = self.run_screen(
            ButtonListScreen,
            title="Tools",
            is_button_text_centered=False,
            button_data=button_data
        )

        if selected_menu_num == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)
        if button_data[selected_menu_num] == IMAGE:
            return Destination(ToolsImageEntropyLivePreviewView)
        if button_data[selected_menu_num] == DICE:
            return Destination(ToolsDiceSeedTypeView)
        if button_data[selected_menu_num] == KEYBOARD:
            return Destination(ToolsCalcFinalWordWarningView)
        if button_data[selected_menu_num] == self.EXPLORER:
            return Destination(ToolsAddressExplorerSelectSourceView)
        if button_data[selected_menu_num] == self.ADDRESS:
            from xmrsigner.views.scan_views import ScanAddressView
            return Destination(ScanAddressView)


"""****************************************************************************
    Image entropy Views
****************************************************************************"""
class ToolsImageEntropyLivePreviewView(View):
    def run(self):
        self.controller.image_entropy_preview_frames = None
        ret = ToolsImageEntropyLivePreviewScreen().display()

        if ret == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)
        
        self.controller.image_entropy_preview_frames = ret
        return Destination(ToolsImageEntropyFinalImageView)



class ToolsImageEntropyFinalImageView(View):
    def run(self):
        if not self.controller.image_entropy_final_image:
            from xmrsigner.hardware.camera import Camera
            # Take the final full-res image
            camera = Camera.get_instance()
            camera.start_single_frame_mode(resolution=(720, 480))
            sleep(0.25)
            self.controller.image_entropy_final_image = camera.capture_frame()
            camera.stop_single_frame_mode()

        # Prep a copy of the image for display. The actual image data is 720x480
        # Present just a center crop and resize it to fit the screen and to keep some of
        #   the data hidden.
        display_version = autocontrast(
            self.controller.image_entropy_final_image,
            cutoff=2
        ).crop(
            (120, 0, 600, 480)
        ).resize(
            (self.canvas_width, self.canvas_height), Image.BICUBIC
        )
        
        ret = ToolsImageEntropyFinalImageScreen(
            final_image=display_version
        ).display()

        if ret == RET_CODE__BACK_BUTTON:
            # Go back to live preview and reshoot
            self.controller.image_entropy_final_image = None
            return Destination(BackStackView)
        
        # return Destination(ToolsImageEntropyMnemonicLengthView)
        return Destination(ToolsImageSeedTypeView)


class ToolsImageSeedTypeView(View):
    def run(self):
        MONERO_SEED = 'Monero Seed'
        POLYSEED = 'Polyseed'
        button_data = [MONERO_SEED, POLYSEED]

        selected_menu_num = ButtonListScreen(
            title="Seed type?",
            button_data=button_data,
        ).display()

        if selected_menu_num == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)
        
        if button_data[selected_menu_num] == MONERO_SEED:
            return Destination(ToolsImageEntropyMnemonicLengthView)
        else:
            return Destination(ToolsImagePolyseedView)


class ToolsImageEntropyMnemonicLengthView(View):
    def run(self):
        if self.settings.get_value(SettingsConstants.SEETING__LOW_SECURITY) == SettingsConstants.OPTION__ENABLED:
            THIRTEEN_WORDS = "13 words"
            TWENTYFOUR_WORDS = "25 words"
            button_data = [THIRTEEN_WORDS, TWENTYFOUR_WORDS]

            selected_menu_num = ButtonListScreen(
                title="Mnemonic Length?",
                button_data=button_data,
            ).display()

            if selected_menu_num == RET_CODE__BACK_BUTTON:
                return Destination(BackStackView)
            
            if button_data[selected_menu_num] == THIRTEEN_WORDS:
                mnemonic_length = 13
            else:
                mnemonic_length = 25
        else:
            mnemonic_length = 25

        preview_images = self.controller.image_entropy_preview_frames
        seed_entropy_image = self.controller.image_entropy_final_image

        # TODO: expire 2024-06-04 should be merged with ToolsImagePolyseedView, same code and be outsid of views...
        # Build in some hardware-level uniqueness via CPU unique Serial num
        try:
            stream = popen("cat /proc/cpuinfo | grep Serial")
            output = stream.read()
            serial_num = output.split(":")[-1].strip().encode('utf-8')
            serial_hash = sha256(serial_num)
            hash_bytes = serial_hash.digest()
        except Exception as e:
            print(repr(e))
            hash_bytes = b'0'

        # Build in modest entropy via millis since power on
        millis_hash = sha256(hash_bytes + str(time()).encode('utf-8'))
        hash_bytes = millis_hash.digest()

        # Build in better entropy by chaining the preview frames
        for frame in preview_images:
            img_hash = sha256(hash_bytes + frame.tobytes())
            hash_bytes = img_hash.digest()

        # Finally build in our headline entropy via the new full-res image
        final_hash = sha256(hash_bytes + seed_entropy_image.tobytes()).digest()

        if mnemonic_length == 13:
            # 12-word mnemonic only uses the first 128 bits / 16 bytes of entropy
            final_hash = final_hash[:16]

        # Generate the mnemonic
        mnemonic = mnemonic_generation.generate_mnemonic_from_bytes(final_hash)

        # TODO: expire 2024-07-31, don't know python memory managment, but `del seed_entropy_image` etc seems for me the better way, well, need to investigate, when not mistaken, python uses GC, is there a way to clean up inmedately?
        # Image should never get saved nor stick around in memory
        seed_entropy_image = None
        preview_images = None
        final_hash = None
        hash_bytes = None
        self.controller.image_entropy_preview_frames = None
        self.controller.image_entropy_final_image = None

        # Add the mnemonic as an in-memory Seed
        seed = Seed(mnemonic, wordlist_language_code=self.settings.get_value(SettingsConstants.SETTING__WORDLIST_LANGUAGE))  # TODO: expire 2024-07-01, see #todo in xmrsigner.helpers.mnemonic_generation, and fix language together...
        self.controller.storage.set_pending_seed(seed)
        
        # Cannot return BACK to this View
        return Destination(SeedWordsWarningView, view_args={"seed_num": None}, clear_history=True)


class ToolsImagePolyseedView(View):
    def run(self):
        preview_images = self.controller.image_entropy_preview_frames
        seed_entropy_image = self.controller.image_entropy_final_image

        # TODO: expire 2024-06-04 should be merged with ToolsImageEntropyMnemonicLengthView, same code and be outsid of views...
        # Build in some hardware-level uniqueness via CPU unique Serial num
        try:
            stream = popen("cat /proc/cpuinfo | grep Serial")
            output = stream.read()
            serial_num = output.split(":")[-1].strip().encode('utf-8')
            serial_hash = sha256(serial_num)
            hash_bytes = serial_hash.digest()
        except Exception as e:
            print(repr(e))
            hash_bytes = b'0'

        # Build in modest entropy via millis since power on
        millis_hash = sha256(hash_bytes + str(time()).encode('utf-8'))
        hash_bytes = millis_hash.digest()

        # Build in better entropy by chaining the preview frames
        for frame in preview_images:
            img_hash = sha256(hash_bytes + frame.tobytes())
            hash_bytes = img_hash.digest()

        # Finally build in our headline entropy via the new full-res image
        final_hash = sha256(hash_bytes + seed_entropy_image.tobytes()).digest()

        mnemonic = polyseed_mnemonic_generation.generate_mnemonic_from_bytes(final_hash)

        # TODO: expire 2024-07-31, don't know python memory managment, but `del seed_entropy_image` etc seems for me the better way, well, need to investigate, when not mistaken, python uses GC, is there a way to clean up inmedately?
        # Image should never get saved nor stick around in memory
        seed_entropy_image = None
        preview_images = None
        final_hash = None
        hash_bytes = None
        self.controller.image_entropy_preview_frames = None
        self.controller.image_entropy_final_image = None

        # Add the mnemonic as an in-memory Seed
        seed = PolyseedSeed(mnemonic, wordlist_language_code=self.settings.get_value(SettingsConstants.SETTING__WORDLIST_LANGUAGE))  # TODO: expire 2024-07-01, see #todo in xmrsigner.helpers.mnemonic_generation, and fix language together...
        self.controller.storage.set_pending_seed(seed)
        
        # Cannot return BACK to this View
        return Destination(SeedWordsWarningView, view_args={"seed_num": None}, clear_history=True)



"""****************************************************************************
    Dice rolls Views
****************************************************************************"""
class ToolsDiceSeedTypeView(View):
    def run(self):
        MONERO_SEED = 'Monero Seed'
        POLYSEED = 'Polyseed'
        button_data = [MONERO_SEED, POLYSEED]

        selected_menu_num = ButtonListScreen(
            title="Seed type?",
            button_data=button_data,
        ).display()

        if selected_menu_num == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)
        
        if button_data[selected_menu_num] == MONERO_SEED:
            return Destination(ToolsDiceEntropyMnemonicLengthView)
        else:
            return Destination(ToolsDicePolyseedView)


class ToolsDiceEntropyMnemonicLengthView(View): # TODO: expire 2024-06-30, offer only 25 words if not low security is set in settings
    def run(self):
        if self.settings.get_value(SettingsConstants.SEETING__LOW_SECURITY) != SettingsConstants.OPTION__ENABLED:
            return Destination(ToolsDiceEntropyEntryView, view_args=dict(total_rolls=99))

        THIRTEEN = "13 words (50 rolls)"
        TWENTY_FIVE = "25 words (99 rolls)"
        
        button_data = [THIRTEEN, TWENTY_FIVE]
        selected_menu_num = ButtonListScreen(
            title="Mnemonic Length",
            is_bottom_list=True,
            is_button_text_centered=True,
            button_data=button_data,
        ).display()

        if selected_menu_num == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)

        elif button_data[selected_menu_num] == THIRTEEN:
            return Destination(ToolsDiceEntropyEntryView, view_args=dict(total_rolls=50))

        elif button_data[selected_menu_num] == TWENTY_FIVE:
            return Destination(ToolsDiceEntropyEntryView, view_args=dict(total_rolls=99))


class ToolsDiceEntropyEntryView(View):
    def __init__(self, total_rolls: int):
        super().__init__()
        self.total_rolls = total_rolls
    

    def run(self):
        ret = ToolsDiceEntropyEntryScreen(
            return_after_n_chars=self.total_rolls,
        ).display()

        if ret == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)
        dice_seed_phrase = mnemonic_generation.generate_mnemonic_from_dice(ret)
        # Add the mnemonic as an in-memory Seed
        seed = Seed(dice_seed_phrase, wordlist_language_code=self.settings.get_value(SettingsConstants.SETTING__WORDLIST_LANGUAGE))
        self.controller.storage.set_pending_seed(seed)

        # Cannot return BACK to this View
        return Destination(SeedWordsWarningView, view_args={"seed_num": None}, clear_history=True)


class ToolsDicePolyseedView(View):
    def __init__(self, total_rolls: int = 99):
        super().__init__()
        self.total_rolls: int = total_rolls

    def run(self):
        ret = ToolsDiceEntropyEntryScreen(
            return_after_n_chars=self.total_rolls,
        ).display()

        if ret == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)
        
        print(f"Dice rolls: {ret}")
        dice_seed_phrase = polyseed_mnemonic_generation.generate_mnemonic_from_dice(ret)
        print(f"""Mnemonic: "{dice_seed_phrase}" """)

        # Add the mnemonic as an in-memory Seed
        seed = PolyseedSeed(dice_seed_phrase, wordlist_language_code=self.settings.get_value(SettingsConstants.SETTING__WORDLIST_LANGUAGE))
        self.controller.storage.set_pending_seed(seed)

        # Cannot return BACK to this View
        return Destination(SeedWordsWarningView, view_args={"seed_num": None}, clear_history=True)



"""****************************************************************************
    Calc final word Views
****************************************************************************"""
class ToolsCalcFinalWordWarningView(View):
    def __init__(self):
        super().__init__()

    def run(self):
        destination = Destination(
            ToolsCalcFinalWordNumWordsView,
            skip_current_view=True,  # Prevent going BACK to WarningViews
        )
        if self.settings.get_value(SettingsConstants.SETTING__DIRE_WARNINGS) == SettingsConstants.OPTION__DISABLED:
            return destination

        MORE_SECURE = "Choose secure way"
        AWARE = "I know what I'm doing"
        button_data = [MORE_SECURE, AWARE]

        selected_menu_num = self.run_screen(
            DireWarningScreen,
            title="Low Entropy Warning",
            show_back_button=False,
            status_headline="Are you sure?",
            text="""The most insecure way, except chosen really random.""",
            button_data=button_data
        )

        if button_data[selected_menu_num] == AWARE:
            # User clicked "I Understand"
            return destination

        elif button_data[selected_menu_num] == MORE_SECURE:
            # return Destination(BackStackView)
            return Destination(ToolsMenuView, view_args={'secure_only': True}, clear_history=True)


class ToolsCalcFinalWordNumWordsView(View):
    def run(self):
        if self.settings.get_value(SettingsConstants.SEETING__LOW_SECURITY) == SettingsConstants.OPTION__ENABLED:
            THIRTEEN = "13 words"
            TWENTY_FIVE = "25 words"
            
            button_data = [THIRTEEN, TWENTY_FIVE]
            selected_menu_num = ButtonListScreen(
                title="Mnemonic Length",
                is_bottom_list=True,
                is_button_text_centered=True,
                button_data=button_data,
            ).display()

            if selected_menu_num == RET_CODE__BACK_BUTTON:
                return Destination(BackStackView)

            elif button_data[selected_menu_num] == THIRTEEN:
                self.controller.storage.init_pending_mnemonic(13)
                return Destination(SeedMnemonicEntryView, view_args=dict(is_calc_final_word=True))

            elif button_data[selected_menu_num] == TWENTY_FIVE:
                self.controller.storage.init_pending_mnemonic(25)
                return Destination(SeedMnemonicEntryView, view_args=dict(is_calc_final_word=True))
        self.controller.storage.init_pending_mnemonic(25)
        return Destination(SeedMnemonicEntryView, view_args=dict(is_calc_final_word=True))


class ToolsCalcFinalWordShowFinalWordView(View):  # TODO: 2024-06-04, rename, because it is missleading, the only thing what will be calculated is the checksum word
    def __init__(self, coin_flips: str = None):
        super().__init__()
        self.coin_flips = coin_flips

    def run(self):
        mnemonic = self.controller.storage.pending_mnemonic
        mnemonic_length = len(mnemonic)
        wordlist_language_code = self.settings.get_value(SettingsConstants.SETTING__WORDLIST_LANGUAGE)
        wordlist = Seed.get_wordlist(wordlist_language_code)

        final_mnemonic = MoneroSeed(MoneroSeed(' '.join(self.controller.storage.pending_mnemonic[:(mnemonic_length -1)])).hex).phrase.split(' ')  # TODO: 2024-06-04 hot fix, make it right, seems actually right to add checksum
        self.controller.storage.update_pending_mnemonic(final_mnemonic[-1], mnemonic_length - 1)
        return Destination(ToolsCalcFinalWordDoneView)


class ToolsCalcFinalWordDoneView(View):
    def run(self):
        mnemonic = self.controller.storage.pending_mnemonic
        mnemonic_word_length = len(mnemonic)
        final_word = mnemonic[-1]

        LOAD = "Load seed"
        DISCARD = ("Discard", None, None, "red")
        button_data = [LOAD, DISCARD]

        selected_menu_num = ToolsCalcFinalWordDoneScreen(
            final_word=final_word,
            mnemonic_word_length=mnemonic_word_length,
            fingerprint=self.controller.storage.get_pending_mnemonic_fingerprint(self.settings.get_value(SettingsConstants.SETTING__NETWORK)),
            button_data=button_data,
        ).display()

        if selected_menu_num == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)
        
        self.controller.storage.convert_pending_mnemonic_to_pending_seed()

        if button_data[selected_menu_num] == LOAD:
            return Destination(SeedFinalizeView)
        
        elif button_data[selected_menu_num] == DISCARD:
            return Destination(SeedDiscardView)


"""****************************************************************************
    Address Explorer Views
****************************************************************************"""
class ToolsAddressExplorerSelectSourceView(View):

    SCAN_SEED = ("Scan a seed", IconConstants.QRCODE)
    SCAN_WALLET = ("Scan wallet", IconConstants.QRCODE)
    TYPE_13WORD = ("Enter 13-word seed", FontAwesomeIconConstants.KEYBOARD)
    TYPE_25WORD = ("Enter 25-word seed", FontAwesomeIconConstants.KEYBOARD)
    TYPE_POLYSEED = ("Enter Polyseed", FontAwesomeIconConstants.KEYBOARD)

    def run(self):
        seeds = self.controller.storage.seeds
        button_data = []
        for seed in seeds:
            button_str = seed.get_fingerprint(self.settings.get_value(SettingsConstants.SETTING__NETWORK))
            button_data.append((button_str, IconConstants.FINGERPRINT))
        button_data = button_data + [self.SCAN_SEED, self.SCAN_WALLET, self.TYPE_13WORD, self.TYPE_25WORD, self.TYPE_POLYSEED]
        
        selected_menu_num = self.run_screen(
            ButtonListScreen,
            title="Address Explorer",
            button_data=button_data,
            is_button_text_centered=False,
            is_bottom_list=True,
        )

        if selected_menu_num == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)

        # Most of the options require us to go through a side flow(s) before we can
        # continue to the address explorer. Set the Controller-level flow so that it
        # knows to re-route us once the side flow is complete.        
        self.controller.resume_main_flow = Controller.FLOW__ADDRESS_EXPLORER

        if len(seeds) > 0 and selected_menu_num < len(seeds):
            # User selected one of the n seeds
            return Destination(
                SeedExportXpubScriptTypeView,
                view_args=dict(
                    seed_num=selected_menu_num,
                    sig_type=SettingsConstants.SINGLE_SIG,
                )
            )
        if button_data[selected_menu_num] == self.SCAN_SEED:
            from xmrsigner.views.scan_views import ScanSeedQRView
            return Destination(ScanSeedQRView)
        if button_data[selected_menu_num] == self.SCAN_WALLET:
            from xmrsigner.views.scan_views import ScanWalletDescriptorView
            return Destination(ScanWalletDescriptorView)
        if button_data[selected_menu_num] in [self.TYPE_13WORD, self.TYPE_25WORD]:
            from xmrsigner.views.seed_views import SeedMnemonicEntryView
            if button_data[selected_menu_num] == self.TYPE_13WORD:
                self.controller.storage.init_pending_mnemonic(num_words=13)
            else:
                self.controller.storage.init_pending_mnemonic(num_words=25)
            return Destination(SeedMnemonicEntryView)
        if button_data[selected_menu_num] == self.TYPE_POLYSEED:
            from xmrsigner.views.seed_views import PolyseedMnemonicEntryView
            return Destination(PolyseedMnemonicEntryView)


class ToolsAddressExplorerAddressTypeView(View):  # TODO: 2024-06-17, holy clusterfuck, added with rebase from main to 0.7.0 of seedsigner, lot of work to do

    RECEIVE = "Receive Addresses"
    CHANGE = "Change Addresses"

    def __init__(self, seed_num: int = None, script_type: str = None, custom_derivation: str = None):
        """
        If the explorer source is a seed, `seed_num` and `script_type` must be
        specified. `custom_derivation` can be specified as needed.

        If the source is a multisig or single sig wallet descriptor, `seed_num`,
        `script_type`, and `custom_derivation` should be `None`.
        """
        super().__init__()
        self.seed_num = seed_num
        network = self.settings.get_value(SettingsConstants.SETTING__NETWORK)

        # Store everything in the Controller's `address_explorer_data` so we don't have
        # to keep passing vals around from View to View and recalculating.
        data = {
            'seed_num': seed_num,
            'network': self.settings.get_value(SettingsConstants.SETTING__NETWORK)
        }
        if self.seed_num is not None:
            self.seed = self.controller.storage.seeds[seed_num]
            data["seed_num"] = self.seed
        else:
            data["wallet_descriptor"] = self.controller.multisig_wallet_descriptor
        self.controller.address_explorer_data = data

    def run(self):
        data = self.controller.address_explorer_data

        wallet_descriptor_display_name = None
        if "wallet_descriptor" in data:
            wallet_descriptor_display_name = data["wallet_descriptor"].brief_policy.replace(" (sorted)", "")

        button_data = [self.RECEIVE, self.CHANGE]

        selected_menu_num = self.run_screen(
            ToolsAddressExplorerAddressTypeScreen,
            button_data=button_data,
            fingerprint=self.seed.get_fingerprint() if self.seed_num is not None else None,
            wallet_descriptor_display_name=wallet_descriptor_display_name
        )

        if selected_menu_num == RET_CODE__BACK_BUTTON:
            # If we entered this flow via an already-loaded seed's SeedOptionsView, we
            # need to clear the `resume_main_flow` so that we don't get stuck in a 
            # SeedOptionsView redirect loop.
            # TODO: Refactor to a cleaner `BackStack.get_previous_View_cls()`
            if len(self.controller.back_stack) > 1 and self.controller.back_stack[-2].View_cls == SeedOptionsView:
                # The BackStack has the current View on the top with the real "back" in second position.
                self.controller.resume_main_flow = None
                self.controller.address_explorer_data = None
            return Destination(BackStackView)
        
        if button_data[selected_menu_num] in [self.RECEIVE, self.CHANGE]:
            return Destination(ToolsAddressExplorerAddressListView, view_args=dict(is_change=button_data[selected_menu_num] == self.CHANGE))


class ToolsAddressExplorerAddressListView(View):
    def __init__(self, is_change: bool = False, start_index: int = 0, selected_button_index: int = 0, initial_scroll: int = 0):
        super().__init__()
        self.is_change = is_change
        self.start_index = start_index
        self.selected_button_index = selected_button_index
        self.initial_scroll = initial_scroll


    def run(self):
        self.loading_screen = None

        addresses = []
        button_data = []
        data = self.controller.address_explorer_data
        addrs_per_screen = 10

        addr_storage_key = "receive_addrs"
        if self.is_change:
            addr_storage_key = "change_addrs"

        if addr_storage_key in data and len(data[addr_storage_key]) >= self.start_index + addrs_per_screen:
            # We already calculated this range of addresses; just retrieve them
            addresses = data[addr_storage_key][self.start_index:self.start_index + addrs_per_screen]

        else:
            try:
                from xmrsigner.gui.screens.screen import LoadingScreenThread
                self.loading_screen = LoadingScreenThread(text="Calculating addrs...")
                self.loading_screen.start()

                if addr_storage_key not in data:
                    data[addr_storage_key] = []

                if "xpub" in data:
                    # Single sig explore from seed
                    if "script_type" in data and data["script_type"] != SettingsConstants.CUSTOM_DERIVATION:
                        # Standard derivation path
                        for i in range(self.start_index, self.start_index + addrs_per_screen):
                            address = embit_utils.get_single_sig_address(xpub=data["xpub"], script_type=data["script_type"], index=i, is_change=self.is_change, embit_network=data["embit_network"])
                            addresses.append(address)
                            data[addr_storage_key].append(address)
                    else:
                        # TODO: Custom derivation path
                        raise Exception("Custom Derivation address explorer not yet implemented")
                
                elif "wallet_descriptor" in data:
                    descriptor: Descriptor = data["wallet_descriptor"]
                    if descriptor.is_basic_multisig:
                        for i in range(self.start_index, self.start_index + addrs_per_screen):
                            address = embit_utils.get_multisig_address(descriptor=descriptor, index=i, is_change=self.is_change, embit_network=data["embit_network"])
                            addresses.append(address)
                            data[addr_storage_key].append(address)

                    else:
                        raise Exception("Single sig descriptors not yet supported")
            finally:
                # Everything is set. Stop the loading screen
                self.loading_screen.stop()

        for i, address in enumerate(addresses):
            cur_index = i + self.start_index

            # Adjust the trailing addr display length based on available room
            # (the index number will push it out on each order of magnitude)
            if cur_index < 10:
                end_digits = -6
            elif cur_index < 100:
                end_digits = -5
            else:
                end_digits = -4
            button_data.append(f"{cur_index}:{address[:8]}...{address[end_digits:]}")

        button_data.append(("Next {}".format(addrs_per_screen), None, None, None, IconConstants.CHEVRON_RIGHT))

        selected_menu_num = self.run_screen(
            ButtonListScreen,
            title="{} Addrs".format("Receive" if not self.is_change else "Change"),
            button_data=button_data,
            button_font_name=GUIConstants.FIXED_WIDTH_EMPHASIS_FONT_NAME,
            button_font_size=GUIConstants.BUTTON_FONT_SIZE + 4,
            is_button_text_centered=False,
            is_bottom_list=True,
            selected_button=self.selected_button_index,
            scroll_y_initial_offset=self.initial_scroll,
        )

        if selected_menu_num == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)
        
        if selected_menu_num == len(addresses):
            # User clicked NEXT
            return Destination(ToolsAddressExplorerAddressListView, view_args=dict(is_change=self.is_change, start_index=self.start_index + addrs_per_screen))
        
        # Preserve the list's current scroll so we can return to the same spot
        initial_scroll = self.screen.buttons[0].scroll_y

        index = selected_menu_num + self.start_index
        return Destination(
            ToolsAddressExplorerAddressView,
            view_args={
                'index': index,
                'address': addresses[selected_menu_num],
                'is_change': self.is_change,
                'start_index': self.start_index,
                'parent_initial_scroll': initial_scroll
            },
            skip_current_view=True
        )


class ToolsAddressExplorerAddressView(View):
    def __init__(self, index: int, address: str, is_change: bool, start_index: int, parent_initial_scroll: int = 0):
        super().__init__()
        self.index = index
        self.address = address
        self.is_change = is_change
        self.start_index = start_index
        self.parent_initial_scroll = parent_initial_scroll
    
    def run(self):
        from xmrsigner.gui.screens.screen import QRDisplayScreen
        qr_encoder = EncodeQR(qr_type=QRType.MONERO_ADDRESS, monero_address=self.address)
        self.run_screen(
            QRDisplayScreen,
            qr_encoder=qr_encoder,
        )
    
        # Exiting/Cancelling the QR display screen always returns to the list
        return Destination(
            ToolsAddressExplorerAddressListView,
            view_args={
                'is_change': self.is_change,
                'start_index': self.start_index,
                'selected_button_index': self.index - self.start_index,
                'initial_scroll': self.parent_initial_scroll
            },
            skip_current_view=True
        )
