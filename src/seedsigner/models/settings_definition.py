from dataclasses import dataclass
from typing import Any, List



class SettingsConstants:
    # Basic defaults
    OPTION__ENABLED = "E"
    OPTION__DISABLED = "D"
    OPTION__PROMPT = "P"
    OPTION__REQUIRED = "R"
    OPTIONS__ENABLED_DISABLED = [
        (OPTION__ENABLED, "Enabled"),
        (OPTION__DISABLED, "Disabled"),
    ]
    OPTIONS__PROMPT_REQUIRED_DISABLED = [
        (OPTION__PROMPT, "Prompt"),
        (OPTION__REQUIRED, "Required"),
        (OPTION__DISABLED, "Disabled"),
    ]
    OPTIONS__ENABLED_DISABLED_REQUIRED = OPTIONS__ENABLED_DISABLED +[
        (OPTION__REQUIRED, "Required"),
    ]
    OPTIONS__ENABLED_DISABLED_PROMPT = OPTIONS__ENABLED_DISABLED + [
        (OPTION__PROMPT, "Prompt"),
    ]
    ALL_OPTIONS = OPTIONS__ENABLED_DISABLED_PROMPT + [
        (OPTION__REQUIRED, "Required"),
    ]

    # User-facing selection options
    COORDINATOR__BLUE_WALLET = "bw"
    COORDINATOR__NUNCHUK = "nun"
    COORDINATOR__SPARROW = "spa"
    COORDINATOR__SPECTER_DESKTOP = "spd"
    ALL_COORDINATORS = [
        (COORDINATOR__BLUE_WALLET, "BlueWallet"),
        (COORDINATOR__NUNCHUK, "Nunchuk"),
        (COORDINATOR__SPARROW, "Sparrow"),
        (COORDINATOR__SPECTER_DESKTOP, "Specter Desktop"),
    ]

    LANGUAGE__ENGLISH = "en"
    ALL_LANGUAGES = [
        (LANGUAGE__ENGLISH, "English"),
    ]

    XMR_DENOMINATION__XMR = "xmr"
    XMR_DENOMINATION__ATOMICUNITS = "atomicunits"
    XMR_DENOMINATION__THRESHOLD = "thr"
    XMR_DENOMINATION__XMRATOMICUNITSHYBRID = "hyb"
    ALL_XMR_DENOMINATIONS = [
        (XMR_DENOMINATION__XMR, "Xmr-only"),
        (XMR_DENOMINATION__ATOMICUNITS, "AtomicUnits-only"),
        (XMR_DENOMINATION__THRESHOLD, "Threshold at 0.01"),
        (XMR_DENOMINATION__XMRATOMICUNITSHYBRID, "Xmr | AtomicUnits hybrid"),
    ]

    CAMERA_ROTATION__0 = 0
    CAMERA_ROTATION__90 = 90
    CAMERA_ROTATION__180 = 180
    CAMERA_ROTATION__270 = 270
    ALL_CAMERA_ROTATIONS = [
        (CAMERA_ROTATION__0, "0°"),
        (CAMERA_ROTATION__90, "90°"),
        (CAMERA_ROTATION__180, "180°"),
        (CAMERA_ROTATION__270, "270°"),
    ]

    # QR code constants
    DENSITY__LOW = "L"
    DENSITY__MEDIUM = "M"
    DENSITY__HIGH = "H"
    ALL_DENSITIES = [
        (DENSITY__LOW, "Low"),
        (DENSITY__MEDIUM, "Medium"),
        (DENSITY__HIGH, "High"),
    ]

    # Seed-related constants
    MAINNET = "M"
    TESTNET = "T"
    STAGENET = "S"
    ALL_NETWORKS = [
        (MAINNET, "Mainnet"),
        (TESTNET, "Testnet"),
        (STAGENET, "Stagenet")
    ]

    @classmethod
    def map_network_to_embit(cls, network) -> str: # TODO: remove comment after 2024-06-10, do we need that for monero, what relays on it?
        if network == SettingsConstants.MAINNET:
            return "main"
        elif network == SettingsConstants.TESTNET:
            return "test"
        if network == SettingsConstants.STAGENET:
            return "regtest"
    

    SINGLE_SIG = "ss"
    MULTISIG = "ms"
    ALL_SIG_TYPES = [
        (SINGLE_SIG, "Single Sig"),
        (MULTISIG, "Multisig"),
    ]

    LEGACY_P2PKH = "leg"  # Intentionally excluded from ALL_SCRIPT_TYPES  # TODO: remove
    NATIVE_SEGWIT = "nat"  # TODO: remove
    NESTED_SEGWIT = "nes"  # TODO: remove
    TAPROOT = "tr"  # TODO: remove
    CUSTOM_DERIVATION = "cus"  # TODO: remove
    ALL_SCRIPT_TYPES = [  # TODO: check before 2024-06-04 as far I am aware there is only one valid way in Monero, check and remove if I'm right
        (NATIVE_SEGWIT, "Native Segwit"),
        (NESTED_SEGWIT, "Nested Segwit (legacy)"),
        (TAPROOT, "Taproot"),
        (CUSTOM_DERIVATION, "Custom Derivation"),
    ]

    WORDLIST_LANGUAGE__ENGLISH = "en"  # TODO: remove comment before 2024-06-10 handle differences in wordlist languages in monero seed and polyseed, think should be handled in the wordlist implementations instead
    WORDLIST_LANGUAGE__CHINESE_SIMPLIFIED = "zh_Hans_CN"
    WORDLIST_LANGUAGE__CHINESE_TRADITIONAL = "zh_Hant_TW"
    WORDLIST_LANGUAGE__FRENCH = "fr"
    WORDLIST_LANGUAGE__ITALIAN = "it"
    WORDLIST_LANGUAGE__JAPANESE = "jp"
    WORDLIST_LANGUAGE__KOREAN = "kr"
    WORDLIST_LANGUAGE__PORTUGUESE = "pt"
    WORDLIST_LANGUAGE__DUTCH = "nl"
    WORDLIST_LANGUAGE__GERMAN = "de"
    WORDLIST_LANGUAGE__RUSSIAN = "ru"
    WORDLIST_LANGUAGE__SPANISH = "es"
    WORDLIST_LANGUAGE__LOJBAN = "lojban"
    WORDLIST_LANGUAGE__ESPERANTO = "esperanto"
    ALL_WORDLIST_LANGUAGE_ENGLISH__NAMES = {
        WORDLIST_LANGUAGE__ENGLISH: 'English',
        WORDLIST_LANGUAGE__CHINESE_SIMPLIFIED: "Chinese (simplified)",
        WORDLIST_LANGUAGE__FRENCH: "French",
        WORDLIST_LANGUAGE__ITALIAN: "Italian",
        WORDLIST_LANGUAGE__JAPANESE: "Japanese",
        WORDLIST_LANGUAGE__PORTUGUESE: "Portuguese",
        WORDLIST_LANGUAGE__DUTCH: "Dutch",
        WORDLIST_LANGUAGE__GERMAN: "German",
        WORDLIST_LANGUAGE__RUSSIAN: "Russian",
        WORDLIST_LANGUAGE__SPANISH: "Spanish",
        WORDLIST_LANGUAGE__LOJBAN: "Lojban",
        WORDLIST_LANGUAGE__ESPERANTO: "Esperanto"
    }
    ALL_WORDLIST_LANGUAGES = [
        (WORDLIST_LANGUAGE__ENGLISH, "English"),
        # (WORDLIST_LANGUAGE__CHINESE_SIMPLIFIED, "简体中文"),
        # (WORDLIST_LANGUAGE__CHINESE_TRADITIONAL, "繁體中文"),
        # (WORDLIST_LANGUAGE__FRENCH, "Français"),
        # (WORDLIST_LANGUAGE__ITALIAN, "Italiano"),
        # (WORDLIST_LANGUAGE__JAPANESE, "日本語"),
        # (WORDLIST_LANGUAGE__KOREAN, "한국어"),
        # (WORDLIST_LANGUAGE__PORTUGUESE, "Português"),
    ]

    
    # Individual SettingsEntry attr_names
    SETTING__LANGUAGE = "language"
    SETTING__WORDLIST_LANGUAGE = "wordlist_language"  # TODO: remove after 2024-06-10, maybe there should be SETTING__WORDLIST_LANGUAGE_MONERO and SETTING__WORDLIST_LANGUAGE_POLYSEED? Makes this even sense, should it not be more dynamic letting the responsibility to the monero, polyseed implementation to have it more future proof?
    SETTING__PERSISTENT_SETTINGS = "persistent_settings"
    SETTING__COORDINATORS = "coordinators"  # TODO: remove before 2024-06-04, WTF are coordinators, does that make any sense for monero? Check, educate yourself and remove if not needed. As far I come there it seems like every walltet in Bitcoin ecosystem has it's own way to communicate, we should use always with UR the same way!
    SETTING__XMR_DENOMINATION = "denomination"

    SEETING__LOW_SECURITY = 'low_security'
    SETTING__NETWORK = "network"
    SETTING__QR_DENSITY = "qr_density"
    SETTING__SIG_TYPES = "sig_types"
    SETTING__SCRIPT_TYPES = "script_types"
    SETTING__MONERO_SEED_PASSPHRASE = "monero_seed_passphrase"
    SETTING__POLYSEED_PASSPHRASE = "polyseed_passphrase"
    SETTING__CAMERA_ROTATION = "camera_rotation"
    SETTING__COMPACT_SEEDQR = "compact_seedqr"
    SETTING__PRIVACY_WARNINGS = "privacy_warnings"
    SETTING__DIRE_WARNINGS = "dire_warnings"
    SETTING__PARTNER_LOGOS = "partner_logos"

    SETTING__DEBUG = "debug"

    # Hidden settings
    SETTING__QR_BRIGHTNESS = "qr_background_color"


    # Structural constants
    # TODO: Not using these for display purposes yet (ever?)
    CATEGORY__SYSTEM = "system"
    CATEGORY__DISPLAY = "display"
    CATEGORY__WALLET = "wallet"
    CATEGORY__FEATURES = "features"

    VISIBILITY__GENERAL = "general"
    VISIBILITY__ADVANCED = "advanced"
    VISIBILITY__DEVELOPER = "developer"
    VISIBILITY__HIDDEN = "hidden"   # For data-only (e.g. custom_derivation), not configurable by the user

    # TODO:SEEDSIGNER: Is there really a difference between ENABLED and PROMPT?
    TYPE__ENABLED_DISABLED = "enabled_disabled"
    TYPE__ENABLED_DISABLED_PROMPT = "enabled_disabled_prompt"
    TYPE__ENABLED_DISABLED_PROMPT_REQUIRED = "enabled_disabled_prompt_required"
    TYPE__SELECT_1 = "select_1"
    TYPE__MULTISELECT = "multiselect"
    TYPE__FREE_ENTRY = "free_entry"

    ALL_ENABLED_DISABLED_TYPES = [
        TYPE__ENABLED_DISABLED,
        TYPE__ENABLED_DISABLED_PROMPT,
        TYPE__ENABLED_DISABLED_PROMPT_REQUIRED,
    ]


