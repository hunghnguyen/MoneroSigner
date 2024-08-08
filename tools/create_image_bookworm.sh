#!/bin/bash
DEVIMAGE_DIR=$PWD/devimage
DEVIMAGE_NAME=xmrsigner-dev.img
DEVIMAGE_MOUNT_BOOT=/mnt/xmrsignerdev_boot
DEVIMAGE_MOUNT_ROOT=/mnt/xmrsignerdev_root
PIOS_LITE_URL=https://downloads.raspberrypi.org/raspios_lite_armhf/images
HOSTNAME=xmrsigner-dev
USER=xmrsigner
PASSWORD=$(openssl passwd -5 "xmrsigner")
SSID=xmrsigner
NETWORK_PASSWORD=$(openssl passwd -5 "xmrsigner")

set -e

check_sudo() {
	if [ "$(id -u)" -ne 0 ]; then
		echo -e "\nThis script requires sudo privileges..."
		sudo true
		if [ $? -ne 0 ]
		then
			echo "This script requires sudo privileges, but failed to aquire..."
			exit 1
		fi
	fi
}

download_pios_image() {
	if [ ! -f $DEVIMAGE_DIR/raspios-lite.img ]
	then
		# Download the latest Raspberry Pi OS Lite image
		LATEST_IMAGE=$(curl -s $PIOS_LITE_URL/ | grep -oP 'href="raspios_lite_armhf-\K[0-9-]*' | tail -n 1)
		IMAGE_NAME=$(curl -s "${PIOS_LITE_URL}/raspios_lite_armhf-${LATEST_IMAGE}/" | grep -oP 'href="\K[^"]*-raspios-[a-z]*-armhf-lite\.img\.xz' | head -n 1)
		IMAGE_URL="${PIOS_LITE_URL}/raspios_lite_armhf-${LATEST_IMAGE}/${IMAGE_NAME}"
		mkdir -p $DEVIMAGE_DIR
		echo 'Download RaspiOS lite image...'
		wget -c -O $DEVIMAGE_DIR/raspios-lite.img.xz "$IMAGE_URL"
		echo 'Extract RaspiOS lite image...'
		xz -d $DEVIMAGE_DIR/raspios-lite.img.xz
	fi
}

