# Authors: Ian Liu, Nick Garrett, Krishna Naik, Ruben Chan
# Project Code for MAE 198 Winter 2018, Team 1
# Code uses the DonkeyCar framework to track and drive to a green and then return
# to base, which is designated by a second color orange.
# Dependencies: FetchFunctionsModularized.py, CvCam1.py, cfg2.py

# This code adds five parts to the Donkeycar framework vehicle.
# Part 1: CvCam1 - captures an image using a mounted Camera and the PiCamera command
# Part 2: ImageConvandFilter - Take the image and searches it for a color then
#   applies a mask and filtering to isolate the image. Returns the pixel x,y coordinates
#   and the pixel radius of a circle that encloses the ball
#Part 3: Controller - Determines the PWM values to send to the ESC. For Throtttle
#   uses PI control
#Part 4,5: PWMsender - Parts that send values to the ESC.

from donkeycar.vehicle import Vehicle
from picamera.array import PiRGBArray
from picamera import PiCamera
from donkeycar.parts.actuator import PCA9685
import time
import CvCam1
import FetchFunctionsModularized as FF
import cfg2

#Setup Vehicle, PWM senders, and Camera
V=Vehicle()
steering_controller = PCA9685(cfg2.Steering_Channel)
throttle_controller = PCA9685(cfg2.Throttle_Channel)

camera=PiCamera()
camera.resolution=cfg2.Cam_Resolution
camera.framerate = cfg2.Cam_FrameRate
rawCapture=PiRGBArray(camera, size=cfg2.Cam_Resolution)


print('Warming Cam...')
time.sleep(.5)
print('Camera Warmed')

#Add parts to the Donkeycar Vehicle
cam=CvCam1.CvCam(camera, rawCapture)
V.add(cam, outputs=["camera/image"],threaded=False)
print('Added Camera Part')

filterImage=CvCam1.ImageConvandFilter()
V.add(filterImage, inputs=["camera/image"], outputs=["x","y","Current_radius"],threaded=False)
print('Added Filtering Part')

Controller=FF.Controller()
V.add(Controller,inputs=["x","y","Current_radius"],outputs=["PWM_Steering","PWM_Throttle"], threaded=False)
print('Added Controller Part')

SteeringPWMSender=FF.SteeringPWMSender(steering_controller)
ThrottlePWMSender=FF.ThrottlePWMSender(throttle_controller)
V.add(SteeringPWMSender,inputs=["PWM_Steering"],threaded=False)
V.add(ThrottlePWMSender,inputs=["PWM_Throttle"],threaded=False)
print('Added PWMSending Parts')

#Start the Vehicle
V.start()
