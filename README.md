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

How Monero is not a direct decendent from Bitcoin a lot of things are different... Really, a lot!


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
- [x] Scan and parse transaction data from animated QR codes using [UR](https://www.blockchaincommons.com/specifications/Blockchain-Commons-URs-Support-Airgapped-PSBTs/)
- [x] Sign transactions
- [x] Live preview during photo-to-seed and QR scanning UX
- [x] Optimized seed word entry interface
- [x] Support for Monero Mainnet, Stagenet & Testnet
- [x] User-configurable QR code display density (__check: UR documentation about viability__)

### Considerations:
* Built for compatibility using  [UR](https://www.blockchaincommons.com/specifications/Blockchain-Commons-URs-Support-Airgapped-PSBTs/) with Feather Waller, etc, and adapt oficial [Monero GUI](https://www.getmonero.org/downloads/#gui).
* Device takes up to 60 seconds to boot before menu appears (be patient!)
* Always test your setup before transfering larger amounts of bitcoin (try testnet first!)
* Slightly rotating the screen clockwise or counter-clockwise should resolve lighting/glare issues
* If you think XmrSigner adds value to the Monero ecosystem, please help us spread the word! (tweets, pics, videos, etc.)

### Related Repositories
* [This one(XmrSigner)](https://github.com/DiosDelRayo/MoneroSigner)
* [XmrSigner OS](https://github.com/DiosDelRayo/monerosigner-os)
* [Emulator](https://github.com/DiosDelRayo/monerosigner-emulator) forked from [SeedSigner Emulator](https://github.com/enteropositivo/seedsigner-emulator), simple to use and no modifications of the source necessary thanks to overlay mount
* [Polyseed](https://github.com/DiosDelRayo/polyseed-python) transpiled and pythonized from [original Polyseed C-implementation](https://github.com/tevador/polyseed)
* [monero-python](https://github.com/DiosDelRayo/monero-python) fork from from [original](https://github.com/monero-ecosystem/monero-python)
* [monero](https://github.com/DiosDelRayo/monero) fork of [monero](https://github.com/monero-project/monero) to extend `monero-wallet-rpc` with two endpoints for encrypted key images handling
* [Companion Application](https://github.com/DiosDelRayo/XmrSignerCompanion) the Qt 6/C++ Companion Application

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
    - [x] Monero signer companion Application finished
        - [x] Show View Only Wallet QR code
        - [x] Export key images
            - [ ] ~~conversion from monero encrypted key images file to RPC Json~~ => Not viable, used modified monero-wallet-rpc
            - [x] Rest
        - [x] import outputs
        - [x] sign transaction
        - [x] export signed transaction
        - [x] UR's implemented
        - [P] sending progress
        - [P] config QR
    - [x] All missing XmrSigner functionality
        - [x] Show View Only Wallet QR code
        - [x] import outputs
        - [x] Export key images
        - [x] import unsigned transaction
        - [x] show data from unsigned transaction
        - [x] ask for confirmation to proceed
        - [x] sign transaction
        - [x] export signed transaction
        - [x] UR's implemented
    - [X] first xmrsigner image build
    - [x] xmrsigner image build chain


3. Cleanup and production ready (45 days from now)
    - [x] Tools
    - [x] Scripts
    - [x] Documentation final version
    - [x] Final cleanup XmrSigner
    - [x] Final cleanup companion Application


4. Monero-GUI integration (60 days from now from, until PR)
    - [ ] Fork
    - [ ] Modify
    - [ ] PR

P: posponed
W: WIP
?: Not decided yet

XmrSigner development faced numerous technical challenges, including issues with monero-python, complexities in the Monero codebase, and difficulties building monero-wallet-rpc for ARMv6 devices.

## Rabbit holes
Pretty much rabbit holes everywhere, somebody please remember me the next time to at least 3x the estimated time to unforeseen clusterfuck.

## What to expect:
1. Create a PiOS development image with XmrSigner running on it (for development only, not for real use).
2. Fix open imperfections in XmrSigner and XmrSigner Companion code.
3. Continue with milestone 3 targets, bringing XmrSigner to beta state.
4. Finish milestone 4, including Monero GUI integration and PR.
5. Make XmrSigner work on XmrSigner OS (buildroot).
6. Create a phone app to test XmrSigner and other offline signing wallets.
7. Write comprehensive documentation.
8. Implement multisig functionality.
9. Potentially develop XmrSigner NG, a slim reimplementation in Go/Zig/Rust or C++/Qt.

The project remains committed to delivering a functional and secure XmrSigner, despite the challenges encountered.

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

At the moment there is only a development image based on Raspberries Pi OS (buster, pretty old),
with bookworm there is stil an issue with picamera2 although I adapted the code to run on both.
After running in similar issues with buster, it could be that it is only a wrong setting in config.txt.

But honestly, this development image was meant that there is at least something running and the
ability to thinker with it, or check things out. But main focus should be to get it on XmrSigner OS
running. Here is the issue to compile monero-wallet-rpc without to bring even more dependencies, which
are by they way all unnecessary becauae absolutely unneeded for the use case, into buidroot.

I will need how to go further and in which direction, monero-wallet-rpc was a temporary solution to
move "quick" after figuring out at monero-python is mostly only a wrapper around monero-wallet-rpc,
but implementing thing like password or key images import/export base on ch_hash_slow (CryptoNight),
there would be a lot to transpile. So the better approach in my opinion and beneficial for all comming
monero developers would be to take monero souce appart modularize it, minimze dependencies and allow
to compile only what you need. And after that reimplement it without monero-wallet-rpc.

Further I think for the XmrSigner itself there are also too much dependencies, and also completely
unnecessary. Essentially XmrSigner doesn't need an OS, it should run bare metal on the Raspberry Pi or
it should be on something like the i.MX from NXP/Freescale. That all let's so many questions open in which
direction to go from here. Input welcome!

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

# Manual Installation Instructions
see the docs: [Manual Installation Instructions](docs/manual_installation.md) (To be updated)