modify_image() {
    LOOP_DEVICE=$(sudo losetup -Pf --show $DEVIMAGE_DIR/$DEVIMAGE_NAME)
    
    sudo mkdir -p $DEVIMAGE_MOUNT_BOOT
    sudo mkdir -p $DEVIMAGE_MOUNT_ROOT

    # Mount partitions
    sudo mount "${LOOP_DEVICE}p1" $DEVIMAGE_MOUNT_BOOT
    sudo mount "${LOOP_DEVICE}p2" $DEVIMAGE_MOUNT_ROOT

    # Enable USB OTG
    echo "dtoverlay=dwc2" | sudo sh -c "cat >> $DEVIMAGE_MOUNT_BOOT/config.txt"
    sudo sed -i 's/#dtparam=spi=on/dtparam=spi=on/' $DEVIMAGE_MOUNT_BOOT/cmdline.txt
    sudo sed -i 's/rootwait/rootwait modules-load=dwc2,g_ether spidev.bufsiz=131072/' $DEVIMAGE_MOUNT_BOOT/cmdline.txt

    # custom toml
    cat << EOCT | sudo sh -c "cat > ${DEVIMAGE_MOUNT_BOOT}/custom.toml"
# Raspberry PI OS config.toml
# This file is used for the initial setup of the system on the first boot, if
# it's s present in the boot partition of the installation.
#
# This file is loaded by firstboot, parsed by init_config and ends up
# as several calls to imager_custom.
# The example below has all current fields.
#
# References:
# - https://github.com/RPi-Distro/raspberrypi-sys-mods/blob/master/usr/lib/raspberrypi-sys-mods/firstboot
# - https://github.com/RPi-Distro/raspberrypi-sys-mods/blob/master/usr/lib/raspberrypi-sys-mods/init_config
# - https://github.com/RPi-Distro/raspberrypi-sys-mods/blob/master/usr/lib/raspberrypi-sys-mods/imager_custom

# Required:
config_version = 1

[system]
hostname = "${HOSTNAME}"

[user]
# If present, the default "rpi" user gets renamed to this "name"
name = "${USER}"
# The password can be encrypted or plain. To encrypt, we can use "openssl passwd -5 raspberry"
password = "${PASSWORD}"
password_encrypted = true

[ssh]
# ssh_import_id = "gh:user" # import public keys from github
enabled = true
password_authentication = true # probably broken, let's test anyway
# We can also seed the ssh public keys configured for the default user:
authorized_keys = [ "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOehLkdqEEaaXBrv2ooTE92+jbC/b3Wrvp+R3b9HnSS9" ]

[wlan]
ssid = "${SSID}"
password = "${NETWORK_PASSWORD}"
password_encrypted = true
hidden = false
# The country is written to /etc/default/crda
# Reference: https://wireless.wiki.kernel.org/en/developers/Regulatory
country = "US"

[locale]
keymap = "us"
timezone = "UTC"
EOCT

    echo 'Setup usb0 network interface...'
    cat << 'EOF' | sudo sh -c "cat > ${DEVIMAGE_MOUNT_ROOT}/etc/network/interfaces.d/usb0"
allow-hotplug usb0
iface usb0 inet dhcp
EOF

    echo 'Creating XmrSigner service...'
    cat << EOF | sudo sh -c "cat > ${DEVIMAGE_MOUNT_ROOT}/etc/systemd/system/xmrsigner.service"
[Unit]
Description=XmrSigner

[Service]
User=xmrsigner
WorkingDirectory=/opt/xmrsigner
ExecStart=/bin/bash -c 'source /opt/xmrsigner/bin/activate && /usr/bin/python3 -m xmrsigner >> /var/log/xmrsigner.log 2>&1'
Restart=always

[Install]
WantedBy=multi-user.target
EOF

    sudo touch ${DEVIMAGE_MOUNT_ROOT}/var/log/xmrsigner.log
    sudo chown xmrsigner:xmrsigner ${DEVIMAGE_MOUNT_ROOT}/var/log/xmrsigner.log
    sudo chmod 644 ${DEVIMAGE_MOUNT_ROOT}/var/log/xmrsigner.log
    sudo ln -s ${DEVIMAGE_MOUNT_ROOT}/etc/systemd/system/xmrsigner.service ${DEVIMAGE_MOUNT_ROOT}/etc/systemd/system/multi-user.target.wants/xmrsigner.service

    # Unmount the image
    sudo umount $DEVIMAGE_MOUNT_BOOT
    sudo umount $DEVIMAGE_MOUNT_ROOT
    sudo losetup -d "$LOOP_DEVICE"
    sudo rmdir $DEVIMAGE_MOUNT_BOOT
    sudo rmdir $DEVIMAGE_MOUNT_ROOT
}

create_image() {
	# Create and modify the image
	if [ ! -f $DEVIMAGE_DIR/$DEVIMAGE_NAME ] || [ "$1" == "--force" ]; then
	    cp $DEVIMAGE_DIR/raspios-lite.img $DEVIMAGE_DIR/$DEVIMAGE_NAME
	    modify_image
	    cat << EOSUCCESS
XmrSigner Development image created successfully!

Now you can flash you image to a sd card with:
    sudo dd if=${DEVIMAGE_DIR}/${DEVIMAGE_NAME} of=<sdcard device> bs=16M conv=fsync && sudo sync
EOSUCCESS
	else
	    echo "Custom image already exists. Use --force to recreate it."
	fi
}
download_pios_image
check_sudo "$@"
create_image "$1"