@dataclass
class SettingsEntry:
    """
        Defines all the parameters for a single settings entry.

        * category: Mostly for organizational purposes when displaying options in the
            SettingsQR UI. Potentially an additional sub-level breakout in the menus
            on the device itself, too.
        
        * selection_options: May be specified as a List(Any) or List(tuple(Any, str)).
            The tuple form is to provide a human-readable display_name. Probably all
            entries should shift to using the tuple form.
    """
    # TODO:SEEDSIGNER: Handle multi-language `display_name` and `help_text`
    category: str
    attr_name: str
    display_name: str
    verbose_name: str = None
    abbreviated_name: str = None
    visibility: str = SettingsConstants.VISIBILITY__GENERAL
    type: str = SettingsConstants.TYPE__ENABLED_DISABLED
    help_text: str = None
    selection_options: List[str] = None
    default_value: Any = None

    def __post_init__(self):
        if self.type == SettingsConstants.TYPE__ENABLED_DISABLED:
            self.selection_options = SettingsConstants.OPTIONS__ENABLED_DISABLED

        elif self.type == SettingsConstants.TYPE__ENABLED_DISABLED_PROMPT:
            self.selection_options = SettingsConstants.OPTIONS__ENABLED_DISABLED_PROMPT

        elif self.type == SettingsConstants.TYPE__ENABLED_DISABLED_PROMPT_REQUIRED:
            self.selection_options = [SettingsConstants.ALL_OPTIONS]

        # Account for List[tuple] and tuple formats as default_value        
        if type(self.default_value) == list and type(self.default_value[0]) == tuple:
            self.default_value = [v[0] for v in self.default_value]
        elif type(self.default_value) == tuple:
            self.default_value = self.default_value[0]


    @property
    def selection_options_display_names(self) -> List[str]:
        if type(self.selection_options[0]) == tuple:
            return [v[1] for v in self.selection_options]
        else:
            # Always return a copy so the original can't be altered
            return list(self.selection_options)


    def get_selection_option_value(self, i: int):
        value = self.selection_options[i]
        if type(value) == tuple:
            value = value[0]
        return value


    def get_selection_option_display_name(self, i: int) -> str:
        value = self.selection_options[i]
        if type(value) == tuple:
            value = value[1]
        return value
    
    
    def get_selection_option_display_name_by_value(self, value) -> str:
        for option in self.selection_options:
            if type(option) == tuple:
                option_value = option[0]
                display_name = option[1]
            else:
                option_value = option
                display_name = option
            if option_value == value:
                return display_name


    def get_selection_option_value_by_display_name(self, display_name: str):
        for option in self.selection_options:
            if type(option) == tuple:
                option_value = option[0]
                option_display_name = option[1]
            else:
                option_value = option
                option_display_name = option
            if option_display_name == display_name:
                return option_value


    def to_dict(self) -> dict:
        if self.selection_options:
            selection_options = []
            for option in self.selection_options:
                if type(option) == tuple:
                    value = option[0]
                    display_name = option[1]
                else:
                    display_name = option
                    value = option
                selection_options.append({
                    "display_name": display_name,
                    "value": value
                })
        else:
            selection_options = None

        return {
            "category": self.category,
            "attr_name": self.attr_name,
            "display_name": self.display_name,
            "verbose_name": self.verbose_name,
            "abbreviated_name": self.abbreviated_name,
            "visibility": self.visibility,
            "type": self.type,
            "help_text": self.help_text,
            "selection_options": selection_options,
            "default_value": self.default_value,
        }



