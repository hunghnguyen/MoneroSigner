# Inline Todo

## Index
- [Urgent](#urgent)
- [By File](#by-file)
- [External Todo](Todo.md)

## Urgent

### 2024-06-04
- `src/seedsigner/models/seed.py`:112
  remove comment after 2024-06-04 is there a better way for a fingerprint, is it only used to display the seeds temporarily saved?
- `src/seedsigner/models/settings_definition.py`:112
  check before 2024-06-04 as far I am aware there is only one valid way in Monero, check and remove if I'm right
- `src/seedsigner/models/settings_definition.py`:163
  remove before 2024-06-04, WTF are coordinators, does that make any sense for monero? Check, educate yourself and remove if not needed. As far I come there it seems like every walltet in Bitcoin ecosystem has it's own way to communicate, we should use always with UR the same way!
- `src/seedsigner/views/seed_views.py`:1
  remove before 2024-06-04
- `src/seedsigner/views/seed_views.py`:6
  remove before 2024-06-04
- `src/seedsigner/views/seed_views.py`:7
  remove before 2024-06-04
- `src/seedsigner/views/seed_views.py`:8
  remove before 2024-06-04
- `src/seedsigner/views/seed_views.py`:115
  check and correct, before 2024-06-04
- `src/seedsigner/views/seed_views.py`:124
  check the reasoning behind and if it can be used for monero seed and polyseed or if we need to modify/split, do before 2024-06-04!
- `src/seedsigner/views/seed_views.py`:229
  2024-06-04, handle polyseed seeds correct and check extra for that settings...
- `src/seedsigner/views/seed_views.py`:676
  expire 2024-06-04: adapt to polyseed, monero seed and view keys - we don't supportMyMonero keys for export. Wait, need to check again, seems that is meant to draw your QR codes on paper, so it would not really make sense for view keys, not? Would it? Think again about before taking decision!
- `src/seedsigner/views/seed_views.py`:759
  expire 2024-06-04, not true for view keys, but should stil be a warning that with view keys you can fuck up your privacy
- `src/seedsigner/views/seed_views.py`:824
  expire 2024-06-04, can only be 25 (monero seed) or 16 (polyseed)
- `src/seedsigner/views/seed_views.py`:930
  expire 2024-06-04, remove BTC related stuff, make it work for monero
- `src/seedsigner/views/seed_views.py`:980
  expire 2024-06-04, remove BTC stuff, make monero work
- `src/seedsigner/views/tools_views.py`:147
  expire 2024-06-04 should be merged with ToolsImagePolyseedView, same code and be outsid of views...
- `src/seedsigner/views/tools_views.py`:200
  expire 2024-06-04 should be merged with ToolsImageEntropyMnemonicLengthView, same code and be outsid of views...
- `src/seedsigner/views/tools_views.py`:376
  2024-06-04, rename, because it is missleading, the only thing what will be calculated is the checksum word
- `src/seedsigner/views/tools_views.py`:388
  2024-06-04 hot fix, make it right, seems actually right to add checksum

### 2024-06-10
- `src/seedsigner/helpers/polyseed_mnemonic_generation.py`:6
  expire 2024-06-10, I think should be moved/merged with mnemonic_generation somehow and somewhere else, think about it.
- `src/seedsigner/models/settings_definition.py`:91
  remove comment after 2024-06-10, do we need that for monero, what relays on it?
- `src/seedsigner/models/settings_definition.py`:119
  remove comment before 2024-06-10 handle differences in wordlist languages in monero seed and polyseed, think should be handled in the wordlist implementations instead
- `src/seedsigner/models/settings_definition.py`:161
  remove after 2024-06-10, maybe there should be SETTING__WORDLIST_LANGUAGE_MONERO and SETTING__WORDLIST_LANGUAGE_POLYSEED? Makes this even sense, should it not be more dynamic letting the responsibility to the monero, polyseed implementation to have it more future proof?
- `src/seedsigner/models/settings_definition.py`:417
  expire 2024-06-10, seems not relevant to Monero, double check before removing
- `src/seedsigner/views/seed_views.py`:142
  heritage from seedsigner, remove before 2024-06-10
- `src/seedsigner/views/seed_views.py`:348
  expire 2024-06-10, here should be probably the option to export the view keys
- `src/seedsigner/views/seed_views.py`:423
  expire 2024-06-10, base for view key export
- `src/seedsigner/views/seed_views.py`:454
  adapt for master keys and view keys only before 2024-06-10
- `src/seedsigner/views/seed_views.py`:466
  no warning or different warning for view keys, adapt before 2024-06-10
- `src/seedsigner/views/seed_views.py`:470
  see todo above, adapt text to master key and view keys before 2024-06-10
- `src/seedsigner/views/seed_views.py`:483
  expire 2024-06-10, handle differences between masters key and view keys
- `src/seedsigner/views/seed_views.py`:1082
  expire 2024-06-10, what is that about??? Remove BTC stuff and make it for monero working. If not needed for monero, remove it
- `src/seedsigner/views/seed_views.py`:1202
  expire 2024-06-10, guess not needed for monero, so remove if not needed
- `src/seedsigner/views/seed_views.py`:1292
  expire 2024-06-10, check if needed for monero, delete or modify
- `src/seedsigner/views/seed_views.py`:1320
  expire 2024-06-10, adapt to monero
- `src/seedsigner/views/seed_views.py`:1341
  expire 2024-06-10, adapt to monero

### 2024-06-21
- `src/seedsigner/views/tools_views.py`:28
  expire 2024-06-21, I think there should be a warning that this way most probale will lead to low entropy, should only be used if user is really knowing what he is doing... Maybe an alternative would be to use it as input entropy with pseudo entropy to generate a new "now magically random" (of course not, but at least with less probability of user picking the most prefered words out of the list and shootig himself in the foot.

### 2024-06-30
- `src/seedsigner/views/seed_views.py`:156
  2024-06-30, clean up, this code is no functional but uggly as fuck!
- `src/seedsigner/views/seed_views.py`:160
  expire 2024-06-30, lean it up
- `src/seedsigner/views/tools_views.py`:267
  expire 2024-06-30, offer only 25 words if not low security is set in settings

### 2024-06-31
- `src/seedsigner/views/seed_views.py`:826
  expire 2024-06-31, from there come this numbers, is this not some data comming from QR code constraints? Would it no be wise to get the number from there instead of this???

### 2024-07-01
- `src/seedsigner/gui/screens/screen.py`:130
  expire 2024-07-01, why hardcoded????
- `src/seedsigner/helpers/mnemonic_generation.py`:1
  expire 2024-07-01 what to do about this file? Do we do the same thing?
- `src/seedsigner/views/tools_views.py`:188
  expire 2024-07-01, see #todo in seedsigner.helpers.mnemonic_generation, and fix language together...
- `src/seedsigner/views/tools_views.py`:236
  expire 2024-07-01, see #todo in seedsigner.helpers.mnemonic_generation, and fix language together...

### 2024-07-31
- `src/seedsigner/helpers/mnemonic_generation.py`:12
  expire 2024-07-31, handle seed languages...
- `src/seedsigner/helpers/polyseed_mnemonic_generation.py`:9
  expire 2024-07-31, handle seed languages...
- `src/seedsigner/views/tools_views.py`:178
  expire 2024-07-31, don't know python memory managment, but `del seed_entropy_image` etc seems for me the better way, well, need to investigate, when not mistaken, python uses GC, is there a way to clean up inmedately?
- `src/seedsigner/views/tools_views.py`:226
  expire 2024-07-31, don't know python memory managment, but `del seed_entropy_image` etc seems for me the better way, well, need to investigate, when not mistaken, python uses GC, is there a way to clean up inmedately?

### No date provided
- `src/seedsigner/controller.py`:60
  **#SEEDSIGNER** Refactor these flow-related attrs that survive across multiple Screens.
- `src/seedsigner/controller.py`:61
  **#SEEDSIGNER** Should all in-memory flow-related attrs get wiped on MainMenuView?
- `src/seedsigner/controller.py`:72
  **#SEEDSIGNER** end refactor section
- `src/seedsigner/controller.py`:123
  **#SEEDSIGNER** Rename "storage" to something more indicative of its temp, in-memory state
- `src/seedsigner/gui/components.py`:15
  **#SEEDSIGNER** Remove all pixel hard coding
- `src/seedsigner/gui/components.py`:254
  **#SEEDSIGNER** Implement autosize width?
- `src/seedsigner/gui/components.py`:291
  **#SEEDSIGNER** getbbox() seems to ignore "\n" so isn't properly factored into height
- `src/seedsigner/gui/components.py`:373
  **#SEEDSIGNER** Don't render blank lines as full height
- `src/seedsigner/gui/components.py`:403
  **#SEEDSIGNER** Store resulting super-sampled image as a member var in __post_init__ and 
- `src/seedsigner/gui/components.py`:786
  change to Monero icon
- `src/seedsigner/gui/components.py`:973
  **#SEEDSIGNER** Rename the seedsigner.helpers.Buttons class (to Inputs?) to reduce confusion
- `src/seedsigner/gui/components.py`:1035
  **#SEEDSIGNER** Only apply screen_y at render
- `src/seedsigner/gui/renderer.py`:84
  **#SEEDSIGNER** Remove all references
- `src/seedsigner/gui/renderer.py`:100
  Should probably move this to screens.py
- `src/seedsigner/gui/renderer.py`:142
  **#SEEDSIGNER** Should probably move this to templates.py
- `src/seedsigner/gui/renderer.py`:148
  **#SEEDSIGNER** Should probably move this to templates.py
- `src/seedsigner/gui/screens/psbt_screens.py`:123
  **#SEEDSIGNER** Properly handle the ellipsis truncation in different languages
- `src/seedsigner/gui/screens/psbt_screens.py`:497
  **#SEEDSIGNER** Test rendering the numeric amounts without the supersampling
- `src/seedsigner/gui/screens/scan_screens.py`:124
  **#SEEDSIGNER** KEY_UP gives control to NavBar; use its back arrow to cancel
- `src/seedsigner/gui/screens/screen.py`:78
  **#SEEDSIGNER** Check self.scroll_y and only render visible elements
- `src/seedsigner/gui/screens/screen.py`:296
  **#SEEDSIGNER** Define an actual class for button_data?
- `src/seedsigner/gui/screens/screen.py`:698
  **#SEEDSIGNER** handle left as BACK
- `src/seedsigner/gui/screens/seed_screens.py`:44
  **#SEEDSIGNER** support other BIP39 languages/charsets
- `src/seedsigner/hardware/buttons.py`:52
  **#SEEDSIGNER** Refactor to keep control in the Controller and not here
- `src/seedsigner/hardware/buttons.py`:165
  **#SEEDSIGNER** Implement `release_lock` functionality as a global somewhere. Mixes up design
- `src/seedsigner/helpers/ur2/cbor_lite.py`:246
  Check that this is the right way -- do we need to use struct.unpack()?
- `src/seedsigner/helpers/ur2/fountain_decoder.py`:37
  Not efficient
- `src/seedsigner/helpers/ur2/fountain_decoder.py`:55
  Handle None?
- `src/seedsigner/helpers/ur2/fountain_decoder.py`:200
  Does this need to make a copy of p?
- `src/seedsigner/helpers/ur2/fountain_encoder.py`:35
  Do something better with this check
- `src/seedsigner/models/decode_qr.py`:114
  Convert the test suite rather than handle here?
- `src/seedsigner/models/decode_qr.py`:320
  Convert the test suite rather than handle here?
- `src/seedsigner/models/decode_qr.py`:481
  Handle regtest bcrt?
- `src/seedsigner/models/decode_qr.py`:794
  Pre-calculate this once on startup
- `src/seedsigner/models/decode_qr.py`:829
  Refactor this to work with the new SettingsDefinition
- `src/seedsigner/models/encode_qr.py`:28
  Refactor so that this is a base class with implementation classes for each
- `src/seedsigner/models/encode_qr.py`:123
  Make these properties?
- `src/seedsigner/models/psbt_parser.py`:194
  Move this to Seed?
- `src/seedsigner/models/psbt_parser.py`:200
  Is this right?
- `src/seedsigner/models/settings.py`:78
  **#SEEDSIGNER** If value is not in entry.selection_options...
- `src/seedsigner/models/settings_definition.py`:107
  remove
- `src/seedsigner/models/settings_definition.py`:108
  remove
- `src/seedsigner/models/settings_definition.py`:109
  remove
- `src/seedsigner/models/settings_definition.py`:110
  remove
- `src/seedsigner/models/settings_definition.py`:111
  remove
- `src/seedsigner/models/settings_definition.py`:186
  Not using these for display purposes yet (ever?)
- `src/seedsigner/models/settings_definition.py`:197
  **#SEEDSIGNER** Is there really a difference between ENABLED and PROMPT?
- `src/seedsigner/models/settings_definition.py`:225
  **#SEEDSIGNER** Handle multi-language `display_name` and `help_text`
- `src/seedsigner/models/settings_definition.py`:353
  **#SEEDSIGNER** Full babel multilanguage support! Until then, type == HIDDEN
- `src/seedsigner/models/settings_definition.py`:362
  **#SEEDSIGNER** Support other bip-39 wordlist languages! Until then, type == HIDDEN
- `src/seedsigner/models/settings_definition.py`:429
  change to VISIBILITY__ADVANCED after implementing passwords for monero seeds, is hidden because this feature is posponed because of insane password derivation method in monero (CryptoNight, need to transpile to python, very propably other #rabbit-hole, be aware before starting!)
- `src/seedsigner/models/settings_definition.py`:480
  **#SEEDSIGNER** No real Developer options needed yet. Disable for now.
- `src/seedsigner/views/psbt_views.py`:45
  Include lock icon on right side of button
- `src/seedsigner/views/psbt_views.py`:316
  Something is wrong with this psbt(?). Reroute to warning?
- `src/seedsigner/views/psbt_views.py`:487
  Reserved for Nick. Are there different failure scenarios that we can detect?
- `src/seedsigner/views/scan_views.py`:19
  Does this belong in its own BaseThread?
- `src/seedsigner/views/scan_views.py`:81
  Handle single-sig descriptors?
- `src/seedsigner/views/screensaver.py`:14
  This early code is now outdated vis-a-vis Screen vs View distinctions
- `src/seedsigner/views/seed_views.py`:385
  **#SEEDSIGNER** How sure are we? Should disable this entirely if we're 100% sure?
- `src/seedsigner/views/seed_views.py`:882
  **#SEEDSIGNER** Does this belong in its own BaseThread?
- `src/seedsigner/views/seed_views.py`:964
  **#SEEDSIGNER** detect single sig vs multisig or have to prompt?
- `src/seedsigner/views/seed_views.py`:1037
  **#SEEDSIGNER** Include lock icon on right side of button
- `src/seedsigner/views/seed_views.py`:1111
  **#SEEDSIGNER** Taproot addr verification
- `src/seedsigner/views/seed_views.py`:1114
  **#SEEDSIGNER** This should be in `Seed` or `PSBT` utility class
- `src/seedsigner/views/seed_views.py`:1269
  **#SEEDSIGNER** Not yet implemented!
- `src/seedsigner/views/seed_views.py`:1281
  **#SEEDSIGNER** Not yet implemented!
- `src/seedsigner/views/seed_views.py`:1285
  **#SEEDSIGNER** Not yet implemented!
- `src/seedsigner/views/seed_views.py`:1381
  **#SEEDSIGNER** Route properly when multisig brute-force addr verification is done
- `src/seedsigner/views/settings_views.py`:81
  **#SEEDSIGNER** Free-entry types (are there any?) will need their own SettingsEntryUpdateFreeEntryView(?).
- `src/seedsigner/views/view.py`:54
  Pull all rendering-related code out of Views and into gui.screens implementations

## By File

### `src/seedsigner/controller.py`
- Line 60: No date provided **#SEEDSIGNER** 
  Refactor these flow-related attrs that survive across multiple Screens.
- Line 61: No date provided **#SEEDSIGNER** 
  Should all in-memory flow-related attrs get wiped on MainMenuView?
- Line 72: No date provided **#SEEDSIGNER** 
  end refactor section
- Line 123: No date provided **#SEEDSIGNER** 
  Rename "storage" to something more indicative of its temp, in-memory state

### `src/seedsigner/gui/components.py`
- Line 15: No date provided **#SEEDSIGNER** 
  Remove all pixel hard coding
- Line 254: No date provided **#SEEDSIGNER** 
  Implement autosize width?
- Line 291: No date provided **#SEEDSIGNER** 
  getbbox() seems to ignore "\n" so isn't properly factored into height
- Line 373: No date provided **#SEEDSIGNER** 
  Don't render blank lines as full height
- Line 403: No date provided **#SEEDSIGNER** 
  Store resulting super-sampled image as a member var in __post_init__ and 
- Line 786: No date provided 
  change to Monero icon
- Line 973: No date provided **#SEEDSIGNER** 
  Rename the seedsigner.helpers.Buttons class (to Inputs?) to reduce confusion
- Line 1035: No date provided **#SEEDSIGNER** 
  Only apply screen_y at render

### `src/seedsigner/gui/renderer.py`
- Line 84: No date provided **#SEEDSIGNER** 
  Remove all references
- Line 100: No date provided 
  Should probably move this to screens.py
- Line 142: No date provided **#SEEDSIGNER** 
  Should probably move this to templates.py
- Line 148: No date provided **#SEEDSIGNER** 
  Should probably move this to templates.py

### `src/seedsigner/gui/screens/psbt_screens.py`
- Line 123: No date provided **#SEEDSIGNER** 
  Properly handle the ellipsis truncation in different languages
- Line 497: No date provided **#SEEDSIGNER** 
  Test rendering the numeric amounts without the supersampling

### `src/seedsigner/gui/screens/scan_screens.py`
- Line 124: No date provided **#SEEDSIGNER** 
  KEY_UP gives control to NavBar; use its back arrow to cancel

### `src/seedsigner/gui/screens/screen.py`
- Line 130: 2024-07-01 
  expire 2024-07-01, why hardcoded????
- Line 78: No date provided **#SEEDSIGNER** 
  Check self.scroll_y and only render visible elements
- Line 296: No date provided **#SEEDSIGNER** 
  Define an actual class for button_data?
- Line 698: No date provided **#SEEDSIGNER** 
  handle left as BACK

### `src/seedsigner/gui/screens/seed_screens.py`
- Line 44: No date provided **#SEEDSIGNER** 
  support other BIP39 languages/charsets

### `src/seedsigner/hardware/buttons.py`
- Line 52: No date provided **#SEEDSIGNER** 
  Refactor to keep control in the Controller and not here
- Line 165: No date provided **#SEEDSIGNER** 
  Implement `release_lock` functionality as a global somewhere. Mixes up design

### `src/seedsigner/helpers/mnemonic_generation.py`
- Line 1: 2024-07-01 
  expire 2024-07-01 what to do about this file? Do we do the same thing?
- Line 12: 2024-07-31 
  expire 2024-07-31, handle seed languages...

### `src/seedsigner/helpers/polyseed_mnemonic_generation.py`
- Line 6: 2024-06-10 
  expire 2024-06-10, I think should be moved/merged with mnemonic_generation somehow and somewhere else, think about it.
- Line 9: 2024-07-31 
  expire 2024-07-31, handle seed languages...

### `src/seedsigner/helpers/ur2/cbor_lite.py`
- Line 246: No date provided 
  Check that this is the right way -- do we need to use struct.unpack()?

### `src/seedsigner/helpers/ur2/fountain_decoder.py`
- Line 37: No date provided 
  Not efficient
- Line 55: No date provided 
  Handle None?
- Line 200: No date provided 
  Does this need to make a copy of p?

### `src/seedsigner/helpers/ur2/fountain_encoder.py`
- Line 35: No date provided 
  Do something better with this check

### `src/seedsigner/models/decode_qr.py`
- Line 114: No date provided 
  Convert the test suite rather than handle here?
- Line 320: No date provided 
  Convert the test suite rather than handle here?
- Line 481: No date provided 
  Handle regtest bcrt?
- Line 794: No date provided 
  Pre-calculate this once on startup
- Line 829: No date provided 
  Refactor this to work with the new SettingsDefinition

### `src/seedsigner/models/encode_qr.py`
- Line 28: No date provided 
  Refactor so that this is a base class with implementation classes for each
- Line 123: No date provided 
  Make these properties?

### `src/seedsigner/models/psbt_parser.py`
- Line 194: No date provided 
  Move this to Seed?
- Line 200: No date provided 
  Is this right?

### `src/seedsigner/models/seed.py`
- Line 112: 2024-06-04 
  remove comment after 2024-06-04 is there a better way for a fingerprint, is it only used to display the seeds temporarily saved?

### `src/seedsigner/models/settings.py`
- Line 78: No date provided **#SEEDSIGNER** 
  If value is not in entry.selection_options...

### `src/seedsigner/models/settings_definition.py`
- Line 112: 2024-06-04 
  check before 2024-06-04 as far I am aware there is only one valid way in Monero, check and remove if I'm right
- Line 163: 2024-06-04 
  remove before 2024-06-04, WTF are coordinators, does that make any sense for monero? Check, educate yourself and remove if not needed. As far I come there it seems like every walltet in Bitcoin ecosystem has it's own way to communicate, we should use always with UR the same way!
- Line 91: 2024-06-10 
  remove comment after 2024-06-10, do we need that for monero, what relays on it?
- Line 119: 2024-06-10 
  remove comment before 2024-06-10 handle differences in wordlist languages in monero seed and polyseed, think should be handled in the wordlist implementations instead
- Line 161: 2024-06-10 
  remove after 2024-06-10, maybe there should be SETTING__WORDLIST_LANGUAGE_MONERO and SETTING__WORDLIST_LANGUAGE_POLYSEED? Makes this even sense, should it not be more dynamic letting the responsibility to the monero, polyseed implementation to have it more future proof?
- Line 417: 2024-06-10 
  expire 2024-06-10, seems not relevant to Monero, double check before removing
- Line 107: No date provided 
  remove
- Line 108: No date provided 
  remove
- Line 109: No date provided 
  remove
- Line 110: No date provided 
  remove
- Line 111: No date provided 
  remove
- Line 186: No date provided 
  Not using these for display purposes yet (ever?)
- Line 197: No date provided **#SEEDSIGNER** 
  Is there really a difference between ENABLED and PROMPT?
- Line 225: No date provided **#SEEDSIGNER** 
  Handle multi-language `display_name` and `help_text`
- Line 353: No date provided **#SEEDSIGNER** 
  Full babel multilanguage support! Until then, type == HIDDEN
- Line 362: No date provided **#SEEDSIGNER** 
  Support other bip-39 wordlist languages! Until then, type == HIDDEN
- Line 429: No date provided 
  change to VISIBILITY__ADVANCED after implementing passwords for monero seeds, is hidden because this feature is posponed because of insane password derivation method in monero (CryptoNight, need to transpile to python, very propably other #rabbit-hole, be aware before starting!)
- Line 480: No date provided **#SEEDSIGNER** 
  No real Developer options needed yet. Disable for now.

### `src/seedsigner/views/psbt_views.py`
- Line 45: No date provided 
  Include lock icon on right side of button
- Line 316: No date provided 
  Something is wrong with this psbt(?). Reroute to warning?
- Line 487: No date provided 
  Reserved for Nick. Are there different failure scenarios that we can detect?

### `src/seedsigner/views/scan_views.py`
- Line 19: No date provided 
  Does this belong in its own BaseThread?
- Line 81: No date provided 
  Handle single-sig descriptors?

### `src/seedsigner/views/screensaver.py`
- Line 14: No date provided 
  This early code is now outdated vis-a-vis Screen vs View distinctions

### `src/seedsigner/views/seed_views.py`
- Line 1: 2024-06-04 
  remove before 2024-06-04
- Line 6: 2024-06-04 
  remove before 2024-06-04
- Line 7: 2024-06-04 
  remove before 2024-06-04
- Line 8: 2024-06-04 
  remove before 2024-06-04
- Line 115: 2024-06-04 
  check and correct, before 2024-06-04
- Line 124: 2024-06-04 
  check the reasoning behind and if it can be used for monero seed and polyseed or if we need to modify/split, do before 2024-06-04!
- Line 229: 2024-06-04 
  2024-06-04, handle polyseed seeds correct and check extra for that settings...
- Line 676: 2024-06-04 
  expire 2024-06-04: adapt to polyseed, monero seed and view keys - we don't supportMyMonero keys for export. Wait, need to check again, seems that is meant to draw your QR codes on paper, so it would not really make sense for view keys, not? Would it? Think again about before taking decision!
- Line 759: 2024-06-04 
  expire 2024-06-04, not true for view keys, but should stil be a warning that with view keys you can fuck up your privacy
- Line 824: 2024-06-04 
  expire 2024-06-04, can only be 25 (monero seed) or 16 (polyseed)
- Line 930: 2024-06-04 
  expire 2024-06-04, remove BTC related stuff, make it work for monero
- Line 980: 2024-06-04 
  expire 2024-06-04, remove BTC stuff, make monero work
- Line 142: 2024-06-10 
  heritage from seedsigner, remove before 2024-06-10
- Line 348: 2024-06-10 
  expire 2024-06-10, here should be probably the option to export the view keys
- Line 423: 2024-06-10 
  expire 2024-06-10, base for view key export
- Line 454: 2024-06-10 
  adapt for master keys and view keys only before 2024-06-10
- Line 466: 2024-06-10 
  no warning or different warning for view keys, adapt before 2024-06-10
- Line 470: 2024-06-10 
  see todo above, adapt text to master key and view keys before 2024-06-10
- Line 483: 2024-06-10 
  expire 2024-06-10, handle differences between masters key and view keys
- Line 1082: 2024-06-10 
  expire 2024-06-10, what is that about??? Remove BTC stuff and make it for monero working. If not needed for monero, remove it
- Line 1202: 2024-06-10 
  expire 2024-06-10, guess not needed for monero, so remove if not needed
- Line 1292: 2024-06-10 
  expire 2024-06-10, check if needed for monero, delete or modify
- Line 1320: 2024-06-10 
  expire 2024-06-10, adapt to monero
- Line 1341: 2024-06-10 
  expire 2024-06-10, adapt to monero
- Line 156: 2024-06-30 
  2024-06-30, clean up, this code is no functional but uggly as fuck!
- Line 160: 2024-06-30 
  expire 2024-06-30, lean it up
- Line 826: 2024-06-31 
  expire 2024-06-31, from there come this numbers, is this not some data comming from QR code constraints? Would it no be wise to get the number from there instead of this???
- Line 385: No date provided **#SEEDSIGNER** 
  How sure are we? Should disable this entirely if we're 100% sure?
- Line 882: No date provided **#SEEDSIGNER** 
  Does this belong in its own BaseThread?
- Line 964: No date provided **#SEEDSIGNER** 
  detect single sig vs multisig or have to prompt?
- Line 1037: No date provided **#SEEDSIGNER** 
  Include lock icon on right side of button
- Line 1111: No date provided **#SEEDSIGNER** 
  Taproot addr verification
- Line 1114: No date provided **#SEEDSIGNER** 
  This should be in `Seed` or `PSBT` utility class
- Line 1269: No date provided **#SEEDSIGNER** 
  Not yet implemented!
- Line 1281: No date provided **#SEEDSIGNER** 
  Not yet implemented!
- Line 1285: No date provided **#SEEDSIGNER** 
  Not yet implemented!
- Line 1381: No date provided **#SEEDSIGNER** 
  Route properly when multisig brute-force addr verification is done

### `src/seedsigner/views/settings_views.py`
- Line 81: No date provided **#SEEDSIGNER** 
  Free-entry types (are there any?) will need their own SettingsEntryUpdateFreeEntryView(?).

### `src/seedsigner/views/tools_views.py`
- Line 147: 2024-06-04 
  expire 2024-06-04 should be merged with ToolsImagePolyseedView, same code and be outsid of views...
- Line 200: 2024-06-04 
  expire 2024-06-04 should be merged with ToolsImageEntropyMnemonicLengthView, same code and be outsid of views...
- Line 376: 2024-06-04 
  2024-06-04, rename, because it is missleading, the only thing what will be calculated is the checksum word
- Line 388: 2024-06-04 
  2024-06-04 hot fix, make it right, seems actually right to add checksum
- Line 28: 2024-06-21 
  expire 2024-06-21, I think there should be a warning that this way most probale will lead to low entropy, should only be used if user is really knowing what he is doing... Maybe an alternative would be to use it as input entropy with pseudo entropy to generate a new "now magically random" (of course not, but at least with less probability of user picking the most prefered words out of the list and shootig himself in the foot.
- Line 267: 2024-06-30 
  expire 2024-06-30, offer only 25 words if not low security is set in settings
- Line 188: 2024-07-01 
  expire 2024-07-01, see #todo in seedsigner.helpers.mnemonic_generation, and fix language together...
- Line 236: 2024-07-01 
  expire 2024-07-01, see #todo in seedsigner.helpers.mnemonic_generation, and fix language together...
- Line 178: 2024-07-31 
  expire 2024-07-31, don't know python memory managment, but `del seed_entropy_image` etc seems for me the better way, well, need to investigate, when not mistaken, python uses GC, is there a way to clean up inmedately?
- Line 226: 2024-07-31 
  expire 2024-07-31, don't know python memory managment, but `del seed_entropy_image` etc seems for me the better way, well, need to investigate, when not mistaken, python uses GC, is there a way to clean up inmedately?

### `src/seedsigner/views/view.py`
- Line 54: No date provided 
  Pull all rendering-related code out of Views and into gui.screens implementations
