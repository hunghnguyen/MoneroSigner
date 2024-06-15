import hashlib
import os
import time

from PIL import Image
from PIL.ImageOps import autocontrast

from xmrsigner.hardware.camera import Camera
from xmrsigner.gui.components import FontAwesomeIconConstants
from xmrsigner.gui.screens import (RET_CODE__BACK_BUTTON, ButtonListScreen, DireWarningScreen)
from xmrsigner.gui.screens.tools_screens import ToolsCalcFinalWordFinalizePromptScreen, ToolsCalcFinalWordScreen, ToolsCoinFlipEntryScreen, ToolsDiceEntropyEntryScreen, ToolsImageEntropyFinalImageScreen, ToolsImageEntropyLivePreviewScreen, ToolsCalcFinalWordDoneScreen
from xmrsigner.helpers import mnemonic_generation
from xmrsigner.helpers import polyseed_mnemonic_generation
from xmrsigner.models.seed import Seed
from xmrsigner.models.polyseed import PolyseedSeed
from xmrsigner.models.settings_definition import SettingsConstants
from xmrsigner.views.seed_views import SeedDiscardView, SeedFinalizeView, SeedMnemonicEntryView, SeedWordsWarningView
from monero.seed import Seed as MoneroSeed

from .view import View, Destination, BackStackView


class ToolsMenuView(View):
    def __init__(self, secure_only: bool = False):
        super().__init__()
        self.secure_only = secure_only

    def run(self):
        IMAGE = (" New seed", FontAwesomeIconConstants.CAMERA)
        DICE = ("New seed", FontAwesomeIconConstants.DICE)
        KEYBOARD = ("Pick own words", FontAwesomeIconConstants.KEYBOARD)  # TODO: expire 2024-06-21, I think there should be a warning that this way most probale will lead to low entropy, should only be used if user is really knowing what he is doing... Maybe an alternative would be to use it as input entropy with pseudo entropy to generate a new "now magically random" (of course not, but at least with less probability of user picking the most prefered words out of the list and shootig himself in the foot.
        if self.secure_only or self.settings.get_value(SettingsConstants.SEETING__LOW_SECURITY) == SettingsConstants.OPTION__DISABLED:
            button_data = [IMAGE, DICE]
        else:
            button_data = [IMAGE, DICE, KEYBOARD]
        screen = ButtonListScreen(
            title="Tools",
            is_button_text_centered=False,
            button_data=button_data
        )
        selected_menu_num = screen.display()

        if selected_menu_num == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)

        elif button_data[selected_menu_num] == IMAGE:
            return Destination(ToolsImageEntropyLivePreviewView)

        elif button_data[selected_menu_num] == DICE:
            return Destination(ToolsDiceSeedTypeView)

        elif button_data[selected_menu_num] == KEYBOARD:
            return Destination(ToolsCalcFinalWordWarningView)



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
            # Take the final full-res image
            camera = Camera.get_instance()
            camera.start_single_frame_mode(resolution=(720, 480))
            time.sleep(0.25)
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
            stream = os.popen("cat /proc/cpuinfo | grep Serial")
            output = stream.read()
            serial_num = output.split(":")[-1].strip().encode('utf-8')
            serial_hash = hashlib.sha256(serial_num)
            hash_bytes = serial_hash.digest()
        except Exception as e:
            print(repr(e))
            hash_bytes = b'0'

        # Build in modest entropy via millis since power on
        millis_hash = hashlib.sha256(hash_bytes + str(time.time()).encode('utf-8'))
        hash_bytes = millis_hash.digest()

        # Build in better entropy by chaining the preview frames
        for frame in preview_images:
            img_hash = hashlib.sha256(hash_bytes + frame.tobytes())
            hash_bytes = img_hash.digest()

        # Finally build in our headline entropy via the new full-res image
        final_hash = hashlib.sha256(hash_bytes + seed_entropy_image.tobytes()).digest()

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
            stream = os.popen("cat /proc/cpuinfo | grep Serial")
            output = stream.read()
            serial_num = output.split(":")[-1].strip().encode('utf-8')
            serial_hash = hashlib.sha256(serial_num)
            hash_bytes = serial_hash.digest()
        except Exception as e:
            print(repr(e))
            hash_bytes = b'0'

        # Build in modest entropy via millis since power on
        millis_hash = hashlib.sha256(hash_bytes + str(time.time()).encode('utf-8'))
        hash_bytes = millis_hash.digest()

        # Build in better entropy by chaining the preview frames
        for frame in preview_images:
            img_hash = hashlib.sha256(hash_bytes + frame.tobytes())
            hash_bytes = img_hash.digest()

        # Finally build in our headline entropy via the new full-res image
        final_hash = hashlib.sha256(hash_bytes + seed_entropy_image.tobytes()).digest()

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
        
        print(f"Dice rolls: {ret}")
        dice_seed_phrase = mnemonic_generation.generate_mnemonic_from_dice(ret)
        print(f"""Mnemonic: "{dice_seed_phrase}" """)

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

        selected_menu_num = DireWarningScreen(
            title="Low Entropy Warning",
            show_back_button=False,
            status_headline="Are you sure?",
            text="""The most insecure way, except chosen really random.""",
            button_data=button_data
        ).display()

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
    def __init__(self, coin_flips=None):
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

