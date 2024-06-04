default:
	true

resources:
	tools/compress_resources.py seedsigner.resources src/seedsigner/resources

clean:
	find src -name __pycache__ -exec rm -rf \{\} \;
