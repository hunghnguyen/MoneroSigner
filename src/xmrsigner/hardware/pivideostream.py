try:
    import picamera2
    from xmrsigner.hardware.picamera2 import PiVideoStream
    print('=> video backend: picamera2')
except Exception:
    import picamera
    from xmrsigner.hardware.picamera import PiVideoStream
    print('=> video backend: picamera')
