#!/bin/bash

DEVIMAGE_DIR=$PWD/devimage
DEVIMAGE_NAME=xmrsigner-dev.img
DEVIMAGE_MOUNT=/mnt/xmrsignerdev
PIOS_LITE_URL=https://downloads.raspberrypi.org/raspios_lite_armhf/images/

set -e

# Function to modify the image
modify_image() {
    LOOP_DEVICE=$(losetup -Pf --show $DEVIMAGE_DIR/$DEVIMAGE_NAME)
    
    # Mount boot and root partitions
    mount "${LOOP_DEVICE}p1" $DEVIMAGE_MOUNT
    mount "${LOOP_DEVICE}p2" $DEVIMAGE_MOUNT

    # Enable USB OTG and SPI
    echo "dtoverlay=dwc2" >> $DEVIMAGE_MOUNT/boot/config.txt
    echo "dtoverlay=spi0-2cs" >> $DEVIMAGE_MOUNT/boot/config.txt
    sed -i 's/rootwait/rootwait modules-load=dwc2,g_ether/' $DEVIMAGE_MOUNT/boot/cmdline.txt

    # Enable SSH
    touch $DEVIMAGE_MOUNT/boot/ssh

    # Create firstboot.sh script
    cat << 'EOFB' > $DEVIMAGE_MOUNT/boot/firstboot.sh
#!/bin/bash

# Setup USB Ethernet gadget
echo "dtoverlay=dwc2" >> /boot/config.txt
echo "g_ether" >> /etc/modules

# Setup network configuration
cat << EOF > /etc/dhcpcd.conf
# USB Ethernet configuration
interface usb0
fallback static_usb0

# Static fallback configuration for usb0
profile static_usb0
static ip_address=10.42.0.100/24
static routers=10.42.0.1
static domain_name_servers=8.8.8.8

# WiFi AP configuration
interface wlan0
static ip_address=192.168.4.1/24
nohook wpa_supplicant
EOF

# Setup WiFi AP using pre-installed hostapd
cat << EOF > /etc/hostapd/hostapd.conf
interface=wlan0
driver=nl80211
ssid=XmrSigner
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=XmrSigner
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
EOF

echo 'DAEMON_CONF="/etc/hostapd/hostapd.conf"' >> /etc/default/hostapd
systemctl enable hostapd

# Configure DHCP server for WiFi AP using pre-installed dnsmasq
cat << EOF > /etc/dnsmasq.conf
interface=wlan0
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
EOF

systemctl enable dnsmasq

# Enable IP forwarding
echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf
sysctl -p

# Setup NAT for internet sharing
iptables -t nat -A POSTROUTING -o usb0 -j MASQUERADE
iptables -A FORWARD -i usb0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i wlan0 -o usb0 -j ACCEPT

# Save iptables rules
iptables-save > /etc/iptables.ipv4.nat

# Restore iptables rules on boot
echo "iptables-restore < /etc/iptables.ipv4.nat" >> /etc/rc.local

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
EOFB

    # Make the script executable
    chmod +x $DEVIMAGE_MOUNT/boot/firstboot.sh

    # Add execution of firstboot.sh to rc.local
    sed -i '/exit 0/i /boot/firstboot.sh' $DEVIMAGE_MOUNT/etc/rc.local

    # Unmount the image
    umount $DEVIMAGE_MOUNT
    losetup -d "$LOOP_DEVICE"
}

# Create and modify the image
if [ ! -f "$DEVIMAGE_DIR/$DEVIMAGE_NAME" ] || [ "$1" == "--force" ]; then
    cp $DEVIMAGE_DIR/raspios-lite.img $DEVIMAGE_DIR/$DEVIMAGE_NAME
    modify_image
    echo "Custom Raspberry Pi OS Lite image created successfully!"
else
    echo "Custom image already exists. Use --force to recreate it."
fi
