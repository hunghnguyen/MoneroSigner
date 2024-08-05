#!/bin/bash
OWN_IP=$(ip address | grep enx | sed -E 's/[0-9]+: ([a-z0-9]+): <.*$/\1/' | sed -E 's/\ *inet\ ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\/.*$/\1/' | tail -n1)
if [ -z "$OWN_IP" ]
then
    exit -1
fi
# echo "Own IP: $OWN_IP" >&2
IFS='.' read -r -a IP_PARTS <<< "$OWN_IP"
RANGE="${IP_PARTS[0]}.${IP_PARTS[1]}.${IP_PARTS[2]}."
FIRST=1
for ((i=1; i<=254; i++)); do
    if [ $i -ne "${IP_PARTS[3]}" ]; then
	if [ $FIRST -eq 1 ]; then
	    RANGE+="$i"
	    FIRST=0
	else
	    RANGE+=",$i"
	fi
    fi
done
# echo "IP Range: $RANGE" >&2
PI_ZERO_IP=$(nmap -oG -  -p22 -n --open $RANGE | grep ssh | awk -F' ' '{ print $2 }')
# echo "Pi zero: $PI_ZERO_IP" >&2
echo $PI_ZERO_IP
