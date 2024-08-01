#!/bin/bash

DEVIMAGE_DIR=$PWD/devimage
DEVIMAGE_NAME=xmrsigner-dev.img
DEVIMAGE_MOUNT=/mnt/xmrsignerdev
PIOS_LITE_URL=https://downloads.raspberrypi.org/raspios_lite_armhf/images/

set -e

# Function to modify the image
modify_image() {
    LOOP_DEVICE=$(sudo losetup -Pf --show $DEVIMAGE_DIR/$DEVIMAGE_NAME)
    
    # Mount boot partition
    sudo mount "${LOOP_DEVICE}p1" $DEVIMAGE_MOUNT

    # Enable USB OTG
    echo "dtoverlay=dwc2" | sudo tee -a $DEVIMAGE_MOUNT/config.txt
    sudo sed -i 's/rootwait/rootwait modules-load=dwc2,g_ether/' $DEVIMAGE_MOUNT/cmdline.txt

    # Enable SSH
    sudo touch $DEVIMAGE_MOUNT/ssh

    # Create firstboot.sh script
    cat << 'EOF' | sudo tee $DEVIMAGE_MOUNT/firstboot.sh
#!/bin/bash

# Setup network configuration
cat << NETCONF > /etc/dhcpcd.conf
interface usb0
fallback static_usb0

define static_usb0
static ip_address=10.42.0.100/24
NETCONF

# Setup WiFi AP
apt-get update
apt-get install -y hostapd dnsmasq
cat << APCONF > /etc/hostapd/hostapd.conf
interface=wlan0
ssid=XmrSigner
wpa_passphrase=XmrSigner
hw_mode=g
channel=7
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
APCONF

echo 'DAEMON_CONF="/etc/hostapd/hostapd.conf"' >> /etc/default/hostapd

# Enable SSH daemon
systemctl enable ssh

# Add user and group xmrsigner:xmrsigner
useradd -m -G sudo xmrsigner
echo "xmrsigner:XmrSigner" | chpasswd

# Add public SSH key for xmrsigner
mkdir -p /home/xmrsigner/.ssh
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOehLkdqEEaaXBrv2ooTE92+jbC/b3Wrvp+R3b9HnSS9" > /home/xmrsigner/.ssh/authorized_keys
chown -R xmrsigner:xmrsigner /home/xmrsigner/.ssh
chmod 700 /home/xmrsigner/.ssh
chmod 600 /home/xmrsigner/.ssh/authorized_keys

# Remove this script and its execution from rc.local
sed -i '/firstboot/d' /etc/rc.local
rm /boot/firstboot.sh

# Reboot to apply changes
reboot
EOF

    # Make the script executable
    sudo chmod +x $DEVIMAGE_MOUNT/firstboot.sh

    # Add execution of firstboot.sh to rc.local
    sudo sed -i '/exit 0/i /boot/firstboot.sh' $DEVIMAGE_MOUNT/cmdline.txt

    # Unmount the image
    sudo umount $DEVIMAGE_MOUNT
    sudo losetup -d "$LOOP_DEVICE"
}

# ... [rest of the script remains the same] ...

# Create and modify the image
if [ ! -f $DEVIMAGE_DIR/$DEVIMAGE_NAME ] || [ "$1" == "--force" ]; then
    cp $DEVIMAGE_DIR/raspios-lite.img $DEVIMAGE_DIR/$DEVIMAGE_NAME
    modify_image
    echo "Custom Raspberry Pi OS Lite image created successfully!"
else
    echo "Custom image already exists. Use --force to recreate it."
fi
