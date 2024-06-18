# Inline Todo

Total: 162

## Index
- [Urgent](#urgent)
- [By File](#by-file)
- [By Tags](#by-tags)
- [External Todo](Todo.md)

## Urgent

### 2024-06-04
- `src/xmrsigner/views/seed_views.py`:861
  expire 2024-06-04: adapt to polyseed, monero seed and view keys - we don't supportMyMonero keys for export. Wait, need to check again, seems that is meant to draw your QR codes on paper, so it would not really make sense for view keys, not? Would it? Think again about before taking decision!
- `src/xmrsigner/views/seed_views.py`:1006
  expire 2024-06-04, can only be 25 (monero seed) or 16 (polyseed)
- `src/xmrsigner/views/seed_views.py`:1112
  expire 2024-06-04, remove BTC related stuff, make it work for monero
- `src/xmrsigner/views/seed_views.py`:1162
  expire 2024-06-04, remove BTC stuff, make monero work
- `src/xmrsigner/views/tools_views.py`:182
  expire 2024-06-04 should be merged with ToolsImagePolyseedView, same code and be outsid of views...
- `src/xmrsigner/views/tools_views.py`:235
  expire 2024-06-04 should be merged with ToolsImageEntropyMnemonicLengthView, same code and be outsid of views...
- `src/xmrsigner/views/tools_views.py`:441
  2024-06-04, rename, because it is missleading, the only thing what will be calculated is the checksum word
- `src/xmrsigner/views/tools_views.py`:452
  2024-06-04 hot fix, make it right, seems actually right to add checksum

### 2024-06-10
- `src/xmrsigner/gui/screens/seed_screens.py`:568
  2024-06-10, remove: Xpub related
- `src/xmrsigner/helpers/polyseed_mnemonic_generation.py`:6
  expire 2024-06-10, I think should be moved/merged with mnemonic_generation somehow and somewhere else, think about it.
- `src/xmrsigner/models/decode_qr.py`:707
  2024-06-10, fix to monero (and polyseed?)
- `src/xmrsigner/models/encode_qr.py`:222
  2024-06-10, needs to return view only wallet URI
- `src/xmrsigner/models/settings_definition.py`:102
  remove comment before 2024-06-10 handle differences in wordlist languages in monero seed and polyseed, think should be handled in the wordlist implementations instead
- `src/xmrsigner/models/settings_definition.py`:144
  remove after 2024-06-10, maybe there should be SETTING__WORDLIST_LANGUAGE_MONERO and SETTING__WORDLIST_LANGUAGE_POLYSEED? Makes this even sense, should it not be more dynamic letting the responsibility to the monero, polyseed implementation to have it more future proof?
- `src/xmrsigner/views/seed_views.py`:598
  2024-06-10: finish implementation
- `src/xmrsigner/views/seed_views.py`:648
  no warning or different warning for view keys, adapt before 2024-06-10
- `src/xmrsigner/views/seed_views.py`:652
  see todo above, adapt text to master key and view keys before 2024-06-10
- `src/xmrsigner/views/seed_views.py`:1343
  expire 2024-06-10, adapt to monero
- `src/xmrsigner/views/seed_views.py`:1364
  expire 2024-06-10, adapt to monero

### 2024-06-12
- `src/xmrsigner/views/seed_views.py`:1315
  expire 2024-06-12, check if needed for monero, delete or modify

### 2024-06-14
- `src/xmrsigner/models/decode_qr.py`:142
  2024-06-14, needs to be adapted for monero
- `src/xmrsigner/models/decode_qr.py`:143
  2024-06-14, needs to be adapted for monero
- `src/xmrsigner/models/decode_qr.py`:401
  2024-06-14, adapt to monero
- `src/xmrsigner/models/decode_qr.py`:410
  2024-06-14, adapt to monero
- `src/xmrsigner/models/decode_qr.py`:719
  2024-06-14, modify to work with monero seed and polyseed
- `src/xmrsigner/models/decode_qr.py`:742
  2024-06-14, adapt for monero seed AND polyseed
- `src/xmrsigner/models/decode_qr.py`:938
  2024-06-14, validate
- `src/xmrsigner/models/encode_qr.py`:15
  2024-06-14, used as quickfix to remove embit.psbt.PSBT! Adapt for monero
- `src/xmrsigner/models/psbt_parser.py`:9
  2024-06-14, quick fix to remove embit.descriptor.Descriptor
- `src/xmrsigner/models/psbt_parser.py`:13
  2024-06-14, quick fix to remove embit.psbt.PSBT
- `src/xmrsigner/models/psbt_parser.py`:64
  2024-06-14 removed to remove embit.bip39, expect to be deleted all and write from ground up for monero
- `src/xmrsigner/models/psbt_parser.py`:124
  2024-06-14, removed whole block to remove embit.script
- `src/xmrsigner/models/psbt_parser.py`:132
  2024-06-14, removed whole block to remove embit.script
- `src/xmrsigner/models/psbt_parser.py`:149
  2024-06-14 removed to remove embit.networks.NETWORKS
- `src/xmrsigner/models/psbt_parser.py`:157
  2024-06-14 removed to remove embit.bip39, expect to be deleted all and write from ground up for monero
- `src/xmrsigner/models/psbt_parser.py`:167
  2024-06-14 removed to remove embit.networks.NETWORKS
- `src/xmrsigner/models/psbt_parser.py`:178
  2024-06-14, removed to remove embit.psbt.psbt
- `src/xmrsigner/models/psbt_parser.py`:282
  2024-06-14, removed to remove embit.ec, probably needs to be removed and written from ground up for monero
- `src/xmrsigner/views/psbt_views.py`:28
  2024-06-14, quick fix to remove embit.psbt.PSBT
- `src/xmrsigner/views/psbt_views.py`:375
  2024-06-14, removed to get rid of embit.script
- `src/xmrsigner/views/psbt_views.py`:390
  2024-06-14, removed to get rid of embit.script
- `src/xmrsigner/views/psbt_views.py`:393
  2024-06-14, removed to get rid of embit.script
- `src/xmrsigner/views/psbt_views.py`:399
  2024-06-14, removed to get rid of embit.network.NETWORKS
- `src/xmrsigner/views/scan_views.py`:114
  2024-06-14, removed to get rid of embit.descriptor.Descriptor
- `src/xmrsigner/views/scan_views.py`:115
  2024-06-14, removed to get rid of embit.descriptor.Descriptor

### 2024-06-15
- `src/xmrsigner/controller.py`:63
  2024-06-15 removed with empit.psbt.psbt
- `src/xmrsigner/controller.py`:303
  2024-06-15, don't like speed over ugly code, there must be a better solution
- `src/xmrsigner/gui/screens/seed_screens.py`:11
  2024-06-15, remove?
- `src/xmrsigner/gui/screens/seed_screens.py`:1354
  2024-06-15, check if used, if not remove, added with rebase from main to 0.7.0 of seedsigner
- `src/xmrsigner/gui/screens/seed_screens.py`:1395
  2024-06-15, check if used, if not remove, added with rebase from main to 0.7.0 of seedsigner
- `src/xmrsigner/gui/screens/settings_screens.py`:302
  2024-06-15, not sure if we need it, added from rebase from main to 0.7.0 from SeedSigner
- `src/xmrsigner/models/decode_qr.py`:335
  2024-06-15, handle Polyseed different from here? 52 decimals (13 words, 100 decimals (25 words), 16 polyseed words would be 64 decimals
- `src/xmrsigner/views/seed_views.py`:1264
  expire 2024-06-15, what is that about??? Remove BTC stuff and make it for monero working. If not needed for monero, remove it
- `src/xmrsigner/views/seed_views.py`:1292
  2024-06-15, nonsense for us
- `src/xmrsigner/views/seed_views.py`:1296
  2024-06-15, remove all the cluster fuck here, we can verify easy if a address belongs to a wallet in monero

### 2024-06-16
- `src/xmrsigner/gui/components.py`:1446
  2024-06-16, seems like not needed, check and remove
- `src/xmrsigner/hardware/microsd.py`:11
  2024-06-16, move to SettingsConstants
- `src/xmrsigner/hardware/microsd.py`:12
  2024-06-16, move to SettingsConstants
- `src/xmrsigner/models/settings.py`:4
  2024-06-16 remove Any if not needed anymore
- `src/xmrsigner/views/psbt_views.py`:44
  2024-06-16, added from rebase main to 0.7.0, check if we really need it
- `src/xmrsigner/views/seed_views.py`:97
  2024-06-16, added with rebase from main to 0.7.0 of seedsigner, check if we need it
- `src/xmrsigner/views/seed_views.py`:1525
  2024-06-16
- `src/xmrsigner/views/seed_views.py`:1557
  2024-06-16
- `src/xmrsigner/views/view.py`:260
  2024-06-16, why all this drama and not simply `from sys import exit` and `exit(0)`???
- `src/xmrsigner/views/view.py`:278
  2024-06-16, IMO should be removed

### 2024-06-17
- `src/xmrsigner/controller.py`:113
  2024-06-17 @see up import statement
- `src/xmrsigner/gui/screens/tools_screens.py`:392
  2024-06-17, added with rebase from main to 0.7.0 of seedsigner, lot of work to do
- `src/xmrsigner/views/settings_views.py`:49
  2024-06-17, display until we know what to do about
- `src/xmrsigner/views/tools_views.py`:60
  2024-06-17, activate when it works
- `src/xmrsigner/views/tools_views.py`:62
  2024-06-17, activate when it works
- `src/xmrsigner/views/tools_views.py`:548
  2024-06-17, holy clusterfuck, added with rebase from main to 0.7.0 of seedsigner, lot of work to do

### 2024-06-20
- `src/xmrsigner/controller.py`:8
  2024-06-20, don't like faster code paying with ugly code, search better solution
- `src/xmrsigner/controller.py`:9
  2024-06-20, don't like faster code paying with ugly code, search better solution
- `src/xmrsigner/controller.py`:143
  2024-06-20, don't like faster code on the expense of ugly code, search a better solution
- `src/xmrsigner/controller.py`:304
  2024-06-20, maybe this should not be imported here, check
- `src/xmrsigner/gui/components.py`:36
  2024-06-20, rename constant
- `src/xmrsigner/gui/components.py`:116
  2024-06-20, at the moment only an anotation from refactoring, see how to resolve the clusterfuck :D
- `src/xmrsigner/gui/screens/psbt_screens.py`:670
  2024-06-20, probably should change to purple if polyseed?
- `src/xmrsigner/gui/screens/scan_screens.py`:118
  2024-06-20, replace with constant!
- `src/xmrsigner/gui/screens/screen.py`:150
  2024-06-20, WTF hardcoded, move to constant!
- `src/xmrsigner/gui/screens/screen.py`:151
  2024-06-20, WTF hardcoded, move to constant!
- `src/xmrsigner/gui/screens/screen.py`:760
  2024-06-20, WTF, anyway on import of SettingsConstants the whole file will be parsed, for what to make this pointless acrobatic?
- `src/xmrsigner/gui/screens/screen.py`:784
  2024-06-20, WTF, anyway on import of SettingsConstants the whole file will be parsed, for what to make this pointless acrobatic?
- `src/xmrsigner/gui/screens/screen.py`:801
  2024-06-20, WTF, anyway on import of SettingsConstants the whole file will be parsed, for what to make this pointless acrobatic?
- `src/xmrsigner/gui/screens/screen.py`:960
  2024-06-20, WTF hardcoded, substitute with constant
- `src/xmrsigner/gui/screens/screen.py`:993
  2024-06-20, remove
- `src/xmrsigner/gui/screens/seed_screens.py`:983
  2024-06-20, what is there going on? Why would you modify a password, and loose accenss? Double check. From rebasing from main to 0.7.0 of seedsigner
- `src/xmrsigner/models/encode_qr.py`:64
  2024-06-20, do we need that? For what purpose? Added with rebase from main to 0.7.0 from seedsigner
- `src/xmrsigner/models/encode_qr.py`:238
  2024-06-20, I don't know yet, but I belief it will not be the case for Monero!
- `src/xmrsigner/views/scan_views.py`:80
  2024-06-20, what about polyseeds?
- `src/xmrsigner/views/seed_views.py`:1429
  2024-06-20

### 2024-06-21
- `src/xmrsigner/views/tools_views.py`:56
  expire 2024-06-21, I think there should be a warning that this way most probale will lead to low entropy, should only be used if user is really knowing what he is doing... Maybe an alternative would be to use it as input entropy with pseudo entropy to generate a new "now magically random" (of course not, but at least with less probability of user picking the most prefered words out of the list and shootig himself in the foot.

### 2024-06-30
- `src/xmrsigner/helpers/qr.py`:45
  2024-06-30, WTF, why not in python?
- `src/xmrsigner/models/settings.py`:16
  2024-06-30 don't know what will uname return on win32, check
- `src/xmrsigner/views/seed_views.py`:256
  2024-06-30, clean up, this code is now functional but uggly as fuck!
- `src/xmrsigner/views/seed_views.py`:260
  expire 2024-06-30, lean it up
- `src/xmrsigner/views/seed_views.py`:1008
  expire 2024-06-30, from there come this numbers, is this not some data comming from QR code constraints? Would it no be wise to get the number from there instead of this???
- `src/xmrsigner/views/tools_views.py`:302
  expire 2024-06-30, offer only 25 words if not low security is set in settings

### 2024-07-01
- `src/xmrsigner/gui/screens/screen.py`:140
  expire 2024-07-01, why hardcoded???? Use constant!
- `src/xmrsigner/helpers/mnemonic_generation.py`:1
  expire 2024-07-01 what to do about this file? Do we do the same thing?
- `src/xmrsigner/views/tools_views.py`:223
  expire 2024-07-01, see #todo in xmrsigner.helpers.mnemonic_generation, and fix language together...
- `src/xmrsigner/views/tools_views.py`:271
  expire 2024-07-01, see #todo in xmrsigner.helpers.mnemonic_generation, and fix language together...

### 2024-07-31
- `src/xmrsigner/helpers/mnemonic_generation.py`:12
  expire 2024-07-31, handle seed languages...
- `src/xmrsigner/helpers/polyseed_mnemonic_generation.py`:9
  expire 2024-07-31, handle seed languages...
- `src/xmrsigner/views/tools_views.py`:213
  expire 2024-07-31, don't know python memory managment, but `del seed_entropy_image` etc seems for me the better way, well, need to investigate, when not mistaken, python uses GC, is there a way to clean up inmedately?
- `src/xmrsigner/views/tools_views.py`:261
  expire 2024-07-31, don't know python memory managment, but `del seed_entropy_image` etc seems for me the better way, well, need to investigate, when not mistaken, python uses GC, is there a way to clean up inmedately?

### No time constraint
- `src/xmrsigner/controller.py`:61
  **#SEEDSIGNER** Refactor these flow-related attrs that survive across multiple Screens.
- `src/xmrsigner/controller.py`:62
  **#SEEDSIGNER** Should all in-memory flow-related attrs get wiped on MainMenuView?
- `src/xmrsigner/controller.py`:75
  **#SEEDSIGNER** end refactor section
- `src/xmrsigner/controller.py`:131
  **#SEEDSIGNER** Rename "storage" to something more indicative of its temp, in-memory state
- `src/xmrsigner/gui/components.py`:20
  **#SEEDSIGNER** Remove all pixel hard coding
- `src/xmrsigner/gui/components.py`:178
  don't need BTC, need XMR glyph is still Bitcoin
- `src/xmrsigner/gui/components.py`:179
  don't need BTC, need XMR glyph is still Bitcoin
- `src/xmrsigner/gui/components.py`:316
  **#SEEDSIGNER** Implement autosize width?
- `src/xmrsigner/gui/components.py`:824
  change to Monero icon
- `src/xmrsigner/gui/components.py`:1011
  **#SEEDSIGNER** Rename the xmrsigner.helpers.Buttons class (to Inputs?) to reduce confusion
- `src/xmrsigner/gui/components.py`:1075
  **#SEEDSIGNER** Only apply screen_y at render
- `src/xmrsigner/gui/screens/psbt_screens.py`:134
  **#SEEDSIGNER** Properly handle the ellipsis truncation in different languages
- `src/xmrsigner/gui/screens/psbt_screens.py`:508
  **#SEEDSIGNER** Test rendering the numeric amounts without the supersampling
- `src/xmrsigner/gui/screens/scan_screens.py`:46
  **#SEEDSIGNER** alternate optimization for Pi Zero 2W?
- `src/xmrsigner/gui/screens/scan_screens.py`:109
  **#SEEDSIGNER** Replace the instructions_text with a disappearing
- `src/xmrsigner/gui/screens/screen.py`:88
  **#SEEDSIGNER** Check self.scroll_y and only render visible elements
- `src/xmrsigner/gui/screens/screen.py`:308
  **#SEEDSIGNER** Define an actual class for button_data?
- `src/xmrsigner/gui/screens/screen.py`:688
  **#SEEDSIGNER** Refactor ToastOverlay to support two lines of icon + text and use
- `src/xmrsigner/gui/screens/seed_screens.py`:61
  **#SEEDSIGNER** support other BIP39 languages/charsets
- `src/xmrsigner/hardware/buttons.py`:65
  **#SEEDSIGNER** Refactor to keep control in the Controller and not here
- `src/xmrsigner/hardware/buttons.py`:178
  **#SEEDSIGNER** Implement `release_lock` functionality as a global somewhere. Mixes up design
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
- `src/xmrsigner/models/decode_qr.py`:114
  **#SEEDSIGNER** Convert the test suite rather than handle here?
- `src/xmrsigner/models/decode_qr.py`:134
  **#SEEDSIGNER** Refactor all of these specific `get_` to just something generic like
- `src/xmrsigner/models/decode_qr.py`:189
  **#SEEDSIGNER** Implement this approach across all decoders, COMMENT: probably unnecesary with a refactoring
- `src/xmrsigner/models/decode_qr.py`:308
  **#SEEDSIGNER** Convert the test suite rather than handle here?
- `src/xmrsigner/models/decode_qr.py`:574
  **#SEEDSIGNER** standardize this approach across all decoders (example: SignMessageQrDecoder)
- `src/xmrsigner/models/decode_qr.py`:738
  **#SEEDSIGNER** Pre-calculate this once on startup
- `src/xmrsigner/models/decode_qr.py`:817
  **#SEEDSIGNER** support formats other than ascii?
- `src/xmrsigner/models/encode_qr.py`:27
  Refactor so that this is a base class with implementation classes for each
- `src/xmrsigner/models/encode_qr.py`:93
  Make these properties?
- `src/xmrsigner/models/psbt_parser.py`:198
  Move this to Seed?
- `src/xmrsigner/models/psbt_parser.py`:204
  Is this right?
- `src/xmrsigner/models/settings.py`:243
  **#SEEDSIGNER** Perhaps prompt the user if the current settings (not including persistent
- `src/xmrsigner/models/settings_definition.py`:169
  Not using these for display purposes yet (ever?)
- `src/xmrsigner/models/settings_definition.py`:179
  **#SEEDSIGNER** Is there really a difference between ENABLED and PROMPT?
- `src/xmrsigner/models/settings_definition.py`:207
  **#SEEDSIGNER** Handle multi-language `display_name` and `help_text`
- `src/xmrsigner/models/settings_definition.py`:326
  **#SEEDSIGNER** Full babel multilanguage support! Until then, type == HIDDEN
- `src/xmrsigner/models/settings_definition.py`:336
  **#SEEDSIGNER** Support other bip-39 wordlist languages! Until then, type == HIDDEN
- `src/xmrsigner/models/settings_definition.py`:391
  change to VISIBILITY__ADVANCED after implementing passwords for monero seeds, is hidden because this feature is posponed because of insane password derivation method in monero (CryptoNight, need to transpile to python, very propably other #rabbit-hole, be aware before starting!)
- `src/xmrsigner/views/psbt_views.py`:334
  **#SEEDSIGNER** Something is wrong with this psbt(?). Reroute to warning?
- `src/xmrsigner/views/scan_views.py`:118
  Handle single-sig descriptors?
- `src/xmrsigner/views/screensaver.py`:12
  This early code is now outdated vis-a-vis Screen vs View distinctions
- `src/xmrsigner/views/seed_views.py`:136
  **#SEEDSIGNER** Include lock icon on right side of button
- `src/xmrsigner/views/seed_views.py`:1064
  **#SEEDSIGNER** Does this belong in its own BaseThread?
- `src/xmrsigner/views/seed_views.py`:1146
  **#SEEDSIGNER** detect single sig vs multisig or have to prompt?
- `src/xmrsigner/views/seed_views.py`:1219
  **#SEEDSIGNER** Include lock icon on right side of button
- `src/xmrsigner/views/seed_views.py`:1404
  **#SEEDSIGNER** Route properly when multisig brute-force addr verification is done
- `src/xmrsigner/views/settings_views.py`:84
  **#SEEDSIGNER** Free-entry types (are there any?) will need their own SettingsEntryUpdateFreeEntryView(?).
- `src/xmrsigner/views/tools_views.py`:598
  Refactor to a cleaner `BackStack.get_previous_View_cls()`
- `src/xmrsigner/views/tools_views.py`:652
  Custom derivation path
- `src/xmrsigner/views/view.py`:69
  **#SEEDSIGNER** Pull all rendering-related code out of Views and into gui.screens implementations

## By File

### `src/xmrsigner/controller.py`
- Line 8: 2024-06-20 
  2024-06-20, don't like faster code paying with ugly code, search better solution
- Line 9: 2024-06-20 
  2024-06-20, don't like faster code paying with ugly code, search better solution
- Line 61: None **#SEEDSIGNER** 
  Refactor these flow-related attrs that survive across multiple Screens.
- Line 62: None **#SEEDSIGNER** 
  Should all in-memory flow-related attrs get wiped on MainMenuView?
- Line 63: 2024-06-15 
  2024-06-15 removed with empit.psbt.psbt
- Line 75: None **#SEEDSIGNER** 
  end refactor section
- Line 113: 2024-06-17 
  2024-06-17 @see up import statement
- Line 131: None **#SEEDSIGNER** 
  Rename "storage" to something more indicative of its temp, in-memory state
- Line 143: 2024-06-20 
  2024-06-20, don't like faster code on the expense of ugly code, search a better solution
- Line 303: 2024-06-15 
  2024-06-15, don't like speed over ugly code, there must be a better solution
- Line 304: 2024-06-20 
  2024-06-20, maybe this should not be imported here, check

### `src/xmrsigner/gui/components.py`
- Line 20: None **#SEEDSIGNER** 
  Remove all pixel hard coding
- Line 36: 2024-06-20 
  2024-06-20, rename constant
- Line 116: 2024-06-20 
  2024-06-20, at the moment only an anotation from refactoring, see how to resolve the clusterfuck :D
- Line 178: None 
  don't need BTC, need XMR glyph is still Bitcoin
- Line 179: None 
  don't need BTC, need XMR glyph is still Bitcoin
- Line 316: None **#SEEDSIGNER** 
  Implement autosize width?
- Line 824: None 
  change to Monero icon
- Line 1011: None **#SEEDSIGNER** 
  Rename the xmrsigner.helpers.Buttons class (to Inputs?) to reduce confusion
- Line 1075: None **#SEEDSIGNER** 
  Only apply screen_y at render
- Line 1446: 2024-06-16 
  2024-06-16, seems like not needed, check and remove

### `src/xmrsigner/gui/screens/psbt_screens.py`
- Line 134: None **#SEEDSIGNER** 
  Properly handle the ellipsis truncation in different languages
- Line 508: None **#SEEDSIGNER** 
  Test rendering the numeric amounts without the supersampling
- Line 670: 2024-06-20 
  2024-06-20, probably should change to purple if polyseed?

### `src/xmrsigner/gui/screens/scan_screens.py`
- Line 46: None **#SEEDSIGNER** 
  alternate optimization for Pi Zero 2W?
- Line 109: None **#SEEDSIGNER** 
  Replace the instructions_text with a disappearing
- Line 118: 2024-06-20 
  2024-06-20, replace with constant!

### `src/xmrsigner/gui/screens/screen.py`
- Line 88: None **#SEEDSIGNER** 
  Check self.scroll_y and only render visible elements
- Line 140: 2024-07-01 
  expire 2024-07-01, why hardcoded???? Use constant!
- Line 150: 2024-06-20 
  2024-06-20, WTF hardcoded, move to constant!
- Line 151: 2024-06-20 
  2024-06-20, WTF hardcoded, move to constant!
- Line 308: None **#SEEDSIGNER** 
  Define an actual class for button_data?
- Line 688: None **#SEEDSIGNER** 
  Refactor ToastOverlay to support two lines of icon + text and use
- Line 760: 2024-06-20 
  2024-06-20, WTF, anyway on import of SettingsConstants the whole file will be parsed, for what to make this pointless acrobatic?
- Line 784: 2024-06-20 
  2024-06-20, WTF, anyway on import of SettingsConstants the whole file will be parsed, for what to make this pointless acrobatic?
- Line 801: 2024-06-20 
  2024-06-20, WTF, anyway on import of SettingsConstants the whole file will be parsed, for what to make this pointless acrobatic?
- Line 960: 2024-06-20 
  2024-06-20, WTF hardcoded, substitute with constant
- Line 993: 2024-06-20 
  2024-06-20, remove

### `src/xmrsigner/gui/screens/seed_screens.py`
- Line 11: 2024-06-15 
  2024-06-15, remove?
- Line 61: None **#SEEDSIGNER** 
  support other BIP39 languages/charsets
- Line 568: 2024-06-10 
  2024-06-10, remove: Xpub related
- Line 983: 2024-06-20 
  2024-06-20, what is there going on? Why would you modify a password, and loose accenss? Double check. From rebasing from main to 0.7.0 of seedsigner
- Line 1354: 2024-06-15 
  2024-06-15, check if used, if not remove, added with rebase from main to 0.7.0 of seedsigner
- Line 1395: 2024-06-15 
  2024-06-15, check if used, if not remove, added with rebase from main to 0.7.0 of seedsigner

### `src/xmrsigner/gui/screens/settings_screens.py`
- Line 302: 2024-06-15 
  2024-06-15, not sure if we need it, added from rebase from main to 0.7.0 from SeedSigner

### `src/xmrsigner/gui/screens/tools_screens.py`
- Line 392: 2024-06-17 
  2024-06-17, added with rebase from main to 0.7.0 of seedsigner, lot of work to do

### `src/xmrsigner/hardware/buttons.py`
- Line 65: None **#SEEDSIGNER** 
  Refactor to keep control in the Controller and not here
- Line 178: None **#SEEDSIGNER** 
  Implement `release_lock` functionality as a global somewhere. Mixes up design

### `src/xmrsigner/hardware/microsd.py`
- Line 11: 2024-06-16 
  2024-06-16, move to SettingsConstants
- Line 12: 2024-06-16 
  2024-06-16, move to SettingsConstants

### `src/xmrsigner/helpers/mnemonic_generation.py`
- Line 1: 2024-07-01 
  expire 2024-07-01 what to do about this file? Do we do the same thing?
- Line 12: 2024-07-31 
  expire 2024-07-31, handle seed languages...

### `src/xmrsigner/helpers/polyseed_mnemonic_generation.py`
- Line 6: 2024-06-10 
  expire 2024-06-10, I think should be moved/merged with mnemonic_generation somehow and somewhere else, think about it.
- Line 9: 2024-07-31 
  expire 2024-07-31, handle seed languages...

### `src/xmrsigner/helpers/qr.py`
- Line 45: 2024-06-30 
  2024-06-30, WTF, why not in python?

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

### `src/xmrsigner/models/decode_qr.py`
- Line 114: None **#SEEDSIGNER** 
  Convert the test suite rather than handle here?
- Line 134: None **#SEEDSIGNER** 
  Refactor all of these specific `get_` to just something generic like
- Line 142: 2024-06-14 
  2024-06-14, needs to be adapted for monero
- Line 143: 2024-06-14 
  2024-06-14, needs to be adapted for monero
- Line 189: None **#SEEDSIGNER** 
  Implement this approach across all decoders, COMMENT: probably unnecesary with a refactoring
- Line 308: None **#SEEDSIGNER** 
  Convert the test suite rather than handle here?
- Line 335: 2024-06-15 
  2024-06-15, handle Polyseed different from here? 52 decimals (13 words, 100 decimals (25 words), 16 polyseed words would be 64 decimals
- Line 401: 2024-06-14 
  2024-06-14, adapt to monero
- Line 410: 2024-06-14 
  2024-06-14, adapt to monero
- Line 574: None **#SEEDSIGNER** 
  standardize this approach across all decoders (example: SignMessageQrDecoder)
- Line 707: 2024-06-10 
  2024-06-10, fix to monero (and polyseed?)
- Line 719: 2024-06-14 
  2024-06-14, modify to work with monero seed and polyseed
- Line 738: None **#SEEDSIGNER** 
  Pre-calculate this once on startup
- Line 742: 2024-06-14 
  2024-06-14, adapt for monero seed AND polyseed
- Line 817: None **#SEEDSIGNER** 
  support formats other than ascii?
- Line 938: 2024-06-14 
  2024-06-14, validate

### `src/xmrsigner/models/encode_qr.py`
- Line 15: 2024-06-14 
  2024-06-14, used as quickfix to remove embit.psbt.PSBT! Adapt for monero
- Line 27: None 
  Refactor so that this is a base class with implementation classes for each
- Line 64: 2024-06-20 
  2024-06-20, do we need that? For what purpose? Added with rebase from main to 0.7.0 from seedsigner
- Line 93: None 
  Make these properties?
- Line 222: 2024-06-10 
  2024-06-10, needs to return view only wallet URI
- Line 238: 2024-06-20 
  2024-06-20, I don't know yet, but I belief it will not be the case for Monero!

### `src/xmrsigner/models/psbt_parser.py`
- Line 9: 2024-06-14 
  2024-06-14, quick fix to remove embit.descriptor.Descriptor
- Line 13: 2024-06-14 
  2024-06-14, quick fix to remove embit.psbt.PSBT
- Line 64: 2024-06-14 
  2024-06-14 removed to remove embit.bip39, expect to be deleted all and write from ground up for monero
- Line 124: 2024-06-14 
  2024-06-14, removed whole block to remove embit.script
- Line 132: 2024-06-14 
  2024-06-14, removed whole block to remove embit.script
- Line 149: 2024-06-14 
  2024-06-14 removed to remove embit.networks.NETWORKS
- Line 157: 2024-06-14 
  2024-06-14 removed to remove embit.bip39, expect to be deleted all and write from ground up for monero
- Line 167: 2024-06-14 
  2024-06-14 removed to remove embit.networks.NETWORKS
- Line 178: 2024-06-14 
  2024-06-14, removed to remove embit.psbt.psbt
- Line 198: None 
  Move this to Seed?
- Line 204: None 
  Is this right?
- Line 282: 2024-06-14 
  2024-06-14, removed to remove embit.ec, probably needs to be removed and written from ground up for monero

### `src/xmrsigner/models/settings.py`
- Line 4: 2024-06-16 
  2024-06-16 remove Any if not needed anymore
- Line 16: 2024-06-30 
  2024-06-30 don't know what will uname return on win32, check
- Line 243: None **#SEEDSIGNER** 
  Perhaps prompt the user if the current settings (not including persistent

### `src/xmrsigner/models/settings_definition.py`
- Line 102: 2024-06-10 
  remove comment before 2024-06-10 handle differences in wordlist languages in monero seed and polyseed, think should be handled in the wordlist implementations instead
- Line 144: 2024-06-10 
  remove after 2024-06-10, maybe there should be SETTING__WORDLIST_LANGUAGE_MONERO and SETTING__WORDLIST_LANGUAGE_POLYSEED? Makes this even sense, should it not be more dynamic letting the responsibility to the monero, polyseed implementation to have it more future proof?
- Line 169: None 
  Not using these for display purposes yet (ever?)
- Line 179: None **#SEEDSIGNER** 
  Is there really a difference between ENABLED and PROMPT?
- Line 207: None **#SEEDSIGNER** 
  Handle multi-language `display_name` and `help_text`
- Line 326: None **#SEEDSIGNER** 
  Full babel multilanguage support! Until then, type == HIDDEN
- Line 336: None **#SEEDSIGNER** 
  Support other bip-39 wordlist languages! Until then, type == HIDDEN
- Line 391: None 
  change to VISIBILITY__ADVANCED after implementing passwords for monero seeds, is hidden because this feature is posponed because of insane password derivation method in monero (CryptoNight, need to transpile to python, very propably other #rabbit-hole, be aware before starting!)

### `src/xmrsigner/views/psbt_views.py`
- Line 28: 2024-06-14 
  2024-06-14, quick fix to remove embit.psbt.PSBT
- Line 44: 2024-06-16 
  2024-06-16, added from rebase main to 0.7.0, check if we really need it
- Line 334: None **#SEEDSIGNER** 
  Something is wrong with this psbt(?). Reroute to warning?
- Line 375: 2024-06-14 
  2024-06-14, removed to get rid of embit.script
- Line 390: 2024-06-14 
  2024-06-14, removed to get rid of embit.script
- Line 393: 2024-06-14 
  2024-06-14, removed to get rid of embit.script
- Line 399: 2024-06-14 
  2024-06-14, removed to get rid of embit.network.NETWORKS

### `src/xmrsigner/views/scan_views.py`
- Line 80: 2024-06-20 
  2024-06-20, what about polyseeds?
- Line 114: 2024-06-14 
  2024-06-14, removed to get rid of embit.descriptor.Descriptor
- Line 115: 2024-06-14 
  2024-06-14, removed to get rid of embit.descriptor.Descriptor
- Line 118: None 
  Handle single-sig descriptors?

### `src/xmrsigner/views/screensaver.py`
- Line 12: None 
  This early code is now outdated vis-a-vis Screen vs View distinctions

### `src/xmrsigner/views/seed_views.py`
- Line 97: 2024-06-16 
  2024-06-16, added with rebase from main to 0.7.0 of seedsigner, check if we need it
- Line 136: None **#SEEDSIGNER** 
  Include lock icon on right side of button
- Line 256: 2024-06-30 
  2024-06-30, clean up, this code is now functional but uggly as fuck!
- Line 260: 2024-06-30 
  expire 2024-06-30, lean it up
- Line 598: 2024-06-10 
  2024-06-10: finish implementation
- Line 648: 2024-06-10 
  no warning or different warning for view keys, adapt before 2024-06-10
- Line 652: 2024-06-10 
  see todo above, adapt text to master key and view keys before 2024-06-10
- Line 861: 2024-06-04 
  expire 2024-06-04: adapt to polyseed, monero seed and view keys - we don't supportMyMonero keys for export. Wait, need to check again, seems that is meant to draw your QR codes on paper, so it would not really make sense for view keys, not? Would it? Think again about before taking decision!
- Line 1006: 2024-06-04 
  expire 2024-06-04, can only be 25 (monero seed) or 16 (polyseed)
- Line 1008: 2024-06-30 
  expire 2024-06-30, from there come this numbers, is this not some data comming from QR code constraints? Would it no be wise to get the number from there instead of this???
- Line 1064: None **#SEEDSIGNER** 
  Does this belong in its own BaseThread?
- Line 1112: 2024-06-04 
  expire 2024-06-04, remove BTC related stuff, make it work for monero
- Line 1146: None **#SEEDSIGNER** 
  detect single sig vs multisig or have to prompt?
- Line 1162: 2024-06-04 
  expire 2024-06-04, remove BTC stuff, make monero work
- Line 1219: None **#SEEDSIGNER** 
  Include lock icon on right side of button
- Line 1264: 2024-06-15 
  expire 2024-06-15, what is that about??? Remove BTC stuff and make it for monero working. If not needed for monero, remove it
- Line 1292: 2024-06-15 
  2024-06-15, nonsense for us
- Line 1296: 2024-06-15 
  2024-06-15, remove all the cluster fuck here, we can verify easy if a address belongs to a wallet in monero
- Line 1315: 2024-06-12 
  expire 2024-06-12, check if needed for monero, delete or modify
- Line 1343: 2024-06-10 
  expire 2024-06-10, adapt to monero
- Line 1364: 2024-06-10 
  expire 2024-06-10, adapt to monero
- Line 1404: None **#SEEDSIGNER** 
  Route properly when multisig brute-force addr verification is done
- Line 1429: 2024-06-20 
  2024-06-20
- Line 1525: 2024-06-16 
  2024-06-16
- Line 1557: 2024-06-16 
  2024-06-16

### `src/xmrsigner/views/settings_views.py`
- Line 49: 2024-06-17 
  2024-06-17, display until we know what to do about
- Line 84: None **#SEEDSIGNER** 
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
- Line 548: 2024-06-17 
  2024-06-17, holy clusterfuck, added with rebase from main to 0.7.0 of seedsigner, lot of work to do
- Line 598: None 
  Refactor to a cleaner `BackStack.get_previous_View_cls()`
- Line 652: None 
  Custom derivation path

### `src/xmrsigner/views/view.py`
- Line 69: None **#SEEDSIGNER** 
  Pull all rendering-related code out of Views and into gui.screens implementations
- Line 260: 2024-06-16 
  2024-06-16, why all this drama and not simply `from sys import exit` and `exit(0)`???
- Line 278: 2024-06-16 
  2024-06-16, IMO should be removed

## By Tags

### **#SEEDSIGNER**
- `src/xmrsigner/controller.py`:61
  Refactor these flow-related attrs that survive across multiple Screens.
- `src/xmrsigner/controller.py`:62
  Should all in-memory flow-related attrs get wiped on MainMenuView?
- `src/xmrsigner/controller.py`:75
  end refactor section
- `src/xmrsigner/controller.py`:131
  Rename "storage" to something more indicative of its temp, in-memory state
- `src/xmrsigner/views/psbt_views.py`:334
  Something is wrong with this psbt(?). Reroute to warning?
- `src/xmrsigner/views/view.py`:69
  Pull all rendering-related code out of Views and into gui.screens implementations
- `src/xmrsigner/views/seed_views.py`:136
  Include lock icon on right side of button
- `src/xmrsigner/views/seed_views.py`:1064
  Does this belong in its own BaseThread?
- `src/xmrsigner/views/seed_views.py`:1146
  detect single sig vs multisig or have to prompt?
- `src/xmrsigner/views/seed_views.py`:1219
  Include lock icon on right side of button
- `src/xmrsigner/views/seed_views.py`:1404
  Route properly when multisig brute-force addr verification is done
- `src/xmrsigner/views/settings_views.py`:84
  Free-entry types (are there any?) will need their own SettingsEntryUpdateFreeEntryView(?).
- `src/xmrsigner/hardware/buttons.py`:65
  Refactor to keep control in the Controller and not here
- `src/xmrsigner/hardware/buttons.py`:178
  Implement `release_lock` functionality as a global somewhere. Mixes up design
- `src/xmrsigner/gui/components.py`:20
  Remove all pixel hard coding
- `src/xmrsigner/gui/components.py`:316
  Implement autosize width?
- `src/xmrsigner/gui/components.py`:1011
  Rename the xmrsigner.helpers.Buttons class (to Inputs?) to reduce confusion
- `src/xmrsigner/gui/components.py`:1075
  Only apply screen_y at render
- `src/xmrsigner/gui/screens/screen.py`:88
  Check self.scroll_y and only render visible elements
- `src/xmrsigner/gui/screens/screen.py`:308
  Define an actual class for button_data?
- `src/xmrsigner/gui/screens/screen.py`:688
  Refactor ToastOverlay to support two lines of icon + text and use
- `src/xmrsigner/gui/screens/psbt_screens.py`:134
  Properly handle the ellipsis truncation in different languages
- `src/xmrsigner/gui/screens/psbt_screens.py`:508
  Test rendering the numeric amounts without the supersampling
- `src/xmrsigner/gui/screens/scan_screens.py`:46
  alternate optimization for Pi Zero 2W?
- `src/xmrsigner/gui/screens/scan_screens.py`:109
  Replace the instructions_text with a disappearing
- `src/xmrsigner/gui/screens/seed_screens.py`:61
  support other BIP39 languages/charsets
- `src/xmrsigner/models/settings.py`:243
  Perhaps prompt the user if the current settings (not including persistent
- `src/xmrsigner/models/decode_qr.py`:114
  Convert the test suite rather than handle here?
- `src/xmrsigner/models/decode_qr.py`:134
  Refactor all of these specific `get_` to just something generic like
- `src/xmrsigner/models/decode_qr.py`:189
  Implement this approach across all decoders, COMMENT: probably unnecesary with a refactoring
- `src/xmrsigner/models/decode_qr.py`:308
  Convert the test suite rather than handle here?
- `src/xmrsigner/models/decode_qr.py`:574
  standardize this approach across all decoders (example: SignMessageQrDecoder)
- `src/xmrsigner/models/decode_qr.py`:738
  Pre-calculate this once on startup
- `src/xmrsigner/models/decode_qr.py`:817
  support formats other than ascii?
- `src/xmrsigner/models/settings_definition.py`:179
  Is there really a difference between ENABLED and PROMPT?
- `src/xmrsigner/models/settings_definition.py`:207
  Handle multi-language `display_name` and `help_text`
- `src/xmrsigner/models/settings_definition.py`:326
  Full babel multilanguage support! Until then, type == HIDDEN
- `src/xmrsigner/models/settings_definition.py`:336
  Support other bip-39 wordlist languages! Until then, type == HIDDEN
