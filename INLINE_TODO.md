# Inline Todo

Total: 41

## Index
- [Urgent](#urgent)
- [By File](#by-file)
- [By Tags](#by-tags)
- [External Todo](Todo.md)

## Urgent

### 2024-06-04
- `src/xmrsigner/views/tools_views.py`:340
  2024-06-04, rename, because it is missleading, the only thing what will be calculated is the checksum word

### 2024-06-17
- `src/xmrsigner/gui/screens/tools_screens.py`:383
  2024-06-17, added with rebase from main to 0.7.0 of seedsigner, lot of work to do
- `src/xmrsigner/views/tools_views.py`:59
  2024-06-17, activate when it works
- `src/xmrsigner/views/tools_views.py`:61
  2024-06-17, activate when it works
- `src/xmrsigner/views/tools_views.py`:443
  2024-06-17, holy clusterfuck, added with rebase from main to 0.7.0 of seedsigner, lot of work to do

### 2024-06-26
- `src/xmrsigner/views/seed_views.py`:333
  2024-06-26, solve multi network issue
- `src/xmrsigner/views/tools_views.py`:369
  2024-06-26, solve multi network issue
- `src/xmrsigner/views/tools_views.py`:458
  2024-06-26, solve multi network issue
- `src/xmrsigner/views/tools_views.py`:464
  2024-06-26, solve multi network issue
- `src/xmrsigner/views/view.py`:245
  2024-06-26, solve multi network issue
- `src/xmrsigner/views/view.py`:249
  2024-06-26, solve multi network issue

### 2024-06-30
- `src/xmrsigner/models/settings.py`:16
  2024-06-30 don't know what will uname return on win32, check

### 2024-07-15
- `src/xmrsigner/views/seed_views.py`:836
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
- `src/xmrsigner/views/monero_views.py`:239
  2024-07-27, decide what to do about
- `src/xmrsigner/views/monero_views.py`:269
  2024-07-27, decide to check or remove
- `src/xmrsigner/views/monero_views.py`:391
  2024-07-27, code missing here!
- `src/xmrsigner/views/wallet_views.py`:151
  2024-07-27, thought: redirect to address viewer as soon it exists

### 2024-07-28
- `src/xmrsigner/gui/components.py`:790
  2024-07-28, render only with Monero Logo
- `src/xmrsigner/gui/components.py`:867
  2024-07-28, render only with Monero Logo

### 2024-08-02
- `src/xmrsigner/gui/components.py`:780
  2024-08-02, change to Monero icon

### 2024-08-04
- `src/xmrsigner/views/wallet_views.py`:225
  2024-08-04, implement

### 2024-08-08
- `src/xmrsigner/views/scan_views.py`:43
  2024-08-08, not sure if this is a good idea, refactor one day

### 2024-08-09
- `src/xmrsigner/views/seed_views.py`:442
  2024-08-09, implement
- `src/xmrsigner/views/wallet_views.py`:209
  2024-08-09 implement

### No time constraint
- `src/test/xmrsigner/helpers/polyseed_mnemonic_generation.py`:13
  not working yet, some issue in polyseed-python
- `src/xmrsigner/gui/components.py`:217
  don't need BTC, need XMR glyph is still Bitcoin
- `src/xmrsigner/gui/components.py`:218
  don't need BTC, need XMR glyph is still Bitcoin
- `src/xmrsigner/hardware/buttons.py`:149
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
- `src/xmrsigner/views/tools_views.py`:493
  Refactor to a cleaner `BackStack.get_previous_View_cls()`
- `src/xmrsigner/views/tools_views.py`:547
  Custom derivation path

## By File

### `src/test/xmrsigner/helpers/polyseed_mnemonic_generation.py`
- Line 13: None 
  not working yet, some issue in polyseed-python

### `src/xmrsigner/gui/components.py`
- Line 217: None 
  don't need BTC, need XMR glyph is still Bitcoin
- Line 218: None 
  don't need BTC, need XMR glyph is still Bitcoin
- Line 780: 2024-08-02 
  2024-08-02, change to Monero icon
- Line 790: 2024-07-28 
  2024-07-28, render only with Monero Logo
- Line 867: 2024-07-28 
  2024-07-28, render only with Monero Logo

### `src/xmrsigner/gui/screens/tools_screens.py`
- Line 383: 2024-06-17 
  2024-06-17, added with rebase from main to 0.7.0 of seedsigner, lot of work to do

### `src/xmrsigner/hardware/buttons.py`
- Line 149: None **#SEEDSIGNER** 
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
- Line 239: 2024-07-27 
  2024-07-27, decide what to do about
- Line 269: 2024-07-27 
  2024-07-27, decide to check or remove
- Line 391: 2024-07-27 
  2024-07-27, code missing here!

### `src/xmrsigner/views/scan_views.py`
- Line 43: 2024-08-08 
  2024-08-08, not sure if this is a good idea, refactor one day
- Line 129: 2024-07-23 
  2024-07-23, implement
- Line 133: 2024-07-23 
  2024-07-23, implement

### `src/xmrsigner/views/screensaver.py`
- Line 12: None 
  This early code is now outdated vis-a-vis Screen vs View distinctions

### `src/xmrsigner/views/seed_views.py`
- Line 333: 2024-06-26 
  2024-06-26, solve multi network issue
- Line 442: 2024-08-09 
  2024-08-09, implement
- Line 836: 2024-07-15 
  expire 2024-07-15, from there come this numbers, is this not some data comming from QR code constraints? Would it no be wise to get the number from there instead of this??? Test if smaller are viable

### `src/xmrsigner/views/tools_views.py`
- Line 59: 2024-06-17 
  2024-06-17, activate when it works
- Line 61: 2024-06-17 
  2024-06-17, activate when it works
- Line 340: 2024-06-04 
  2024-06-04, rename, because it is missleading, the only thing what will be calculated is the checksum word
- Line 369: 2024-06-26 
  2024-06-26, solve multi network issue
- Line 443: 2024-06-17 
  2024-06-17, holy clusterfuck, added with rebase from main to 0.7.0 of seedsigner, lot of work to do
- Line 458: 2024-06-26 
  2024-06-26, solve multi network issue
- Line 464: 2024-06-26 
  2024-06-26, solve multi network issue
- Line 493: None 
  Refactor to a cleaner `BackStack.get_previous_View_cls()`
- Line 547: None 
  Custom derivation path

### `src/xmrsigner/views/view.py`
- Line 245: 2024-06-26 
  2024-06-26, solve multi network issue
- Line 249: 2024-06-26 
  2024-06-26, solve multi network issue

### `src/xmrsigner/views/wallet_views.py`
- Line 151: 2024-07-27 
  2024-07-27, thought: redirect to address viewer as soon it exists
- Line 209: 2024-08-09 
  2024-08-09 implement
- Line 225: 2024-08-04 
  2024-08-04, implement

## By Tags

### **#SEEDSIGNER**
- `src/xmrsigner/hardware/buttons.py`:149
  Implement `release_lock` functionality as a global somewhere. Mixes up design
- `src/xmrsigner/models/base_decoder.py`:29
  standardize this approach across all decoders (example: SignMessageQrDecoder)
