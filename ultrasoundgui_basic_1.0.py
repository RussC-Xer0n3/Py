#! /usr/bin/env/ python3

# CONSIDERATIONS - 30 degrees, unintended feedback, conical, image readings

##############################################################################
    # In combination with code from the dev team at FreeNove
    # The code herin is intended to generate an ultrasound
    # image of the contents of a self built faraday cage for
    # the analytics of signal activity within the cage. Yet
    # to be completed for all intents of purpose. It makes use
    # of the source code at the github repository located
    # https://github.com/Freenove/Freenove_RFID_Starter_Kit_for_Raspberry_Pi.git 
    # In combination of FreeNove Code in directory
    # Freenove_RFID_Starter_Kit_for_Raspberry_Pi-master\Code\Python_Code\
    # \23.1.1_UltrasonicRanging
    # Additional author is Xer0ne and referred herein
    # Mike McGrath 'Python in easy steps'
##############################################################################

import tkinter
from tkinter import *
import imageio
from PIL import Image, ImageTk
window = Tk()
window.title("UltraSound GUI")
import math
#import RPi.GPIO as GPIO
import time

'''
    Get and store variables related to float data fromultrasound and assign
    to key - value pairs to allocate key as string to string 'grey' for image
    representation of data in tkinter interface
'''

dict = {'1:0.000000',
'2:0.010204',
'3:0.020408',
'4:0.030612',
'5:0.040816',
'6:0.051020',
'7:0.061224',
'8:0.071429',
'9:0.081633',
'10:0.091837',
'11:0.102041',
'12:0.112245',
'13:0.122449',
'14:0.132653',
'15:0.142857',
'16:0.153061',
'17:0.163265',
'18:0.173469',
'19:0.183673',
'20:0.193878',
'21:0.204082',
'22:0.214286',
'23:0.224490',
'24:0.234694',
'25:0.244898',
'26:0.255102',
'27:0.265306',
'28:0.275510',
'29:0.285714',
'30:0.295918',
'31:0.306122',
'32:0.316327',
'33:0.326531',
'34:0.336735',
'35:0.346939',
'36:0.357143',
'37:0.367347',
'38:0.377551',
'39:0.387755',
'40:0.397959',
'41:0.408163',
'42:0.418367',
'43:0.428571',
'44:0.438776',
'45:0.448980',
'46:0.459184',
'47:0.469388',
'48:0.479592',
'49:0.489796',
'50:0.500000',
'51:0.510204',
'52:0.520408',
'53:0.530612',
'54:0.540816',
'55:0.551020',
'56:0.561225',
'57:0.571429',
'58:0.581633',
'59:0.591837',
'60:0.602041',
'61:0.612245',
'62:0.622449',
'63:0.632653',
'64:0.642857',
'65:0.653061',
'66:0.663265',
'67:0.673469',
'68:0.683673',
'69:0.693878',
'70:0.704082',
'71:0.714286',
'72:0.724490',
'73:0.734694',
'74:0.744898',
'75:0.755102',
'76:0.765306',
'77:0.775510',
'78:0.785714',
'79:0.795918',
'80:0.806122',
'81:0.816327',
'82:0.826531',
'83:0.836735',
'84:0.846939',
'85:0.857143',
'86:0.867347',
'87:0.877551',
'88:0.887755',
'89:0.897959',
'90:0.908163',
'91:0.918367',
'92:0.928571',
'93:0.938776',
'94:0.948980',
'95:0.959184',
'96:0.969388',
'97:0.979592',
'98:0.989796',
'99:1.000000'}


txPin=16 #tx 'trig'
rxPin=18 #rx 'echo'

'''
    220 (original linear) - define the maximum measuring 
    distance, unit: cm (currently the cubic area of the 
    self built faraday cage without subtraction of it's 
    internal contents)


    # Could use spherical circumference, cylindrical, wombal, etc
'''

MAX_DISTANCE= math.pow(50, 3) # cm cubed - for homemade faraday - 10.5*23*25.5
final = image_index()
'''
    MAX_DISTANCE*60 calculate timeout (seconds 
    because sound is appx 340 meters per second) 
    according to the maximum measuring distance
'''

timeOut=MAX_DISTANCE*0.6

####################
# Window shabizzle #
####################

# From Satyam Singh Narajan - https://www.codespeedy.com/video-streaming-in-tkinter-with-python/
image = final.get_next_data()

def stream():
    try:
        frame_image = image_fromarray(image)
        frame_image = ImageTk.PhotoImage(frame_image)
        l1.config(image=frame_image)
        l1.image = (frame_image)
        l1.after(delay,lambda: stream())
    except:
        KeyboardInterrupt
        return

frame=Frame(window)
image.pack(side=LEFT,padx=10,pady=10)
frame.pack()

