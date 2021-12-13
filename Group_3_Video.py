import picamera
from time import sleep

with picamera.Picamera() as camera:
     camera.start_recording("video.h264")
     sleep(5)
     camera.stop_recording()
