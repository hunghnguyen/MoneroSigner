# Todo
## Backend
- [x] monero-python for monero seeds
- [.] [monero-python](https://github.com/DiosDelRayo/monero-python/Todo.md): monero seed encryption/decryption * not part of the CCS, delayed how it seems a rabbit hole (>48h work)
- [x] polyseed-python for Polyseeds
- [x] implementation for monero signing capability
- [x] UR
- [ ] check what to do about [mnemonic_generation](src/seedsigner/helpers/mnemonic_generation.py)
## Start
- [x] check partner logos, what to do about?
## Scan
- [x] check what is needed to Modify
## Seeds
### Seed
- [x] Remove Export Xpub (BTC only)
- [x] Export monero seed
- [x] Export Polyseed (if Polyseed wallet)
- [x] Convert Polyseed to monero 25 words seed
- [.] Convert 14 words feather wallet seeds to monero 25 words seed (future)
- [x] Export QR
- [x] Export View Key
#### Load seed
- [x] Scan seed QR
- [x] Enter 13 word monero seed
- [x] Enter 25 word monero seed
- [?] Enter 14 words feather wallet seed (think should be supported in future)
- [x] Enter Polyseed
## Tools
- [x] New camera seed
- [x] restrict normally camara seed to 25 word monero seed, 13 words only possible if activated low security in settings
- [x] New camera Polyseed
- [x] New dice monero seed
- [x] Restrict new dice monero seeds to 25 words, 13 words only possible if activated low security in settings
- [x] New dice Polyseed
- [x] Pick own words monero seed only with activated low security in settings
- [x] Calc 25 word monero seed, should show a warning
- [x] Calc 25 word monero seed, 13 words only possible if activated low security in settings
## Setting
- [x] Coordinator Software, should not be necessary because of only one way: UR, so remove Coordinator code
- [x] Denomination Display
### Advanced
- [x] Network Monero: Change Regtest to stagenet
- [-] Monero seed passphrase, __not viable at the moment, excluded from the CCS, to be done with calm (#rabbit-hole)__
- [x] Polyseed passphrase
- [x] Compact Seed QR
- [x] Partner logos: 'Monero CCS' for now
- [ ] Handle donation screen
- [x] Low security: disabled/enabled

## Other things
- [x] remove all xpub related code
- [x] remove seedsigner public signing key from repository
- [ ] offer signatures for source and builds, tend to use signify over gpg
- [ ] Change links where necessary
- [ ] Adapt documentation
- [x] Implement [Polyseed](https://github.com/DiosDelRayo/polyseed-python)
- [W] Implement [Companion Application](https://github.com/DiosDelRayo/XmrSignerCompanion)
- [x] Implement UR [foundation-ur-py](https://github.com/DiosDelRayo/foundation-ur-py)
- [ ] Modify [Monero GUI](https://github.com/DiosDelRayo/monero-gui)
- [x] tools/increment_version.py needs also to update the version in setup.py
- [x] setup.py needs further modification
- [x] not working as expcted, fix: tools/tag_version.py
- [ ] remove old font if unused
- [ ] check how to generate font to include monero logo
---
## Considerations:
- [?] Shoud feather wallet 14 words seed be offered to be imported?
---
see also: [Inline Todo](INLINE_TODO.md)

## SECURITY RELATED!
- [ ] study: [monero burning bug](https://www.getmonero.org/2018/09/25/a-post-mortum-of-the-burning-bug.html)
- [ ] study: [public key be used for more-than one payment](https://monero.stackexchange.com/questions/4163/can-a-one-time-public-key-be-used-for-more-than-one-payment)
- [x] consult `jeffro256` about security issues on MoneroSigner in-/outside (Monero-GUI modification, monero-python, Companion Application), `rucknium` referd me to him. => [@see chat](chat-monero-community.txt), but mostly the result is checking if camera digesting is enriched with /dev/urandom and second all the rest seems good.
