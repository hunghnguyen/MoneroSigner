SSH_PRIVATE_KEY=${PWD}/xmrsigner_dev_ssh
SRC_DIR=${PWD}/src
DEV_DEVICE_IP=''

default:
	true

resources:
	@echo 'compress_resources...'
	tools/compress_resources.py xmrsigner.resources src/xmrsigner/resources

clean:
	@echo 'clean py cache files...'
	@find src -name __pycache__ -exec rm -rf \{\} \; >&2

version:
	grep VERSION src/xmrsigner/controller.py | awk -F'"' '{ print $2 }'

checksums: clean
	@echo 'generate sha256 checksums...'
	@find src -type f -exec sha256sum --tag {} \; > SHA256
	@find tools -type f -exec sha256sum --tag {} \; >> SHA256
	@find docs -type f -exec sha256sum --tag {} \; >> SHA256
	@sha256sum --tag requirements.txt >> SHA256
	@sha256sum --tag setup.py >> SHA256
	@sha256sum --tag Makefile >> SHA256
	@sha256sum --tag README.md >> SHA256
	@sha256sum --tag LICENSE.md >> SHA256
	@rm -f SHA256.sig
	@git add SHA256

sign: checksums
	@echo 'Sign the checksums...'
	@tools/sign.sh
	@cat SHA256 >> SHA256.sig
	@git add SHA256.sig

verify:
	@echo 'Verify source files...'
	@signify-openbsd -C -p xmrsigner.pub -x SHA256.sig | grep -v ': OK'
	@echo 'Source is verified!'

.increment-patch:
	@tools/increment_version.py --patch

patch: .increment-patch checksums sign version
	@tools/tag_version.py

.increment-minor:
	@tools/increment_version.py --minor

minor: .increment-minor checksums sign version
	@tools/tag_version.py

.increment-major:
	@tools/increment_version.py --major

major: .increment-major checksums sign version
	@tools/tag_version.py

image-clean:
	@echo 'Remove folder devimage...'
	@rm -rf devimage

image-bookworm:
	@echo 'Build PiOS (bookworm) image with XmrSigner for Development...'
	@tools/create_image_bookworm.sh

image-buster:
	@echo 'Build PiOS (buster) image with XmrSigner for Development...'
	@tools/create_image_bookworm.sh

unixtime:
	date +unixtime:%s?tz=%Z | qr

dev-device-ip:
	$(eval DEV_DEVICE_IP := $(shell tools/find_dev_device.sh))
	@if [ -z "$(DEV_DEVICE_IP)" ]; then \
		echo "DEV_DEVICE_IP is empty. Is the pi zero connected and up?"; \
		exit 1; \
	fi

dev-device-sync: dev-device-ip
	scp -r -i ${SSH_PRIVATE_KEY} ${SRC_DIR}/xmrsigner xmrsigner@${DEV_DEVICE_IP}:/opt/xmrsigner/src/

dev-device-shell: dev-device-ip
	ssh -i ${SSH_PRIVATE_KEY} xmrsigner@${DEV_DEVICE_IP}

dev-device-time-sync: dev-device-ip
	date +'%s %Z' | ssh -i ${SSH_PRIVATE_KEY} xmrsigner@${DEV_DEVICE_IP} 'read -r ts tz; sudo date -s @${ts}; echo $tz | sudo tee /etc/timezone; sudo dpkg-reconfigure -f noninteractive tzdata'
