# Inline Todo

## Index
- [Urgent](#urgent)
- [By File](#by-file)
- [External Todo](Todo.md)

## Urgent

### 2024-06-04
- `src/seedsigner/views/seed_views.py`:741
  expire 2024-06-04: adapt to polyseed, monero seed and view keys - we don't supportMyMonero keys for export. Wait, need to check again, seems that is meant to draw your QR codes on paper, so it would not really make sense for view keys, not? Would it? Think again about before taking decision!
- `src/seedsigner/views/seed_views.py`:822
  expire 2024-06-04, not true for view keys, but should stil be a warning that with view keys you can fuck up your privacy
- `src/seedsigner/views/seed_views.py`:885
  expire 2024-06-04, can only be 25 (monero seed) or 16 (polyseed)
- `src/seedsigner/views/seed_views.py`:991
  expire 2024-06-04, remove BTC related stuff, make it work for monero
- `src/seedsigner/views/seed_views.py`:1041
  expire 2024-06-04, remove BTC stuff, make monero work
- `src/seedsigner/views/tools_views.py`:153
  expire 2024-06-04 should be merged with ToolsImagePolyseedView, same code and be outsid of views...
- `src/seedsigner/views/tools_views.py`:206
  expire 2024-06-04 should be merged with ToolsImageEntropyMnemonicLengthView, same code and be outsid of views...
- `src/seedsigner/views/tools_views.py`:415
  2024-06-04, rename, because it is missleading, the only thing what will be calculated is the checksum word
- `src/seedsigner/views/tools_views.py`:427
  2024-06-04 hot fix, make it right, seems actually right to add checksum

### 2024-06-10
- `src/seedsigner/gui/screens/seed_screens.py`:552
  2024-06-10, remove: Xpub related
- `src/seedsigner/gui/screens/seed_screens.py`:568
  2024-06-10, remove: Xpub related
- `src/seedsigner/helpers/polyseed_mnemonic_generation.py`:6
  expire 2024-06-10, I think should be moved/merged with mnemonic_generation somehow and somewhere else, think about it.
- `src/seedsigner/models/decode_qr.py`:702
  2024-06-10, fix to monero (and polyseed?)
- `src/seedsigner/models/encode_qr.py`:225
  2024-06-10, needs to return view only wallet URI
- `src/seedsigner/models/settings_definition.py`:96
  remove comment before 2024-06-10 handle differences in wordlist languages in monero seed and polyseed, think should be handled in the wordlist implementations instead
- `src/seedsigner/models/settings_definition.py`:138
  remove after 2024-06-10, maybe there should be SETTING__WORDLIST_LANGUAGE_MONERO and SETTING__WORDLIST_LANGUAGE_POLYSEED? Makes this even sense, should it not be more dynamic letting the responsibility to the monero, polyseed implementation to have it more future proof?
- `src/seedsigner/views/seed_views.py`:481
  2024-06-10: finish implementation
- `src/seedsigner/views/seed_views.py`:531
  no warning or different warning for view keys, adapt before 2024-06-10
- `src/seedsigner/views/seed_views.py`:535
  see todo above, adapt text to master key and view keys before 2024-06-10
- `src/seedsigner/views/seed_views.py`:1222
  expire 2024-06-10, adapt to monero
- `src/seedsigner/views/seed_views.py`:1243
  expire 2024-06-10, adapt to monero

### 2024-06-12
- `src/seedsigner/views/seed_views.py`:1194
  expire 2024-06-12, check if needed for monero, delete or modify

### 2024-06-15
- `src/seedsigner/models/decode_qr.py`:336
  2024-06-15, handle Polyseed different from here? 52 decimals (13 words, 100 decimals (25 words), 16 polyseed words would be 64 decimals
- `src/seedsigner/views/psbt_views.py`:494
  2024-06-15 remove coordinator
- `src/seedsigner/views/seed_views.py`:1143
  expire 2024-06-15, what is that about??? Remove BTC stuff and make it for monero working. If not needed for monero, remove it
- `src/seedsigner/views/seed_views.py`:1171
  2024-06-15, nonsense for us
- `src/seedsigner/views/seed_views.py`:1175
  2024-06-15, remove all the cluster fuck here, we can verify easy if a address belongs to a wallet in monero

### 2024-06-21
- `src/seedsigner/views/tools_views.py`:31
  expire 2024-06-21, I think there should be a warning that this way most probale will lead to low entropy, should only be used if user is really knowing what he is doing... Maybe an alternative would be to use it as input entropy with pseudo entropy to generate a new "now magically random" (of course not, but at least with less probability of user picking the most prefered words out of the list and shootig himself in the foot.

### 2024-06-30
- `src/seedsigner/views/seed_views.py`:155
  2024-06-30, clean up, this code is now functional but uggly as fuck!
- `src/seedsigner/views/seed_views.py`:159
  expire 2024-06-30, lean it up
- `src/seedsigner/views/tools_views.py`:273
  expire 2024-06-30, offer only 25 words if not low security is set in settings

### 2024-06-31
- `src/seedsigner/views/seed_views.py`:887
  expire 2024-06-31, from there come this numbers, is this not some data comming from QR code constraints? Would it no be wise to get the number from there instead of this???

### 2024-07-01
- `src/seedsigner/gui/screens/screen.py`:130
  expire 2024-07-01, why hardcoded????
- `src/seedsigner/helpers/mnemonic_generation.py`:1
  expire 2024-07-01 what to do about this file? Do we do the same thing?
- `src/seedsigner/views/tools_views.py`:194
  expire 2024-07-01, see #todo in seedsigner.helpers.mnemonic_generation, and fix language together...
- `src/seedsigner/views/tools_views.py`:242
  expire 2024-07-01, see #todo in seedsigner.helpers.mnemonic_generation, and fix language together...

### 2024-07-31
- `src/seedsigner/helpers/mnemonic_generation.py`:12
  expire 2024-07-31, handle seed languages...
- `src/seedsigner/helpers/polyseed_mnemonic_generation.py`:9
  expire 2024-07-31, handle seed languages...
- `src/seedsigner/views/tools_views.py`:184
  expire 2024-07-31, don't know python memory managment, but `del seed_entropy_image` etc seems for me the better way, well, need to investigate, when not mistaken, python uses GC, is there a way to clean up inmedately?
- `src/seedsigner/views/tools_views.py`:232
  expire 2024-07-31, don't know python memory managment, but `del seed_entropy_image` etc seems for me the better way, well, need to investigate, when not mistaken, python uses GC, is there a way to clean up inmedately?

### No date provided
- `src/seedsigner/controller.py`:56
  **#SEEDSIGNER** Refactor these flow-related attrs that survive across multiple Screens.
- `src/seedsigner/controller.py`:57
  **#SEEDSIGNER** Should all in-memory flow-related attrs get wiped on MainMenuView?
- `src/seedsigner/controller.py`:70
  **#SEEDSIGNER** end refactor section
- `src/seedsigner/controller.py`:121
  **#SEEDSIGNER** Rename "storage" to something more indicative of its temp, in-memory state
- `src/seedsigner/gui/components.py`:18
  **#SEEDSIGNER** Remove all pixel hard coding
- `src/seedsigner/gui/components.py`:257
  **#SEEDSIGNER** Implement autosize width?
- `src/seedsigner/gui/components.py`:294
  **#SEEDSIGNER** getbbox() seems to ignore "\n" so isn't properly factored into height
- `src/seedsigner/gui/components.py`:376
  **#SEEDSIGNER** Don't render blank lines as full height
- `src/seedsigner/gui/components.py`:406
  **#SEEDSIGNER** Store resulting super-sampled image as a member var in __post_init__ and 
- `src/seedsigner/gui/components.py`:789
  change to Monero icon
- `src/seedsigner/gui/components.py`:976
  **#SEEDSIGNER** Rename the seedsigner.helpers.Buttons class (to Inputs?) to reduce confusion
- `src/seedsigner/gui/components.py`:1038
  **#SEEDSIGNER** Only apply screen_y at render
- `src/seedsigner/gui/renderer.py`:85
  **#SEEDSIGNER** Remove all references
- `src/seedsigner/gui/renderer.py`:101
  Should probably move this to screens.py
- `src/seedsigner/gui/renderer.py`:143
  **#SEEDSIGNER** Should probably move this to templates.py
- `src/seedsigner/gui/renderer.py`:149
  **#SEEDSIGNER** Should probably move this to templates.py
- `src/seedsigner/gui/screens/psbt_screens.py`:124
  **#SEEDSIGNER** Properly handle the ellipsis truncation in different languages
- `src/seedsigner/gui/screens/psbt_screens.py`:498
  **#SEEDSIGNER** Test rendering the numeric amounts without the supersampling
- `src/seedsigner/gui/screens/scan_screens.py`:124
  **#SEEDSIGNER** KEY_UP gives control to NavBar; use its back arrow to cancel
- `src/seedsigner/gui/screens/screen.py`:78
  **#SEEDSIGNER** Check self.scroll_y and only render visible elements
- `src/seedsigner/gui/screens/screen.py`:296
  **#SEEDSIGNER** Define an actual class for button_data?
- `src/seedsigner/gui/screens/screen.py`:698
  **#SEEDSIGNER** handle left as BACK
- `src/seedsigner/gui/screens/seed_screens.py`:45
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
- `src/seedsigner/models/decode_qr.py`:109
  **#SEEDSIGNER** Convert the test suite rather than handle here?
- `src/seedsigner/models/decode_qr.py`:309
  **#SEEDSIGNER** Convert the test suite rather than handle here?
- `src/seedsigner/models/decode_qr.py`:733
  **#SEEDSIGNER** Pre-calculate this once on startup
- `src/seedsigner/models/decode_qr.py`:768
  **#SEEDSIGNER** Refactor this to work with the new SettingsDefinition
- `src/seedsigner/models/encode_qr.py`:30
  Refactor so that this is a base class with implementation classes for each
- `src/seedsigner/models/encode_qr.py`:91
  Make these properties?
- `src/seedsigner/models/psbt_parser.py`:194
  Move this to Seed?
- `src/seedsigner/models/psbt_parser.py`:200
  Is this right?
- `src/seedsigner/models/settings.py`:78
  **#SEEDSIGNER** If value is not in entry.selection_options...
- `src/seedsigner/models/settings_definition.py`:161
  Not using these for display purposes yet (ever?)
- `src/seedsigner/models/settings_definition.py`:172
  **#SEEDSIGNER** Is there really a difference between ENABLED and PROMPT?
- `src/seedsigner/models/settings_definition.py`:200
  **#SEEDSIGNER** Handle multi-language `display_name` and `help_text`
- `src/seedsigner/models/settings_definition.py`:328
  **#SEEDSIGNER** Full babel multilanguage support! Until then, type == HIDDEN
- `src/seedsigner/models/settings_definition.py`:337
  **#SEEDSIGNER** Support other bip-39 wordlist languages! Until then, type == HIDDEN
- `src/seedsigner/models/settings_definition.py`:389
  change to VISIBILITY__ADVANCED after implementing passwords for monero seeds, is hidden because this feature is posponed because of insane password derivation method in monero (CryptoNight, need to transpile to python, very propably other #rabbit-hole, be aware before starting!)
- `src/seedsigner/models/settings_definition.py`:440
  **#SEEDSIGNER** No real Developer options needed yet. Disable for now.
- `src/seedsigner/views/psbt_views.py`:45
  **#SEEDSIGNER** Include lock icon on right side of button
- `src/seedsigner/views/psbt_views.py`:316
  **#SEEDSIGNER** Something is wrong with this psbt(?). Reroute to warning?
- `src/seedsigner/views/psbt_views.py`:487
  **#SEEDSIGNER** Reserved for Nick. Are there different failure scenarios that we can detect?
- `src/seedsigner/views/scan_views.py`:19
  Does this belong in its own BaseThread?
- `src/seedsigner/views/scan_views.py`:81
  Handle single-sig descriptors?
- `src/seedsigner/views/screensaver.py`:14
  This early code is now outdated vis-a-vis Screen vs View distinctions
- `src/seedsigner/views/seed_views.py`:428
  **#SEEDSIGNER** How sure are we? Should disable this entirely if we're 100% sure?
- `src/seedsigner/views/seed_views.py`:943
  **#SEEDSIGNER** Does this belong in its own BaseThread?
- `src/seedsigner/views/seed_views.py`:1025
  **#SEEDSIGNER** detect single sig vs multisig or have to prompt?
- `src/seedsigner/views/seed_views.py`:1098
  **#SEEDSIGNER** Include lock icon on right side of button
- `src/seedsigner/views/seed_views.py`:1283
  **#SEEDSIGNER** Route properly when multisig brute-force addr verification is done
- `src/seedsigner/views/settings_views.py`:81
  **#SEEDSIGNER** Free-entry types (are there any?) will need their own SettingsEntryUpdateFreeEntryView(?).
- `src/seedsigner/views/view.py`:54
  Pull all rendering-related code out of Views and into gui.screens implementations

## By File

### `src/seedsigner/controller.py`
- Line 56: No date provided **#SEEDSIGNER** 
  Refactor these flow-related attrs that survive across multiple Screens.
- Line 57: No date provided **#SEEDSIGNER** 
  Should all in-memory flow-related attrs get wiped on MainMenuView?
- Line 70: No date provided **#SEEDSIGNER** 
  end refactor section
- Line 121: No date provided **#SEEDSIGNER** 
  Rename "storage" to something more indicative of its temp, in-memory state

### `src/seedsigner/gui/components.py`
- Line 18: No date provided **#SEEDSIGNER** 
  Remove all pixel hard coding
- Line 257: No date provided **#SEEDSIGNER** 
  Implement autosize width?
- Line 294: No date provided **#SEEDSIGNER** 
  getbbox() seems to ignore "\n" so isn't properly factored into height
- Line 376: No date provided **#SEEDSIGNER** 
  Don't render blank lines as full height
- Line 406: No date provided **#SEEDSIGNER** 
  Store resulting super-sampled image as a member var in __post_init__ and 
- Line 789: No date provided 
  change to Monero icon
- Line 976: No date provided **#SEEDSIGNER** 
  Rename the seedsigner.helpers.Buttons class (to Inputs?) to reduce confusion
- Line 1038: No date provided **#SEEDSIGNER** 
  Only apply screen_y at render

### `src/seedsigner/gui/renderer.py`
- Line 85: No date provided **#SEEDSIGNER** 
  Remove all references
- Line 101: No date provided 
  Should probably move this to screens.py
- Line 143: No date provided **#SEEDSIGNER** 
  Should probably move this to templates.py
- Line 149: No date provided **#SEEDSIGNER** 
  Should probably move this to templates.py

### `src/seedsigner/gui/screens/psbt_screens.py`
- Line 124: No date provided **#SEEDSIGNER** 
  Properly handle the ellipsis truncation in different languages
- Line 498: No date provided **#SEEDSIGNER** 
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
- Line 552: 2024-06-10 
  2024-06-10, remove: Xpub related
- Line 568: 2024-06-10 
  2024-06-10, remove: Xpub related
- Line 45: No date provided **#SEEDSIGNER** 
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
- Line 702: 2024-06-10 
  2024-06-10, fix to monero (and polyseed?)
- Line 336: 2024-06-15 
  2024-06-15, handle Polyseed different from here? 52 decimals (13 words, 100 decimals (25 words), 16 polyseed words would be 64 decimals
- Line 109: No date provided **#SEEDSIGNER** 
  Convert the test suite rather than handle here?
- Line 309: No date provided **#SEEDSIGNER** 
  Convert the test suite rather than handle here?
- Line 733: No date provided **#SEEDSIGNER** 
  Pre-calculate this once on startup
- Line 768: No date provided **#SEEDSIGNER** 
  Refactor this to work with the new SettingsDefinition

### `src/seedsigner/models/encode_qr.py`
- Line 225: 2024-06-10 
  2024-06-10, needs to return view only wallet URI
- Line 30: No date provided 
  Refactor so that this is a base class with implementation classes for each
- Line 91: No date provided 
  Make these properties?

### `src/seedsigner/models/psbt_parser.py`
- Line 194: No date provided 
  Move this to Seed?
- Line 200: No date provided 
  Is this right?

### `src/seedsigner/models/settings.py`
- Line 78: No date provided **#SEEDSIGNER** 
  If value is not in entry.selection_options...

### `src/seedsigner/models/settings_definition.py`
- Line 96: 2024-06-10 
  remove comment before 2024-06-10 handle differences in wordlist languages in monero seed and polyseed, think should be handled in the wordlist implementations instead
- Line 138: 2024-06-10 
  remove after 2024-06-10, maybe there should be SETTING__WORDLIST_LANGUAGE_MONERO and SETTING__WORDLIST_LANGUAGE_POLYSEED? Makes this even sense, should it not be more dynamic letting the responsibility to the monero, polyseed implementation to have it more future proof?
- Line 161: No date provided 
  Not using these for display purposes yet (ever?)
- Line 172: No date provided **#SEEDSIGNER** 
  Is there really a difference between ENABLED and PROMPT?
- Line 200: No date provided **#SEEDSIGNER** 
  Handle multi-language `display_name` and `help_text`
- Line 328: No date provided **#SEEDSIGNER** 
  Full babel multilanguage support! Until then, type == HIDDEN
- Line 337: No date provided **#SEEDSIGNER** 
  Support other bip-39 wordlist languages! Until then, type == HIDDEN
- Line 389: No date provided 
  change to VISIBILITY__ADVANCED after implementing passwords for monero seeds, is hidden because this feature is posponed because of insane password derivation method in monero (CryptoNight, need to transpile to python, very propably other #rabbit-hole, be aware before starting!)
- Line 440: No date provided **#SEEDSIGNER** 
  No real Developer options needed yet. Disable for now.

### `src/seedsigner/views/psbt_views.py`
- Line 494: 2024-06-15 
  2024-06-15 remove coordinator
- Line 45: No date provided **#SEEDSIGNER** 
  Include lock icon on right side of button
- Line 316: No date provided **#SEEDSIGNER** 
  Something is wrong with this psbt(?). Reroute to warning?
- Line 487: No date provided **#SEEDSIGNER** 
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
- Line 741: 2024-06-04 
  expire 2024-06-04: adapt to polyseed, monero seed and view keys - we don't supportMyMonero keys for export. Wait, need to check again, seems that is meant to draw your QR codes on paper, so it would not really make sense for view keys, not? Would it? Think again about before taking decision!
- Line 822: 2024-06-04 
  expire 2024-06-04, not true for view keys, but should stil be a warning that with view keys you can fuck up your privacy
- Line 885: 2024-06-04 
  expire 2024-06-04, can only be 25 (monero seed) or 16 (polyseed)
- Line 991: 2024-06-04 
  expire 2024-06-04, remove BTC related stuff, make it work for monero
- Line 1041: 2024-06-04 
  expire 2024-06-04, remove BTC stuff, make monero work
- Line 481: 2024-06-10 
  2024-06-10: finish implementation
- Line 531: 2024-06-10 
  no warning or different warning for view keys, adapt before 2024-06-10
- Line 535: 2024-06-10 
  see todo above, adapt text to master key and view keys before 2024-06-10
- Line 1222: 2024-06-10 
  expire 2024-06-10, adapt to monero
- Line 1243: 2024-06-10 
  expire 2024-06-10, adapt to monero
- Line 1194: 2024-06-12 
  expire 2024-06-12, check if needed for monero, delete or modify
- Line 1143: 2024-06-15 
  expire 2024-06-15, what is that about??? Remove BTC stuff and make it for monero working. If not needed for monero, remove it
- Line 1171: 2024-06-15 
  2024-06-15, nonsense for us
- Line 1175: 2024-06-15 
  2024-06-15, remove all the cluster fuck here, we can verify easy if a address belongs to a wallet in monero
- Line 155: 2024-06-30 
  2024-06-30, clean up, this code is now functional but uggly as fuck!
- Line 159: 2024-06-30 
  expire 2024-06-30, lean it up
- Line 887: 2024-06-31 
  expire 2024-06-31, from there come this numbers, is this not some data comming from QR code constraints? Would it no be wise to get the number from there instead of this???
- Line 428: No date provided **#SEEDSIGNER** 
  How sure are we? Should disable this entirely if we're 100% sure?
- Line 943: No date provided **#SEEDSIGNER** 
  Does this belong in its own BaseThread?
- Line 1025: No date provided **#SEEDSIGNER** 
  detect single sig vs multisig or have to prompt?
- Line 1098: No date provided **#SEEDSIGNER** 
  Include lock icon on right side of button
- Line 1283: No date provided **#SEEDSIGNER** 
  Route properly when multisig brute-force addr verification is done

### `src/seedsigner/views/settings_views.py`
- Line 81: No date provided **#SEEDSIGNER** 
  Free-entry types (are there any?) will need their own SettingsEntryUpdateFreeEntryView(?).

### `src/seedsigner/views/tools_views.py`
- Line 153: 2024-06-04 
  expire 2024-06-04 should be merged with ToolsImagePolyseedView, same code and be outsid of views...
- Line 206: 2024-06-04 
  expire 2024-06-04 should be merged with ToolsImageEntropyMnemonicLengthView, same code and be outsid of views...
- Line 415: 2024-06-04 
  2024-06-04, rename, because it is missleading, the only thing what will be calculated is the checksum word
- Line 427: 2024-06-04 
  2024-06-04 hot fix, make it right, seems actually right to add checksum
- Line 31: 2024-06-21 
  expire 2024-06-21, I think there should be a warning that this way most probale will lead to low entropy, should only be used if user is really knowing what he is doing... Maybe an alternative would be to use it as input entropy with pseudo entropy to generate a new "now magically random" (of course not, but at least with less probability of user picking the most prefered words out of the list and shootig himself in the foot.
- Line 273: 2024-06-30 
  expire 2024-06-30, offer only 25 words if not low security is set in settings
- Line 194: 2024-07-01 
  expire 2024-07-01, see #todo in seedsigner.helpers.mnemonic_generation, and fix language together...
- Line 242: 2024-07-01 
  expire 2024-07-01, see #todo in seedsigner.helpers.mnemonic_generation, and fix language together...
- Line 184: 2024-07-31 
  expire 2024-07-31, don't know python memory managment, but `del seed_entropy_image` etc seems for me the better way, well, need to investigate, when not mistaken, python uses GC, is there a way to clean up inmedately?
- Line 232: 2024-07-31 
  expire 2024-07-31, don't know python memory managment, but `del seed_entropy_image` etc seems for me the better way, well, need to investigate, when not mistaken, python uses GC, is there a way to clean up inmedately?

### `src/seedsigner/views/view.py`
- Line 54: No date provided 
  Pull all rendering-related code out of Views and into gui.screens implementations