stream_name = final
video = imageio.get_reader(stream_name)
delay = int(ultrasound.LO / video.get_meta_data()['fps'])
stream()

'''
BUttons
    for commands just type the name of the function no ()'s
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

####################
# Window shabizzle #
#       END        #
####################

'''
shade_index()
    Method is supposed to divide the values gathered from the ultrasound method
    into a pool of 99 'pockets' associated with the color index for tkinter
    then feed each index into the canvas (view port) at relevant points realtime via image_index()

    The code below is intended to receive the data fed back from the
    ultrasound() method and generate an image not dissimilar to ultrasound
    in maternity wards. It's eventual intended purpose is to 'see' signals
    from a separate piece of aparatus in the project.
    Author - Xer0ne Et. Al
'''

def shade_index(fImage):
    
    # see: http://www.science.smith.edu/dftwiki/index.php/File:TkInterColorCharts.png
    
    i = 1
    values = ""
    v = fImage
    
    # syntax reference for decrement and increment
    # Mike McGrath & https://www.tutorialspoint.com/increment-and-decrement-operators-in-python

    for key,value in dict.items():
        
        gray = "gray"
        values = ""

        if ((v / 2) < (dict.items(value) / 2)):
    
            values = gray + str(dict.items(key-1))
            return values
    
        elif (v == dict.items(value)):
    
            values = gray + str(dict.items(key))
            return values

        elif ((v / 2) > (dict.items(value) / 2)):
    
            values = gray + str(dict.items(key+1))
            return values    

'''
image_index()
    from central pixel, radiate diagonally in 4 directions to edge of canvas
    since frequencies are received radially, makes sense to replicate from 
    a central point and project the data outwards on the canvas
'''

def image_index(values):

    i = 79998 #central 'pixel' of image
    g = values #gray1 for example
    can = Canvas(window,width = 400,height = 400) #canvas of pixels
    final = 0

    for i in pow(can, 2):
        
        data = g * pow(i, 4)
        can.create_image(data)
        return

'''
https://www.rfcafe.com/references/electrical/image-frequency.htm - accessed 15/07/21

    formula for frequency subtraction on ultrasonic sound frequencies -
    Equations label the lines to indicate the origin of each product. 
    Notice that a negative image of the "positive" frequencies is shown 
    to the left of 0 Hz (DC). Negative frequencies are often used in 
    order to make the equations easier to visualize (substitute fLO=-fLO and 
    FImage=-FImage). It prevents the equations from needing to indicate 
    subtracting a negative number, which is the equivalent of addition.

    The fundamental equation for calculating the resulting frequencies from the 
    presence of a local oscillator (our rf we want to "see") (fLO), the intended RF signal (our ultra sound) (fRF), and the 
    unintended image (FImage), are as follows:

    f = fLO - fRF

    f = FImage - fLO = fRF + 2fIF (IF Intended frequencies)

    Ok, then how do you prevent the image frequency from ending up in the IF band?
    There are two methods that can be used alone or together, depending on your 
    system requirements. The first is to use a filter to prevent the image frequency 
    from ever getting to the mixer input. The other is to use a mixer whose 
    construction is such that a phasing technique is used to cancel out the image 
    frequency (an image-reject mixer).

    PROPOSED MODDIFICATION - NOTES
    Whilst we have the oscilator or frequencies which will be changing regularly
    we want to be able to get an image of what we want to see;

    since we already know difinitively which frequency we are emitting on the ultrasonic
    we can subtract the received information from our known rf returning the 'disruption'
    to what we are supposed to see thus returning the image.

    example - we set the us to 2hz we are expecting to see 2hz rx after a tx
    when subtracting 2hz from what is received the anomolies recorded in float values
    should be what has interfered with that frequency depending on penetration values and
    whether those disruptions effect higher pitched ranges not dissimilar to sonar.

    furthermore, since the frequencies being measured are or may be variable , it
    would make sense to subtract the rx from the tx yielding the interference as an image.

    ultimately attempting to yield ultrasound effect into gui from ultrasound module HC-SR04 
    may require longer or shorter wait times before each tx such as 0.1 sec because 340m/s is
    approx sound velocity. Modded in src code.

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
    LO = ((distance / pulseTime) - RF) #REVISIT HERE
    fImage = LO - MAX_DISTANCE
    return fIimage

############
# MODIFIED #
############
'''
    ########################################################################
    # Filename    : UltrasonicRanging.py
    # Description : Get distance via UltrasonicRanging sensor - MODDED
    # auther      : www.freenove.com
    # modification: 2019/12/28
    ########################################################################
    imports and var malloc at the top of the file
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
    print ('Program is starting...')
    setup()
    ultrasound()
    try:
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        GPIO.cleanup() # release GPIO resource
