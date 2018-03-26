import cv2
import time
import cfg2
from picamera.array import PiRGBArray


#CvCam class Takes and Image from the camera and gives it to the Vehicle
class CvCam(object):
    
    def __init__(self, camera, rawCapture):
        self.camera=camera
        self.rawCapture=rawCapture
        self.frame=None
        self.running=True
        camera.start_recording('foo.h264')
   
    def run(self):
        if self.running==True:
            self.rawCapture=PiRGBArray(self.camera, size=cfg2.Cam_Resolution)
            self.camera.capture(self.rawCapture, format="bgr",use_video_port=True)
            self.frame=self.rawCapture.array  
            return self.frame
    
    def shutdown(self):
        self.camera.stop_recording()
        self.running=False
        time.sleep(1.5)     
        self.camera.close()
        time.sleep(1.5)

#ImageConvandFilter Class imports the image and 1) converts it from BGR to HSV
#2) searches the image for pixels within a color range found in cfg2.py
#3) Filters the image through dilation and erotion
#4) Finds largest blob with findContours()
#5) Returns the pixel location x,y and pixel radius of circle around blob        
class ImageConvandFilter(object):
    
    def __init__(self):
        self.loopnum=1
        self.running=True        
        self.lowerColorSearch=None
        self.upperColorSearch=None
    
        
    def run(self,image):
        if self.running==True:
            if image is not None:
                hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #cvt to HSV 
                mask = cv2.inRange(hsv, cfg2.currentColor_lower, cfg2.currentColor_upper)
                mask = cv2.erode(mask, None, iterations = 4) #erode away the white
                mask = cv2.dilate(mask, None, iterations = 4) #dilates the white
                cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
                if len(cnts) > 0: #If we found at least one blob
                    c=max(cnts,key=cv2.contourArea)
                    ((x, y), Current_radius) = cv2.minEnclosingCircle(c) 
                    return x,y,Current_radius
                else:
                    return None
            else:
                return None
        
    def shutdown(self):
        self.running=False
