import picamera

print ("Ready.")
with picamera.Picamera as camera:
     camera.start_preview()
     camera.resolution = (1280, 720)
     camera.capture("")
     print("Done Taking Picture.")
