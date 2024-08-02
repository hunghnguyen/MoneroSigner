default:
	true

resources:
	tools/compress_resources.py xmrsigner.resources src/xmrsigner/resources

clean:
	find src -name __pycache__ -exec rm -rf \{\} \;

patch:
	tools/increment_version.py --patch
	tools/tag_version.py

minor:
	tools/increment_version.py --minor
	tools/tag_version.py

major:
	tools/increment_version.py --major
	tools/tag_version.py

image:
	@echo Build PiOS image with XmrSigner for Development...
	tools/create_image_bookworm.sh
