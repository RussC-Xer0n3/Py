#! /usr/bin/env/ python3

# CONSIDERATIONS - 30 degrees, unintended feedback, conical, image readings

##############################################################################
    # In combination with code from the dev team at FreeNove
    # The code herin is intended to generate an ultrasound
    # image of the OBJECTS IN FRONT OF THE HC-SR04. It makes use
    # of the source code at the github repository located
    # https://github.com/Freenove/Freenove_RFID_Starter_Kit_for_Raspberry_Pi.git 
    # In combination of FreeNove Code in directory
    # Freenove_RFID_Starter_Kit_for_Raspberry_Pi-master\Code\Python_Code\
    # \23.1.1_UltrasonicRanging
    # Additional author is Xer0ne and referred herein
    # Mike McGrath 'Python in easy steps'
##############################################################################
'''
https://www.rfcafe.com/references/electrical/image-frequency.htm - accessed 15/07/21

    f = fLO - fRF

    f = FImage - fLO = fRF + 2fIF (IF Intended frequencies)

    https://en.wikipedia.org/wiki/Speed_of_sound 343 m/s

    ###########################################################
    # PROPOSED MODIFICATION -> f = fRF - fLO                  #
    # because the local oscilator will be the device being    #
    # monitored makes life a little easier since we will      #
    # know which frequency is being used as the monitor       #
    # thus we should subtract the LO from that data being     #
    # received and it will permit us to see the differentials #
    # either way the algorithm does the same thing however    #
    # in the interest of ease seems simpler to subtract the   #
    # frequency emitted out of the device with modulation     #
    # from the constant expected from the HC-SR04 device      #
    ###########################################################
'''
import tkinter
from tkinter import *
import imageio
from PIL import Image, ImageTk
window = Tk()
window.title("UltraSound GUI")
import math
#import RPi.GPIO as GPIO
import time
import numpy as np
import cv2 # OpenCV

txPin=16 #tx 'trig'
rxPin=18 #rx 'echo'

'''
    220 (original linear) - define the maximum measuring 
    distance, unit: cm (currently the cubic area of the 
    self built faraday cage without subtraction of it's 
    internal contents)

    MAX_DISTANCE*60 calculate timeout (seconds 
    because sound is appx 340 meters per second) 
    according to the maximum measuring distance

    Could use spherical circumference, cylindrical, wombal, etc
'''

MAX_DISTANCE= math.pow(50, 3) # cm cubed - for homemade faraday - 10.5*23*25.5

timeOut=MAX_DISTANCE*0.6

'''
encode data from ultrasound to a video encoder in preparation for displaying via stream()
    Modded from h4kr Alkasm reynoldsalexander.com Alexander Reynolds 
    https://stackoverflow.com/questions/51914683/how-to-make-video-from-an-updating-numpy-array-in-python
'''
# initialize water image
height = 400
width = 400
depth = MAX_DISTANCE*height*width
water_depth = np.zeros((depth), dtype=float)

# initialize video writer
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
fps = 30
video_filename = 'output.avi'
out = cv2.VideoWriter(video_filename, fourcc, fps, (depth))

# new frame after each addition of water
for i in range(10):
    image = fImage
    for item in image:
        water_depth[item[0.000000], item[1.000000]] += 0.003921
        #add this array to the video
        gray = cv2.normalize(water_depth, None, 255, 0, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        gray_3c = cv2.merge([gray, gray, gray])
        out.write(gray_3c)

'''
stream()
    stream the encoded video live to the user interface
    From Satyam Singh Narajan - https://www.codespeedy.com/video-streaming-in-tkinter-with-python/
'''
def stream():
    try:
        image = video.get_next_data()
        frame_image = Image.fromarray(image)
        frame_image=ImageTk.PhotoImage(frame_image)
        l1.config(image=frame_image)
        l1.image = frame_image
        l1.after(delay, lambda: stream())
    except:
        video.close()
        return   

frame=Frame(window)
image.pack(side=LEFT,padx=10,pady=10)
frame.pack()

stream_name = "output.avi"
video = imageio.get_reader(stream_name)
delay = int(ultrasound.LO / video.get_meta_data()['fps'])

'''
Buttons for commands just type the name of the function no ()'s
'''
start_ultra=Button(window,text="Start ultrasound", command=__main__)
start_ultra.pack(side=RIGHT,padx=10)

stop_ultra=Button(window,text="Stop ultrasound", command=KeyboardInterrupt )
stop_ultra.pack(side=RIGHT,padx=10)

# exit
btn=Button(window,text="Exit", command=exit)
btn.pack(side=RIGHT,padx=10)

# contiguous
window.mainloop()

'''
ultrasound()
    designed to modify the capabilities of the HC-SR04 module to produce 
    ultrasound as opposed to sonar

    PSEUDO  tx at 2MHz for example using modified source code is values 1.000000
        wait for the rx and subtract tx from rx where anything not 2MHz is > than 0.000000 
        feed data to image_index method for processing and rendering
        hope that it works and looks good!! - !!!!not yet complete or verified!!!!!
'''
def ultrasound(distance,pulseTime):  
    RF = pulseIn(rxPin,GPIO.HIGH,timeOut)
    LO = ((distance / pulseTime) - RF)
    fImage = LO - MAX_DISTANCE
    return fImage

'''
    ######################    MODDIFIED    #################################
    # Filename    : UltrasonicRanging.py
    # Description : Get distance via UltrasonicRanging sensor - MODDED
    # author      : www.freenove.com & Xer0n3
    # modification: 2019/12/28
    ########################################################################
'''
def pulseIn(pin,level,timeOut): # obtain pulse time of a pin under timeOut
    t0 = time.time()
    
    while(GPIO.input(pin) != level):
    
        if((time.time()-t0) > timeOut * 0.000001):
            return 0
    
    t0 = time.time()
    
    while(GPIO.input(pin) == level):
    
        if((time.time() - t0) > timeOut * 0.000001):
            return 0
    
    pulseTime = (time.time() - t0) * 1000000
    
    return pulseTime

'''
getSonar()
    get the measurement results of ultrasonic module, with unit: cm
'''
def getSonar():
    GPIO.output(txPin,GPIO.HIGH) # make trigPin output 10us HIGH level 
    time.sleep(0.00001) # 10us
    GPIO.output(txPin,GPIO.LOW) # make trigPin output LOW level
    pingTime = pulseIn(rxPin,GPIO.HIGH,timeOut) # read plus time of echoPin
    distance = pingTime * 343.0 / MAX_DISTANCE / 10000.000000 # calculate distance with sound speed 340m/s 
    return distance

'''
setup()
    setup the module for data receipt
'''
def setup():
    GPIO.setmode(GPIO.BOARD) # use PHYSICAL GPIO Numbering
    GPIO.setup(txPin,GPIO.OUT) # set trigPin to OUTPUT mode
    GPIO.setup(rxPin,GPIO.IN) # set echoPin to INPUT mode

'''
loop()
    loop the methods therein until timer count lapsed or system interupt
'''
def loop():
    while(True):
        distance = getSonar()   # get distance
        shadeindex(distance)    # print ("The distance is : %.2f cm"%(distance))
        time.sleep(0.1) # originally 1 second now down to 10 ms

'''
__main__
    main method call from external
'''

if __name__ == '__main__': # Program entrance
    setup()
    ultrasound()
    stream()
    try:
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        # close out the video writer
        out.release()
        GPIO.cleanup() # release GPIO resource