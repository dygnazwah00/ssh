import picamera
print ("About to take a picture")
with picamera.PiCamera() as camera:
	camera.start_preview()
	camera.resolution = (1280, 720)
	camera.capture("/home/pi/Desktop/GROUP3/ssh/ssh.jpg")
	camera.stop_preview()
	print("picture taken.")
