# Inline Todo

Total: 75

## Index
- [Urgent](#urgent)
- [By File](#by-file)
- [By Tags](#by-tags)
- [External Todo](Todo.md)

## Urgent

### 2024-06-04
- `src/xmrsigner/views/tools_views.py`:182
  expire 2024-06-04 should be merged with ToolsImagePolyseedView, same code and be outsid of views...
- `src/xmrsigner/views/tools_views.py`:235
  expire 2024-06-04 should be merged with ToolsImageEntropyMnemonicLengthView, same code and be outsid of views...
- `src/xmrsigner/views/tools_views.py`:441
  2024-06-04, rename, because it is missleading, the only thing what will be calculated is the checksum word
- `src/xmrsigner/views/tools_views.py`:452
  2024-06-04 hot fix, make it right, seems actually right to add checksum

### 2024-06-10
- `src/xmrsigner/models/settings_definition.py`:102
  remove comment before 2024-06-10 handle differences in wordlist languages in monero seed and polyseed, think should be handled in the wordlist implementations instead
- `src/xmrsigner/models/settings_definition.py`:144
  remove after 2024-06-10, maybe there should be SETTING__WORDLIST_LANGUAGE_MONERO and SETTING__WORDLIST_LANGUAGE_POLYSEED? Makes this even sense, should it not be more dynamic letting the responsibility to the monero, polyseed implementation to have it more future proof?
- `src/xmrsigner/views/wallet_views.py`:222
  2024-06-10: finish implementation

### 2024-06-16
- `src/xmrsigner/models/settings.py`:4
  2024-06-16 remove Any if not needed anymore

### 2024-06-17
- `src/xmrsigner/gui/screens/tools_screens.py`:392
  2024-06-17, added with rebase from main to 0.7.0 of seedsigner, lot of work to do
- `src/xmrsigner/views/tools_views.py`:60
  2024-06-17, activate when it works
- `src/xmrsigner/views/tools_views.py`:62
  2024-06-17, activate when it works
- `src/xmrsigner/views/tools_views.py`:548
  2024-06-17, holy clusterfuck, added with rebase from main to 0.7.0 of seedsigner, lot of work to do

### 2024-06-20
- `src/xmrsigner/gui/screens/monero_screens.py`:656
  2024-06-20, probably should change to purple if polyseed?

### 2024-06-21
- `src/xmrsigner/views/tools_views.py`:56
  expire 2024-06-21, I think there should be a warning that this way most probale will lead to low entropy, should only be used if user is really knowing what he is doing... Maybe an alternative would be to use it as input entropy with pseudo entropy to generate a new "now magically random" (of course not, but at least with less probability of user picking the most prefered words out of the list and shootig himself in the foot.

### 2024-06-26
- `src/xmrsigner/views/seed_views.py`:314
  2024-06-26, solve multi network issue
- `src/xmrsigner/views/tools_views.py`:470
  2024-06-26, solve multi network issue
- `src/xmrsigner/views/tools_views.py`:563
  2024-06-26, solve multi network issue
- `src/xmrsigner/views/tools_views.py`:569
  2024-06-26, solve multi network issue
- `src/xmrsigner/views/view.py`:246
  2024-06-26, solve multi network issue
- `src/xmrsigner/views/view.py`:250
  2024-06-26, solve multi network issue

### 2024-06-27
- `src/xmrsigner/views/settings_views.py`:51
  2024-06-27, don't display until we know what to do about

### 2024-06-30
- `src/xmrsigner/models/settings.py`:16
  2024-06-30 don't know what will uname return on win32, check
- `src/xmrsigner/views/seed_views.py`:156
  2024-06-30, clean up, this code is now functional but uggly as fuck!
- `src/xmrsigner/views/seed_views.py`:160
  expire 2024-06-30, lean it up
- `src/xmrsigner/views/tools_views.py`:302
  expire 2024-06-30, offer only 25 words if not low security is set in settings

### 2024-07-01
- `src/xmrsigner/views/tools_views.py`:223
  expire 2024-07-01, see #todo in xmrsigner.helpers.mnemonic_generation, and fix language together...
- `src/xmrsigner/views/tools_views.py`:271
  expire 2024-07-01, see #todo in xmrsigner.helpers.mnemonic_generation, and fix language together...

### 2024-07-02
- `src/test/xmrsigner/helpers/polyseed_mnemonic_generation.py`:27
  2024-07-02, continue here!
- `src/xmrsigner/helpers/polyseed_mnemonic_generation.py`:7
  2024-07-02, language selection not working issue in polyseed-python

### 2024-07-15
- `src/test/xmrsigner/helpers/monero_time.py`:130
  2024-07-15, WTF is the issue?
- `src/xmrsigner/views/seed_views.py`:816
  expire 2024-07-15, from there come this numbers, is this not some data comming from QR code constraints? Would it no be wise to get the number from there instead of this??? Test if smaller are viable

### 2024-07-21
- `src/xmrsigner/models/ur_encoder.py`:9
  2024-07-21, rename ur_type and ur_payload
- `src/xmrsigner/models/ur_encoder.py`:12
  2024-07-21, probably not a good var name

### 2024-07-23
- `src/xmrsigner/views/scan_views.py`:129
  2024-07-23, implement
- `src/xmrsigner/views/scan_views.py`:133
  2024-07-23, implement
- `src/xmrsigner/views/wallet_views.py`:207
  2024-07-23, create a WalletOptionsScreen!

### 2024-07-24
- `src/xmrsigner/controller.py`:69
  2024-07-24, holy clusterfuck, improve this sh*t - but later
- `src/xmrsigner/models/decode_qr.py`:113
  2024-07-24, remove DEBUG only
- `src/xmrsigner/views/wallet_views.py`:245
  2024-07-24, to remove

### 2024-07-26
- `src/xmrsigner/helpers/monero.py`:1
  2024-07-26, this should be in monero-python

### 2024-07-27
- `src/xmrsigner/views/monero_views.py`:238
  2024-07-27, decide what to do about
- `src/xmrsigner/views/monero_views.py`:268
  2024-07-27, decide to check or remove
- `src/xmrsigner/views/monero_views.py`:390
  2024-07-27, code missing here!
- `src/xmrsigner/views/wallet_views.py`:148
  2024-07-27, thought: redirect to address viewer as soon it exists

### 2024-07-28
- `src/xmrsigner/gui/components.py`:764
  2024-07-28, render only with Monero Logo
- `src/xmrsigner/gui/components.py`:841
  2024-07-28, render only with Monero Logo

### 2024-07-30
- `src/xmrsigner/helpers/qr.py`:45
  2024-07-30, WTF, implement in python?

### 2024-07-31
- `src/xmrsigner/views/tools_views.py`:213
  expire 2024-07-31, don't know python memory managment, but `del seed_entropy_image` etc seems for me the better way, well, need to investigate, when not mistaken, python uses GC, is there a way to clean up inmedately?
- `src/xmrsigner/views/tools_views.py`:261
  expire 2024-07-31, don't know python memory managment, but `del seed_entropy_image` etc seems for me the better way, well, need to investigate, when not mistaken, python uses GC, is there a way to clean up inmedately?

### 2024-08-02
- `src/xmrsigner/controller.py`:166
  2024-08-02, for temporary use until refactoring is finished
- `src/xmrsigner/gui/components.py`:754
  2024-08-02, change to Monero icon

### 2024-12-01
- `src/xmrsigner/models/settings_definition.py`:391
  2024-12-01, change to VISIBILITY__ADVANCED after implementing passwords for monero seeds, is hidden because this feature is posponed because of insane password derivation method in monero (CryptoNight, need to transpile to python, very propably other #rabbit-hole, be aware before starting!)

### No time constraint
- `src/test/xmrsigner/helpers/polyseed_mnemonic_generation.py`:12
  not working yet, some issue in polyseed-python
- `src/xmrsigner/gui/components.py`:191
  don't need BTC, need XMR glyph is still Bitcoin
- `src/xmrsigner/gui/components.py`:192
  don't need BTC, need XMR glyph is still Bitcoin
- `src/xmrsigner/hardware/buttons.py`:66
  **#SEEDSIGNER** Refactor to keep control in the Controller and not here
- `src/xmrsigner/hardware/buttons.py`:179
  **#SEEDSIGNER** Implement `release_lock` functionality as a global somewhere. Mixes up design
- `src/xmrsigner/helpers/monero_time.py`:1
  move this to monero-python, network related part should maybe move to .network?
- `src/xmrsigner/helpers/ur2/cbor_lite.py`:246
  Check that this is the right way -- do we need to use struct.unpack()?
- `src/xmrsigner/helpers/ur2/fountain_decoder.py`:37
  Not efficient
- `src/xmrsigner/helpers/ur2/fountain_decoder.py`:55
  Handle None?
- `src/xmrsigner/helpers/ur2/fountain_decoder.py`:200
  Does this need to make a copy of p?
- `src/xmrsigner/helpers/ur2/fountain_encoder.py`:35
  Do something better with this check
- `src/xmrsigner/models/base_decoder.py`:29
  **#SEEDSIGNER** standardize this approach across all decoders (example: SignMessageQrDecoder)
- `src/xmrsigner/models/settings.py`:246
  **#SEEDSIGNER** Perhaps prompt the user if the current settings (not including persistent
- `src/xmrsigner/models/settings_definition.py`:169
  **#SEEDSIGNER** Not using these for display purposes yet (ever?)
- `src/xmrsigner/models/settings_definition.py`:179
  **#SEEDSIGNER** Is there really a difference between ENABLED and PROMPT?
- `src/xmrsigner/models/settings_definition.py`:207
  **#SEEDSIGNER** Handle multi-language `display_name` and `help_text`
- `src/xmrsigner/models/settings_definition.py`:326
  **#SEEDSIGNER** Full babel multilanguage support! Until then, type == HIDDEN
- `src/xmrsigner/models/settings_definition.py`:336
  **#SEEDSIGNER** Support wordlist languages! Until then, type == HIDDEN
- `src/xmrsigner/views/screensaver.py`:12
  This early code is now outdated vis-a-vis Screen vs View distinctions
- `src/xmrsigner/views/settings_views.py`:90
  **#SEEDSIGNER** Free-entry types (are there any?) will need their own SettingsEntryUpdateFreeEntryView(?).
- `src/xmrsigner/views/tools_views.py`:598
  Refactor to a cleaner `BackStack.get_previous_View_cls()`
- `src/xmrsigner/views/tools_views.py`:652
  Custom derivation path
- `src/xmrsigner/views/view.py`:67
  **#SEEDSIGNER** Pull all rendering-related code out of Views and into gui.screens implementations

## By File

### `src/test/xmrsigner/helpers/monero_time.py`
- Line 130: 2024-07-15 
  2024-07-15, WTF is the issue?

### `src/test/xmrsigner/helpers/polyseed_mnemonic_generation.py`
- Line 12: None 
  not working yet, some issue in polyseed-python
- Line 27: 2024-07-02 
  2024-07-02, continue here!

### `src/xmrsigner/controller.py`
- Line 69: 2024-07-24 
  2024-07-24, holy clusterfuck, improve this sh*t - but later
- Line 166: 2024-08-02 
  2024-08-02, for temporary use until refactoring is finished

### `src/xmrsigner/gui/components.py`
- Line 191: None 
  don't need BTC, need XMR glyph is still Bitcoin
- Line 192: None 
  don't need BTC, need XMR glyph is still Bitcoin
- Line 754: 2024-08-02 
  2024-08-02, change to Monero icon
- Line 764: 2024-07-28 
  2024-07-28, render only with Monero Logo
- Line 841: 2024-07-28 
  2024-07-28, render only with Monero Logo

### `src/xmrsigner/gui/screens/monero_screens.py`
- Line 656: 2024-06-20 
  2024-06-20, probably should change to purple if polyseed?

### `src/xmrsigner/gui/screens/tools_screens.py`
- Line 392: 2024-06-17 
  2024-06-17, added with rebase from main to 0.7.0 of seedsigner, lot of work to do

### `src/xmrsigner/hardware/buttons.py`
- Line 66: None **#SEEDSIGNER** 
  Refactor to keep control in the Controller and not here
- Line 179: None **#SEEDSIGNER** 
  Implement `release_lock` functionality as a global somewhere. Mixes up design

### `src/xmrsigner/helpers/monero.py`
- Line 1: 2024-07-26 
  2024-07-26, this should be in monero-python

### `src/xmrsigner/helpers/monero_time.py`
- Line 1: None 
  move this to monero-python, network related part should maybe move to .network?

### `src/xmrsigner/helpers/polyseed_mnemonic_generation.py`
- Line 7: 2024-07-02 
  2024-07-02, language selection not working issue in polyseed-python

### `src/xmrsigner/helpers/qr.py`
- Line 45: 2024-07-30 
  2024-07-30, WTF, implement in python?

### `src/xmrsigner/helpers/ur2/cbor_lite.py`
- Line 246: None 
  Check that this is the right way -- do we need to use struct.unpack()?

### `src/xmrsigner/helpers/ur2/fountain_decoder.py`
- Line 37: None 
  Not efficient
- Line 55: None 
  Handle None?
- Line 200: None 
  Does this need to make a copy of p?

### `src/xmrsigner/helpers/ur2/fountain_encoder.py`
- Line 35: None 
  Do something better with this check

### `src/xmrsigner/models/base_decoder.py`
- Line 29: None **#SEEDSIGNER** 
  standardize this approach across all decoders (example: SignMessageQrDecoder)

### `src/xmrsigner/models/decode_qr.py`
- Line 113: 2024-07-24 
  2024-07-24, remove DEBUG only

### `src/xmrsigner/models/settings.py`
- Line 4: 2024-06-16 
  2024-06-16 remove Any if not needed anymore
- Line 16: 2024-06-30 
  2024-06-30 don't know what will uname return on win32, check
- Line 246: None **#SEEDSIGNER** 
  Perhaps prompt the user if the current settings (not including persistent

### `src/xmrsigner/models/settings_definition.py`
- Line 102: 2024-06-10 
  remove comment before 2024-06-10 handle differences in wordlist languages in monero seed and polyseed, think should be handled in the wordlist implementations instead
- Line 144: 2024-06-10 
  remove after 2024-06-10, maybe there should be SETTING__WORDLIST_LANGUAGE_MONERO and SETTING__WORDLIST_LANGUAGE_POLYSEED? Makes this even sense, should it not be more dynamic letting the responsibility to the monero, polyseed implementation to have it more future proof?
- Line 169: None **#SEEDSIGNER** 
  Not using these for display purposes yet (ever?)
- Line 179: None **#SEEDSIGNER** 
  Is there really a difference between ENABLED and PROMPT?
- Line 207: None **#SEEDSIGNER** 
  Handle multi-language `display_name` and `help_text`
- Line 326: None **#SEEDSIGNER** 
  Full babel multilanguage support! Until then, type == HIDDEN
- Line 336: None **#SEEDSIGNER** 
  Support wordlist languages! Until then, type == HIDDEN
- Line 391: 2024-12-01 
  2024-12-01, change to VISIBILITY__ADVANCED after implementing passwords for monero seeds, is hidden because this feature is posponed because of insane password derivation method in monero (CryptoNight, need to transpile to python, very propably other #rabbit-hole, be aware before starting!)

### `src/xmrsigner/models/ur_encoder.py`
- Line 9: 2024-07-21 
  2024-07-21, rename ur_type and ur_payload
- Line 12: 2024-07-21 
  2024-07-21, probably not a good var name

### `src/xmrsigner/views/monero_views.py`
- Line 238: 2024-07-27 
  2024-07-27, decide what to do about
- Line 268: 2024-07-27 
  2024-07-27, decide to check or remove
- Line 390: 2024-07-27 
  2024-07-27, code missing here!

### `src/xmrsigner/views/scan_views.py`
- Line 129: 2024-07-23 
  2024-07-23, implement
- Line 133: 2024-07-23 
  2024-07-23, implement

### `src/xmrsigner/views/screensaver.py`
- Line 12: None 
  This early code is now outdated vis-a-vis Screen vs View distinctions

### `src/xmrsigner/views/seed_views.py`
- Line 156: 2024-06-30 
  2024-06-30, clean up, this code is now functional but uggly as fuck!
- Line 160: 2024-06-30 
  expire 2024-06-30, lean it up
- Line 314: 2024-06-26 
  2024-06-26, solve multi network issue
- Line 816: 2024-07-15 
  expire 2024-07-15, from there come this numbers, is this not some data comming from QR code constraints? Would it no be wise to get the number from there instead of this??? Test if smaller are viable

### `src/xmrsigner/views/settings_views.py`
- Line 51: 2024-06-27 
  2024-06-27, don't display until we know what to do about
- Line 90: None **#SEEDSIGNER** 
  Free-entry types (are there any?) will need their own SettingsEntryUpdateFreeEntryView(?).

### `src/xmrsigner/views/tools_views.py`
- Line 56: 2024-06-21 
  expire 2024-06-21, I think there should be a warning that this way most probale will lead to low entropy, should only be used if user is really knowing what he is doing... Maybe an alternative would be to use it as input entropy with pseudo entropy to generate a new "now magically random" (of course not, but at least with less probability of user picking the most prefered words out of the list and shootig himself in the foot.
- Line 60: 2024-06-17 
  2024-06-17, activate when it works
- Line 62: 2024-06-17 
  2024-06-17, activate when it works
- Line 182: 2024-06-04 
  expire 2024-06-04 should be merged with ToolsImagePolyseedView, same code and be outsid of views...
- Line 213: 2024-07-31 
  expire 2024-07-31, don't know python memory managment, but `del seed_entropy_image` etc seems for me the better way, well, need to investigate, when not mistaken, python uses GC, is there a way to clean up inmedately?
- Line 223: 2024-07-01 
  expire 2024-07-01, see #todo in xmrsigner.helpers.mnemonic_generation, and fix language together...
- Line 235: 2024-06-04 
  expire 2024-06-04 should be merged with ToolsImageEntropyMnemonicLengthView, same code and be outsid of views...
- Line 261: 2024-07-31 
  expire 2024-07-31, don't know python memory managment, but `del seed_entropy_image` etc seems for me the better way, well, need to investigate, when not mistaken, python uses GC, is there a way to clean up inmedately?
- Line 271: 2024-07-01 
  expire 2024-07-01, see #todo in xmrsigner.helpers.mnemonic_generation, and fix language together...
- Line 302: 2024-06-30 
  expire 2024-06-30, offer only 25 words if not low security is set in settings
- Line 441: 2024-06-04 
  2024-06-04, rename, because it is missleading, the only thing what will be calculated is the checksum word
- Line 452: 2024-06-04 
  2024-06-04 hot fix, make it right, seems actually right to add checksum
- Line 470: 2024-06-26 
  2024-06-26, solve multi network issue
- Line 548: 2024-06-17 
  2024-06-17, holy clusterfuck, added with rebase from main to 0.7.0 of seedsigner, lot of work to do
- Line 563: 2024-06-26 
  2024-06-26, solve multi network issue
- Line 569: 2024-06-26 
  2024-06-26, solve multi network issue
- Line 598: None 
  Refactor to a cleaner `BackStack.get_previous_View_cls()`
- Line 652: None 
  Custom derivation path

### `src/xmrsigner/views/view.py`
- Line 67: None **#SEEDSIGNER** 
  Pull all rendering-related code out of Views and into gui.screens implementations
- Line 246: 2024-06-26 
  2024-06-26, solve multi network issue
- Line 250: 2024-06-26 
  2024-06-26, solve multi network issue

### `src/xmrsigner/views/wallet_views.py`
- Line 148: 2024-07-27 
  2024-07-27, thought: redirect to address viewer as soon it exists
- Line 207: 2024-07-23 
  2024-07-23, create a WalletOptionsScreen!
- Line 222: 2024-06-10 
  2024-06-10: finish implementation
- Line 245: 2024-07-24 
  2024-07-24, to remove

## By Tags

### **#SEEDSIGNER**
- `src/xmrsigner/views/view.py`:67
  Pull all rendering-related code out of Views and into gui.screens implementations
- `src/xmrsigner/views/settings_views.py`:90
  Free-entry types (are there any?) will need their own SettingsEntryUpdateFreeEntryView(?).
- `src/xmrsigner/hardware/buttons.py`:66
  Refactor to keep control in the Controller and not here
- `src/xmrsigner/hardware/buttons.py`:179
  Implement `release_lock` functionality as a global somewhere. Mixes up design
- `src/xmrsigner/models/base_decoder.py`:29
  standardize this approach across all decoders (example: SignMessageQrDecoder)
- `src/xmrsigner/models/settings.py`:246
  Perhaps prompt the user if the current settings (not including persistent
- `src/xmrsigner/models/settings_definition.py`:169
  Not using these for display purposes yet (ever?)
- `src/xmrsigner/models/settings_definition.py`:179
  Is there really a difference between ENABLED and PROMPT?
- `src/xmrsigner/models/settings_definition.py`:207
  Handle multi-language `display_name` and `help_text`
- `src/xmrsigner/models/settings_definition.py`:326
  Full babel multilanguage support! Until then, type == HIDDEN
- `src/xmrsigner/models/settings_definition.py`:336
  Support wordlist languages! Until then, type == HIDDEN
