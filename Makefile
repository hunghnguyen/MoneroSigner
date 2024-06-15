default:
	true

resources:
	tools/compress_resources.py xmrsigner.resources src/xmrsigner/resources

clean:
	find src -name __pycache__ -exec rm -rf \{\} \;