class SettingsDefinition:
    """
        Master list of all settings, their possible options, their defaults, on-device
        display strings, and enriched SettingsQR UI options.

        Used to auto-build the Settings UI menuing with no repetitive boilerplate code.

        Defines the on-disk persistent storage structure and can read that format back
        and validate the values.

        Used to generate a master json file that documents all these params which can
        then be read in by the SettingsQR UI to auto-generate the necessary html inputs.
    """
    # Increment if there are any breaking changes; write migrations to bridge from
    # incompatible prior versions.
    version: int = 1

    settings_entries: List[SettingsEntry] = [
        # General options

        # TODO:SEEDSIGNER: Full babel multilanguage support! Until then, type == HIDDEN
        SettingsEntry(category=SettingsConstants.CATEGORY__SYSTEM,
                      attr_name=SettingsConstants.SETTING__LANGUAGE,
                      display_name="Language",
                      type=SettingsConstants.TYPE__SELECT_1,
                      visibility=SettingsConstants.VISIBILITY__HIDDEN,
                      selection_options=SettingsConstants.ALL_LANGUAGES,
                      default_value=SettingsConstants.LANGUAGE__ENGLISH),

        # TODO:SEEDSIGNER: Support other bip-39 wordlist languages! Until then, type == HIDDEN
        SettingsEntry(category=SettingsConstants.CATEGORY__SYSTEM,
                      attr_name=SettingsConstants.SETTING__WORDLIST_LANGUAGE,
                      display_name="Mnemonic language",
                      type=SettingsConstants.TYPE__SELECT_1,
                      visibility=SettingsConstants.VISIBILITY__HIDDEN,
                      selection_options=SettingsConstants.ALL_WORDLIST_LANGUAGES,
                      default_value=SettingsConstants.WORDLIST_LANGUAGE__ENGLISH),

        SettingsEntry(category=SettingsConstants.CATEGORY__SYSTEM,
                      attr_name=SettingsConstants.SETTING__PERSISTENT_SETTINGS,
                      display_name="Persistent settings",
                      help_text="Store Settings on SD card.",
                      default_value=SettingsConstants.OPTION__DISABLED),

        # SettingsEntry(category=SettingsConstants.CATEGORY__WALLET,  TODO: remove before 2024-06-10 Coordinators needed for out purpose?
        #              attr_name=SettingsConstants.SETTING__COORDINATORS,
        #              display_name="Coordinator software",
        #              type=SettingsConstants.TYPE__MULTISELECT,
        #              selection_options=SettingsConstants.ALL_COORDINATORS,
        #              default_value=SettingsConstants.ALL_COORDINATORS),

        SettingsEntry(category=SettingsConstants.CATEGORY__SYSTEM,
                      attr_name=SettingsConstants.SETTING__XMR_DENOMINATION,
                      display_name="Denomination display",
                      type=SettingsConstants.TYPE__SELECT_1,
                      selection_options=SettingsConstants.ALL_XMR_DENOMINATIONS,
                      default_value=SettingsConstants.XMR_DENOMINATION__THRESHOLD),
     

        # Advanced options
        SettingsEntry(category=SettingsConstants.CATEGORY__FEATURES,
                      attr_name=SettingsConstants.SETTING__NETWORK,
                      display_name="Monero network",
                      type=SettingsConstants.TYPE__SELECT_1,
                      visibility=SettingsConstants.VISIBILITY__ADVANCED,
                      selection_options=SettingsConstants.ALL_NETWORKS,
                      default_value=SettingsConstants.MAINNET),

        SettingsEntry(category=SettingsConstants.CATEGORY__FEATURES,
                      attr_name=SettingsConstants.SETTING__QR_DENSITY,
                      display_name="QR code density",
                      type=SettingsConstants.TYPE__SELECT_1,
                      visibility=SettingsConstants.VISIBILITY__ADVANCED,
                      selection_options=SettingsConstants.ALL_DENSITIES,
                      default_value=SettingsConstants.DENSITY__MEDIUM),

        SettingsEntry(category=SettingsConstants.CATEGORY__FEATURES,
                      attr_name=SettingsConstants.SETTING__SIG_TYPES,
                      display_name="Sig types",
                      type=SettingsConstants.TYPE__MULTISELECT,
                      visibility=SettingsConstants.VISIBILITY__ADVANCED,
                      selection_options=SettingsConstants.ALL_SIG_TYPES,
                      default_value=SettingsConstants.ALL_SIG_TYPES),

        SettingsEntry(category=SettingsConstants.CATEGORY__FEATURES,  # TODO: expire 2024-06-10, seems not relevant to Monero, double check before removing
                      attr_name=SettingsConstants.SETTING__SCRIPT_TYPES,
                      display_name="Script types",
                      type=SettingsConstants.TYPE__MULTISELECT,
                      visibility=SettingsConstants.VISIBILITY__ADVANCED,
                      selection_options=SettingsConstants.ALL_SCRIPT_TYPES,
                      default_value=[SettingsConstants.NATIVE_SEGWIT, SettingsConstants.NESTED_SEGWIT]),

        SettingsEntry(category=SettingsConstants.CATEGORY__FEATURES,
                      attr_name=SettingsConstants.SETTING__MONERO_SEED_PASSPHRASE,
                      display_name="Monero seed passphrase",
                      type=SettingsConstants.TYPE__SELECT_1,
                      visibility=SettingsConstants.VISIBILITY__HIDDEN,  # TODO: change to VISIBILITY__ADVANCED after implementing passwords for monero seeds, is hidden because this feature is posponed because of insane password derivation method in monero (CryptoNight, need to transpile to python, very propably other #rabbit-hole, be aware before starting!)
                      selection_options=SettingsConstants.OPTIONS__ENABLED_DISABLED_REQUIRED,
                      default_value=SettingsConstants.OPTION__DISABLED),

        SettingsEntry(category=SettingsConstants.CATEGORY__FEATURES,
                      attr_name=SettingsConstants.SETTING__POLYSEED_PASSPHRASE,
                      display_name="Polyseed passphrase",
                      type=SettingsConstants.TYPE__SELECT_1,
                      visibility=SettingsConstants.VISIBILITY__ADVANCED,
                      selection_options=SettingsConstants.OPTIONS__ENABLED_DISABLED_REQUIRED,
                      default_value=SettingsConstants.OPTION__ENABLED),

        SettingsEntry(category=SettingsConstants.CATEGORY__FEATURES,
                      attr_name=SettingsConstants.SETTING__CAMERA_ROTATION,
                      display_name="Camera rotation",
                      type=SettingsConstants.TYPE__SELECT_1,
                      visibility=SettingsConstants.VISIBILITY__ADVANCED,
                      selection_options=SettingsConstants.ALL_CAMERA_ROTATIONS,
                      default_value=SettingsConstants.CAMERA_ROTATION__0),

        SettingsEntry(category=SettingsConstants.CATEGORY__FEATURES,
                      attr_name=SettingsConstants.SETTING__COMPACT_SEEDQR,
                      display_name="CompactSeedQR",
                      visibility=SettingsConstants.VISIBILITY__ADVANCED,
                      default_value=SettingsConstants.OPTION__DISABLED),

        SettingsEntry(category=SettingsConstants.CATEGORY__FEATURES,
                      attr_name=SettingsConstants.SETTING__PRIVACY_WARNINGS,
                      display_name="Show privacy warnings",
                      visibility=SettingsConstants.VISIBILITY__ADVANCED,
                      default_value=SettingsConstants.OPTION__ENABLED),

        SettingsEntry(category=SettingsConstants.CATEGORY__FEATURES,
                      attr_name=SettingsConstants.SEETING__LOW_SECURITY ,
                      display_name="Low security",
                      visibility=SettingsConstants.VISIBILITY__ADVANCED,
                      default_value=SettingsConstants.OPTION__DISABLED),

        SettingsEntry(category=SettingsConstants.CATEGORY__FEATURES,
                      attr_name=SettingsConstants.SETTING__DIRE_WARNINGS,
                      display_name="Show dire warnings",
                      visibility=SettingsConstants.VISIBILITY__ADVANCED,
                      default_value=SettingsConstants.OPTION__ENABLED),

        SettingsEntry(category=SettingsConstants.CATEGORY__FEATURES,
                      attr_name=SettingsConstants.SETTING__PARTNER_LOGOS,
                      display_name="Show partner logos",
                      visibility=SettingsConstants.VISIBILITY__ADVANCED,
                      default_value=SettingsConstants.OPTION__DISABLED),

        # Developer options TODO: well, would prefer to not include developer options into the code base for security reasons, but rather modify the code on the fly on making an image WITH HUGE WARNINGS EVERYWHERE: not for production purposes, so I think how it was anyway not used, remove this entirely before 2024-04-10
        # TODO:SEEDSIGNER: No real Developer options needed yet. Disable for now.
        # SettingsEntry(category=SettingsConstants.CATEGORY__SYSTEM,
        #               attr_name=SettingsConstants.SETTING__DEBUG,
        #               display_name="Debug",
        #               visibility=SettingsConstants.VISIBILITY__DEVELOPER,
        #               default_value=SettingsConstants.OPTION__DISABLED),
        
        # "Hidden" settings with no UI interaction
        SettingsEntry(category=SettingsConstants.CATEGORY__SYSTEM,
                      attr_name=SettingsConstants.SETTING__QR_BRIGHTNESS,
                      display_name="QR background color",
                      type=SettingsConstants.TYPE__FREE_ENTRY,
                      visibility=SettingsConstants.VISIBILITY__HIDDEN,
                      default_value=189),
    ]


    @classmethod
    def get_settings_entries(cls, visibiilty: str = SettingsConstants.VISIBILITY__GENERAL) -> List[SettingsEntry]:
        entries = []
        for entry in cls.settings_entries:
            if entry.visibility == visibiilty:
                entries.append(entry)
        return entries
    

    @classmethod
    def get_settings_entry(cls, attr_name) -> SettingsEntry:
        for entry in cls.settings_entries:
            if entry.attr_name == attr_name:
                return entry


    @classmethod
    def get_defaults(cls) -> dict:
        as_dict = {}
        for entry in SettingsDefinition.settings_entries:
            if type(entry.default_value) == list:
                # Must copy the default_value list, otherwise we'll inadvertently change
                # defaults when updating these attrs
                as_dict[entry.attr_name] = list(entry.default_value)
            else:
                as_dict[entry.attr_name] = entry.default_value
        return as_dict


    @classmethod
    def to_dict(cls) -> dict:
        output = {
            "settings_entries": [],
        }
        for settings_entry in cls.settings_entries:
            output["settings_entries"].append(settings_entry.to_dict())
        
        return output



if __name__ == "__main__":
    import json

    output_file = "settings_definition.json"
    with open(output_file, 'w') as json_file:
        json.dump(SettingsDefinition.to_dict(), json_file, indent=4)
