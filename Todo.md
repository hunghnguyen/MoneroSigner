# Todo
## Backend
- [x] monero-python for monero seeds
- [ ] [monero-python](https://github.com/DiosDelRayo/monero-python/Todo.md): monero seed encryption/decryption * not part of the CCS, delayed how it seems a rabbit hole (>48h work)
- [x] polyseed-python for Polyseeds
- [ ] implementation for monero signing capability
- [ ] is UR already provided by SeedSigner, or need to switch?
- [ ] check what to do about [mnemonic_generation](src/seedsigner/helpers/mnemonic_generation.py)
## Start
- [x] check partner logos, what to do about?
## Scan
- [ ] check what is needed to Modify
## Seeds
### Seed
- [x] Remove Export Xpub (BTC only)
- [ ] Export monero seed
- [ ] Export Polyseed (if Polyseed wallet)
- [ ] Convert Polyseed to monero 25 words seed (future)
- [ ] Convert 14 words feather wallet seeds to monero 25 words seed (future)
- [ ] Export QR
- [ ] Export View Key
#### Load seed
- [ ] Scan seed QR
- [ ] Enter 13 word monero seed
- [ ] Enter 25 word monero seed
- [ ] Enter 14 words feather wallet seed (think should be supported in future)
- [ ] Enter Polyseed
## Tools
- [x] New camera seed
- [x] restrict normally camara seed to 25 word monero seed, 13 words only possible if activated low security in settings
- [x] New camera Polyseed
- [x] New dice monero seed
- [x] Restrict new dice monero seeds to 25 words, 13 words only possible if activated low security in settings
- [x] New dice Polyseed
- [ ] Calc 25 word monero seed, should show a warning
- [ ] Calc 25 word monero seed, 13 words only possible if activated low security in settings
## Setting
- [ ] Coordinator Software, should not be necessary because of only one way: UR, so remove Coordinator code
- [x] Denomination Display
### Advanced
- [x] Network Monero: Change Regtest to stagenet
- [-] Monero seed passphrase, __not viable at the moment, excluded from the CCS, to be done with calm (#rabbit-hole)__
- [ ] Polyseed passphrase
- [ ] Compact Seed QR (check)
- [x] Partner logos: 'Monero CCS' for now
- [ ] Handle donation screen
- [x] Low security: disabled/enabled

## Other things
- [ ] remove all xpub related code
- [ ] remove seedsigner public signing key from repository
- [ ] offer signatures for source and builds, tend to use signify over gpg
- [ ] Change links where necessary
- [ ] Adapt documentation
- [x] Implement [Polyseed] (https://github.com/DiosDelRayo/polyseed-python)
- [ ] Implement UR [foundation-ur-py](https://github.com/DiosDelRayo/foundation-ur-py)
- [ ] Create companion application
- [ ] Modify [Monero GUI](https://github.com/DiosDelRayo/monero-gui)
---
## Considerations:
- [ ] Shoud feather wallet 14 words seed be offered to be imported?
