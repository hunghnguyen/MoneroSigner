# Manual Installation Instructions (on Linux)

Create the base image from Raspberry Pi OS buster, and flash it to a microSD card.

```bash
make image-buster
```

Username: xmrsigner
Password: xmrsigner

Plug the pi zero into your usb and on the pi zero end in the USB OTG port.

```bash
make dev-device-shell
```
will search the pi on you usb ethernet port, and ssh with the ssh key into the pi as user `xmrsigner`

Now launch the Raspberry Pi's System Configuration tool using the command:
```
sudo raspi-config
```

Set the following:
* `Interface Options`:
    * `Camera`: enable
    * `SPI`: enable
* `Localisation Options`:
    * `Locale`: arrow up and down through the list and select or deselect languages with the spacebar.
        * Deselect the default language option that is selected
        * Select `en_US.UTF-8 UTF-8` for US English
* You will also need to configure the WiFi settings if you are using the #1 option above to connect to the internet

When you exit the System Configuration tool, you will be prompted to reboot the system; allow the system to reboot and continue with these instructions.

### Install dependencies
Copy this entire box and run it as one command (will take 15-20min to complete):
```
sudo apt-get update && sudo apt-get install -y wiringpi python3-pip \
   python3-numpy python-pil libopenjp2-7 git python3-opencv \
   python3-picamera libatlas-base-dev qrencode
```

### Install `zbar`
`zbar` is "an open source software suite for reading bar codes" (more info here: [https://github.com/mchehab/zbar](https://github.com/mchehab/zbar)).

SeedSigner requires `zbar` at 0.23.x or higher.

Download the binary:
```
curl -L http://raspbian.raspberrypi.org/raspbian/pool/main/z/zbar/libzbar0_0.23.90-1_armhf.deb --output libzbar0_0.23.90-1_armhf.deb
```

And then install it:
```
sudo apt install ./libzbar0_0.23.90-1_armhf.deb
```

Cleanup:
```
rm libzbar0_0.23.90-1_armhf.deb
```

### Install the [C library for Broadcom BCM 2835](http://www.airspayce.com/mikem/bcm2835/)
This library "provides functions for reading digital inputs and setting digital outputs, using SPI and I2C, and for accessing the system timers."

Run each of the following individual steps:
```
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.60.tar.gz
tar zxvf bcm2835-1.60.tar.gz
cd bcm2835-1.60/
sudo ./configure
sudo make && sudo make check && sudo make install
cd ..
rm bcm2835-1.60.tar.gz
sudo rm -rf bcm2835-1.60
```

### Install XmrSigner
```bash
sudo mkdir -p /opt/xmrsigner
sudo chown -R xmrsigner:xmrsigner /opt/xmrsigner
cd /opt/xmrsigner
python3 -m venv .
```

Then logout of the XmrSigner and
```
make dev-device-install-requirements
make dev-device-rsync
```
will install the requirements and  copy the source of XmrSigner to the XmrSigner development device

Finally:
```bash
make dev-device-reboot
```

After the pi zero cam up again, you can wath the logfile with:
```bash
make dev-device-log
```

I know it is still a bit complicated but I ran out of time, I will integrate this all in `make image-buster` ASAP.
