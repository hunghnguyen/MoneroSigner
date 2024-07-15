# Build an offline, airgapped Monero signing device for less than $50!

---------------

* [Project Summary](#project-summary)
* [Features](#features)
* [Related Repositories](#related-repositories)
* [Todo](Todo.md)
* [Monero CCS Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/465)
* [Milestones](#milestones)
* [Timeline](#timeline)
* [Shopping List](#shopping-list)
* [Software Installation](#software-installation)
  * [Verifying Your Software](#verifying-your-software)
* [Enclosure Designs](#enclosure-designs)
* [SeedQR Printable Templates](#seedqr-printable-templates)
* [Manual Installation Instructions](#manual-installation-instructions)


---------------

 MoneroSigner is in the process of rebranding to XmrSigner, to be not confused to an abandoned project called MoneroSigner.

---------------

# Project Summary

 XmrSigner is a fork from [SeedSigner](https://github.com/SeedSigner/seedsigner), Bitcoin signing device. It builds on the same hardware and actually you could use the same device for Monero and Bitcoin with two different microSD cards. MoneroSigner offers anyone the opportunity to build a verifiably air-gapped, stateless Monero signing device using inexpensive, publicly available hardware components (usually < $50).

How Monero is not a direct decendent from Bitcoin a lot of things are different...


### Features

- [x] Calculate word 13/25 of monero seed phrase
- [x] Create a 25-word monero seed phrase with 99 dice rolls
- [x] Create a 16 word polyseed phrase with 99(?) dice rolls
- [x] Create a 25-word monero seed phrase by taking a digital photo
- [x] Create a 16-word polyseed phrase by taking a digital photo
- [x] Temporarily store up to 3 seed phrases while device is powered
- [ ] ~~Monero passphrase support~~, posponed, possible #rabbit-hole (>48h work to implement in python)
- [x] Polyseed passphrase support
- [ ] ~~Multisig support~~: later
- [ ] Scan and parse transaction data from animated QR codes using [UR](https://www.blockchaincommons.com/specifications/Blockchain-Commons-URs-Support-Airgapped-PSBTs/)
- [ ] Sign transactions
- [x] Live preview during photo-to-seed and QR scanning UX
- [x] Optimized seed word entry interface
- [ ] Support for Monero Mainnet, Stagenet & Testnet
- [ ] User-configurable QR code display density (__check: UR documentation about viability__)

### Considerations:
* Built for compatibility using  [UR](https://www.blockchaincommons.com/specifications/Blockchain-Commons-URs-Support-Airgapped-PSBTs/) with Feather Waller, etc (__check__), and adapt oficial [Monero GUI](https://www.getmonero.org/downloads/#gui).
* Device takes up to 60 seconds to boot before menu appears (be patient!)
* Always test your setup before transfering larger amounts of bitcoin (try testnet first!)
* Slightly rotating the screen clockwise or counter-clockwise should resolve lighting/glare issues
* If you think XmrSigner adds value to the Monero ecosystem, please help us spread the word! (tweets, pics, videos, etc.)

### Related Repositories
* [This one(MoneroSigner](https://github.com/DiosDelRayo/MoneroSigner)
* [Emulator](https://github.com/DiosDelRayo/monerosigner-emulator) forked from [SeedSigner Emulator](https://github.com/enteropositivo/seedsigner-emulator), simple to use and no modifications of the source necessary thanks to overlay mount
* [Polyseed](https://github.com/DiosDelRayo/polyseed-python) transpiled and pythonized from [original Polyseed C-implementation](https://github.com/tevador/polyseed)
* [Companion Application](https://github.com/DiosDelRayo/XmrSignerCompanion) the Qt 6/C++ Companion Application
* Companion Application [#Todo](Todo.md)

---------------
# Milestones
1. Monero Signer basics on emulator (10 days from now)
    - [x] Emulator easy start
    - [x] Polyseed python implementation
    - [x] Monero seed generation with camera for entropy
    - [x] Monero seed generation on dice rolls
    - [x] Monero seed generation by picking words
    - [x] Polyseed generation with camera for entropy
    - [x] Polyseed generation on dice rolls
    - [ ] ~~Polyseed generation by picking words~~ can't be done, because you can't choose words, because seeds are generate with pbkdf sha256, so only one way, we could over an alternative, or generate need seeds out of the choosen one.
    - [x] Wallet export seed phrase
    - [-] ~~Wallet export seed hex~~ not to be implemented, bad decision
    - [x] Wallet export QR code
    - [x] Build script to generate executable for linux
    - [x] Build script to generate executable win32
    - [-] ~~Build script to generate executable macOS~~ Not supported: use Docker


2. XmrSigner working with companion Application (25 days from now)
    - [ ] Monero signer companion Application finished
        - [x] Show View Only Wallet QR code
        - [ ] Export key images
            - [ ] conversion from monero encrypted key images file to RPC Json 
            - [x] Rest
        - [x] import outputs
        - [x] sign transaction
        - [x] export signed transaction
        - [x] UR's implemented
        - [ ] sending progress
        - [ ] config QR
    - [ ] All missing XmrSigner functionality
        - [x] Show View Only Wallet QR code
        - [ ] import outputs
        - [ ] Export key images
        - [ ] import unsigned transaction
        - [ ] show data from unsigned transaction
        - [ ] ask for confirmation to proceed
        - [ ] sign transaction
        - [ ] export signed transaction
        - [ ] UR's implemented
    - [X] first xmrsigner image build
    - [x] xmrsigner image build chain


3. Cleanup and production ready (45 days from now)
    - [ ] Tools
    - [ ] Scripts
    - [ ] Documentation final version
    - [ ] Final cleanup XmrSigner
    - [ ] Final cleanup companion Application


4. Monero-GUI integration (60 days from now from, until PR)
    - [ ] Fork
    - [ ] Modify
    - [ ] PR
---------------
# Timeline
```
 /------------------------------------------------------------- 2024-05-25 Proposal and project start
 |
 |   /--------------------------------------------------------- 2024-05-29 Ordered missing hardware (Display hat + pi cam)
 |   |
 |   |   /----------------------------------------------------- 2024-05-02 missing hardware arrived
 |   |   |
 |   |   | /--------------------------------------------------- 2024-06-04 Milestone 1, estimated arrival of hardware
 |   |   | |
 |   |   | |              /------------------------------------ 2024-06-19 Milestone 2
 |   |   | |              |
 |   |   | |              |                   /---------------- 2024-07-09 Milestone 3
 |   |   | |              |                   |
 |   |   | |              |                   |              /- 2024-07-24 Milestone 4
 |   |   | |              |                   |              |
(S)==|===|(1)============(2)=================(3)============(4)=====>
                                                     A
                                                     |
                                                     \------ Today: 2024-07-14

Heavy delay, Milestone 2 not yet finished. Try to hurry harder.
Pretty much rabbit holes everywhere, somebody please remember me the next time to at least 3x
the estimated time to unforseen clusterfuck.

XmrSigner and XmrSigner Companion use for now the monero-wallet-rpc, to not import the whole monero source monster into that source, but to accomplish the compatibility the key images need to be transfered in the format monero-wallet-cli writes and reads the files. (wallet2)

Now, no problem then let's write a converter on both sides, pack the json into binary form and then encrypt it with the secret view key. Needed: ed25519, keccak_256 and chacha20, well, not a walk of cake but doable in some hours. Only to figure out, then that key generation for chacha20 uses...tata: cn_slow_hash `*arg*` WTF.

So, when you now go to untangle there the source you pulling one spaghetti after another...

Options:
 - Implement cn_slow_hash in python and try to cut the cn_slow_hash part out of the monero monster source with a scalpel, but I have huge worries that one dependency leads to the next, how I have studied the monero source until now... -> so, not at the moment how I drown finacially already but prefered version.
 - switch to wallet2 for companion and use monero-wallet-cli on XmrSigner -> seems pretty uggly almost disgusting to me
 - patch monero-wallet-rpc -> probably the best quick fix, but don't know yet what to do about. Because it would be to try a PR or maintain a fork, with a permanent headache, although, how it would be a temporary solution... (there is not something like a temporary solution, if it works 99% of the time it will stay and hurt as fuck. Would mean to add two endpoints more to monero-wallet-rpc: `export_key_images_binary` and `import_key_images_binary`. -> also ugly but probably the solution for now.
 - using a combo of monero-wallet-rpc with monero-wallet-cli -> WTF, fuck off, this is the uggliest of all hacks

 Will postpone the decission because already enough time wasted...
```
---------------

# Shopping List

To build a SeedSigner, you will need:

* Raspberry Pi Zero (preferably version 1.3 with no WiFi/Bluetooth capability, but any Raspberry Pi 2/3/4 or Zero model will work)
* Waveshare 1.3" 240x240 pxl LCD (correct pixel count is important, more info at https://www.waveshare.com/wiki/1.3inch_LCD_HAT)
* Pi Zero-compatible camera (tested to work with the Aokin / AuviPal 5MP 1080p with OV5647 Sensor)

Notes:
* You will need to solder the 40 GPIO pins (20 pins per row) to the Raspberry Pi Zero board. If you don't want to solder, purchase "GPIO Hammer Headers" for a solderless experience.
* Other cameras with the above sensor module should work, but may not fit in the Orange Pill enclosure
* Choose the Waveshare screen carefully; make sure to purchase the model that has a resolution of 240x240 pixels

---------------

# Software Installation

This section is comming soon

---------------

# Enclosure Designs

Comming soon

## Community Designs

* [Lil Pill](https://cults3d.com/en/3d-model/gadget/lil-pill-seedsigner-case) by @_CyberNomad
* [OrangeSurf Case](https://github.com/orangesurf/orangesurf-seedsigner-case) by @OrangeSurfBTC
* [PS4 Seedsigner](https://www.thingiverse.com/thing:5363525) by @Silexperience
* [OpenPill Faceplate](https://www.printables.com/en/model/179924-seedsigner-open-pill-cover-plates-digital-cross-jo) by @Revetuzo 
* [Waveshare CoverPlate](https://cults3d.com/en/3d-model/various/seedsigner-coverplate-for-waveshare-1-3-inch-lcd-hat-with-240x240-pixel-display) by @Adathome1

---------------

# SeedQR Printable Templates

Comming soon.

---------------

# Manual Installation Instructions
see the docs: [Manual Installation Instructions](docs/manual_installation.md) (To be updated)
