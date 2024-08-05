# Inline Todo

Total: 39

## Index
- [Urgent](#urgent)
- [By File](#by-file)
- [By Tags](#by-tags)
- [External Todo](Todo.md)

## Urgent

### 2024-06-04
- `src/xmrsigner/views/tools_views.py`:342
  2024-06-04, rename, because it is missleading, the only thing what will be calculated is the checksum word

### 2024-06-17
- `src/xmrsigner/gui/screens/tools_screens.py`:383
  2024-06-17, added with rebase from main to 0.7.0 of seedsigner, lot of work to do
- `src/xmrsigner/views/tools_views.py`:61
  2024-06-17, activate when it works
- `src/xmrsigner/views/tools_views.py`:63
  2024-06-17, activate when it works
- `src/xmrsigner/views/tools_views.py`:445
  2024-06-17, holy clusterfuck, added with rebase from main to 0.7.0 of seedsigner, lot of work to do

### 2024-06-26
- `src/xmrsigner/views/seed_views.py`:313
  2024-06-26, solve multi network issue
- `src/xmrsigner/views/tools_views.py`:371
  2024-06-26, solve multi network issue
- `src/xmrsigner/views/tools_views.py`:460
  2024-06-26, solve multi network issue
- `src/xmrsigner/views/tools_views.py`:466
  2024-06-26, solve multi network issue
- `src/xmrsigner/views/view.py`:245
  2024-06-26, solve multi network issue
- `src/xmrsigner/views/view.py`:249
  2024-06-26, solve multi network issue

### 2024-06-30
- `src/xmrsigner/models/settings.py`:16
  2024-06-30 don't know what will uname return on win32, check

### 2024-07-15
- `src/xmrsigner/views/seed_views.py`:815
  expire 2024-07-15, from there come this numbers, is this not some data comming from QR code constraints? Would it no be wise to get the number from there instead of this??? Test if smaller are viable

### 2024-07-23
- `src/xmrsigner/views/scan_views.py`:129
  2024-07-23, implement
- `src/xmrsigner/views/scan_views.py`:133
  2024-07-23, implement

### 2024-07-26
- `src/xmrsigner/helpers/monero.py`:234
  2024-07-26, this should be in monero-python

### 2024-07-27
- `src/xmrsigner/views/monero_views.py`:238
  2024-07-27, decide what to do about
- `src/xmrsigner/views/monero_views.py`:268
  2024-07-27, decide to check or remove
- `src/xmrsigner/views/monero_views.py`:390
  2024-07-27, code missing here!
- `src/xmrsigner/views/wallet_views.py`:151
  2024-07-27, thought: redirect to address viewer as soon it exists

### 2024-07-28
- `src/xmrsigner/gui/components.py`:774
  2024-07-28, render only with Monero Logo
- `src/xmrsigner/gui/components.py`:851
  2024-07-28, render only with Monero Logo

### 2024-08-02
- `src/xmrsigner/gui/components.py`:764
  2024-08-02, change to Monero icon

### 2024-08-04
- `src/xmrsigner/views/wallet_views.py`:225
  2024-08-04, implement

### No time constraint
- `src/test/xmrsigner/helpers/polyseed_mnemonic_generation.py`:13
  not working yet, some issue in polyseed-python
- `src/xmrsigner/gui/components.py`:201
  don't need BTC, need XMR glyph is still Bitcoin
- `src/xmrsigner/gui/components.py`:202
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
- `src/xmrsigner/views/screensaver.py`:12
  This early code is now outdated vis-a-vis Screen vs View distinctions
- `src/xmrsigner/views/tools_views.py`:495
  Refactor to a cleaner `BackStack.get_previous_View_cls()`
- `src/xmrsigner/views/tools_views.py`:549
  Custom derivation path

## By File

### `src/test/xmrsigner/helpers/polyseed_mnemonic_generation.py`
- Line 13: None 
  not working yet, some issue in polyseed-python

### `src/xmrsigner/gui/components.py`
- Line 201: None 
  don't need BTC, need XMR glyph is still Bitcoin
- Line 202: None 
  don't need BTC, need XMR glyph is still Bitcoin
- Line 764: 2024-08-02 
  2024-08-02, change to Monero icon
- Line 774: 2024-07-28 
  2024-07-28, render only with Monero Logo
- Line 851: 2024-07-28 
  2024-07-28, render only with Monero Logo

### `src/xmrsigner/gui/screens/tools_screens.py`
- Line 383: 2024-06-17 
  2024-06-17, added with rebase from main to 0.7.0 of seedsigner, lot of work to do

### `src/xmrsigner/hardware/buttons.py`
- Line 66: None **#SEEDSIGNER** 
  Refactor to keep control in the Controller and not here
- Line 179: None **#SEEDSIGNER** 
  Implement `release_lock` functionality as a global somewhere. Mixes up design

### `src/xmrsigner/helpers/monero.py`
- Line 234: 2024-07-26 
  2024-07-26, this should be in monero-python

### `src/xmrsigner/helpers/monero_time.py`
- Line 1: None 
  move this to monero-python, network related part should maybe move to .network?

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

### `src/xmrsigner/models/settings.py`
- Line 16: 2024-06-30 
  2024-06-30 don't know what will uname return on win32, check

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
- Line 313: 2024-06-26 
  2024-06-26, solve multi network issue
- Line 815: 2024-07-15 
  expire 2024-07-15, from there come this numbers, is this not some data comming from QR code constraints? Would it no be wise to get the number from there instead of this??? Test if smaller are viable

### `src/xmrsigner/views/tools_views.py`
- Line 61: 2024-06-17 
  2024-06-17, activate when it works
- Line 63: 2024-06-17 
  2024-06-17, activate when it works
- Line 342: 2024-06-04 
  2024-06-04, rename, because it is missleading, the only thing what will be calculated is the checksum word
- Line 371: 2024-06-26 
  2024-06-26, solve multi network issue
- Line 445: 2024-06-17 
  2024-06-17, holy clusterfuck, added with rebase from main to 0.7.0 of seedsigner, lot of work to do
- Line 460: 2024-06-26 
  2024-06-26, solve multi network issue
- Line 466: 2024-06-26 
  2024-06-26, solve multi network issue
- Line 495: None 
  Refactor to a cleaner `BackStack.get_previous_View_cls()`
- Line 549: None 
  Custom derivation path

### `src/xmrsigner/views/view.py`
- Line 245: 2024-06-26 
  2024-06-26, solve multi network issue
- Line 249: 2024-06-26 
  2024-06-26, solve multi network issue

### `src/xmrsigner/views/wallet_views.py`
- Line 151: 2024-07-27 
  2024-07-27, thought: redirect to address viewer as soon it exists
- Line 225: 2024-08-04 
  2024-08-04, implement

## By Tags

### **#SEEDSIGNER**
- `src/xmrsigner/hardware/buttons.py`:66
  Refactor to keep control in the Controller and not here
- `src/xmrsigner/hardware/buttons.py`:179
  Implement `release_lock` functionality as a global somewhere. Mixes up design
- `src/xmrsigner/models/base_decoder.py`:29
  standardize this approach across all decoders (example: SignMessageQrDecoder)
