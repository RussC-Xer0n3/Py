<style>
/* The dropdown container */
.dropdown {
  float: left;
  overflow: hidden;
}
/* Dropdown button */
.dropdown .dropbtn {
  font-size: 16px;
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: inherit;
  font-family: inherit; /* Important for vertical align on mobile phones */
  margin: 0; /* Important for vertical align on mobile phones */
}
/* Add a red background color to navbar links on hover */
.navbar a:hover, .dropdown:hover .dropbtn {
    background-color: aliceblue;
    color: teal;
  }
  /* Dropdown content (hidden by default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: teal;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}
/* Links inside the dropdown */
.dropdown-content a {
  float: none;
  color: aliceblue;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}
/* Add a grey background color to dropdown links on hover */
.dropdown-content a:hover {
  background-color: #ddd;
}
/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {
  display: block;
}
</style>
<nav class="w3-container w3-teal w3-center w3-margin-top">
    <div class="dropdown">
        <button class="dropbtn">Projects
          <i class="fa fa-caret-down"></i>
        </button>
        <div class="dropdown-content">
          <a href="https://russc-xer0n3.github.io/Tumor-Probability">Tumor probability</a>
          <a href="https://russc-xer0n3.github.io/NetPCaC">NetPCaC</a>
          <a href="https://russc-xer0n3.github.io/LANDROVER">LANDROVER</a>
          <a href="https://russc-xer0n3.github.io/MAC">MAC Address</a>
          <a href="https://russc-xer0n3.github.io/SCRUD">SCRUD</a>
          <a href="https://russc-xer0n3.github.io/Remove">Code Syntax Removal</a>
          <a href="https://russc-xer0n3.github.io/PassGen">PassGen</a>
          <a href="https://russc-xer0n3.github.io/C_Shapes">C Programming Shapes</a>
          <a href="https://russc-xer0n3.github.io/Shapes---python">Python Shapes and space</a>
          <a href="https://russc-xer0n3.github.io/The-old-Fusion-Repository">Fusion?</a>
          <a href="https://russc-xer0n3.github.io/The-Russian-Wedding-Rings">The Russian Wedding Rings</a>
          <a href="https://russc-xer0n3.github.io/QBit-and-GParticulates">QBit and GParticulates</a>
          <a href="https://russc-xer0n3.github.io/Thyme-old">Thyme</a>
          <a href="https://russc-xer0n3.github.io/IP-Port">IP and Ports</a>
          <a href="https://russc-xer0n3.github.io/Xer0n3">Xer0n3</a>
          <a href="https://russc-xer0n3.github.io/ScrambledEggs">ScrambledEggs</a>
          <a href="https://russc-xer0n3.github.io/Py">Python Code</a>
        </div>
    </div>
    <br>
      <a href="https://www.facebook.com/profile.php?id=100075972987666"><i class="fa fa-facebook-official w3-hover-opacity"></i></a>
      <a href="https://www.instagram.com/russellclarke821"><i class="fa fa-instagram w3-hover-opacity"></i></a>
      <a href="https://www.pinterest.co.uk/russellclarke821/"><i class="fa fa-pinterest-p w3-hover-opacity"></i></a>
      <a href="https://twitter.com/Developing821"><i class="fa fa-twitter w3-hover-opacity"></i></a>
      <a href="https://www.linkedin.com/in/russell-clarke-09a1a5238"></a><i class="fa fa-linkedin w3-hover-opacity"></i>
      <br><a href="https://russc-xer0n3.github.io">My CV and additional information</a>
    <br>
</nav>
# Python Minified Projects
## Small scale projects to help learn and understand and solve real world scenarios 

### What's in the repo?
In the Py repository there are several unfinished projects which will be worked on or have hit a 'brick wall' in their progress; In example, the [ultrasoundgui_basic_1.0.py](https://github.com/RussC-Xer0n3/Py/blob/main/ultrasoundgui_basic_1.0.py) project.

The project is intended to convert an [HC-SR04 module](https://www.theengineeringprojects.com/2018/10/introduction-to-hc-sr04-ultrasonic-sensor.html) included with the [Freenove RFID raspberry PI starter kit](https://freenove.com/store.html) and their [subsequent tutorials](https://freenove.com/tutorial.html).

The aim is to convert from an ultrasound ranging device to a full ultrasound interface using the boiler plate code and expanding on it with an interface included.

Another program was written to print out the values for the grey scale and the values were added as string values to the string value 'grey' using a logic function.

### TKinter Grey Scale Values
```
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
```

### Issues faced
The issue we face now and why the project has stopped temporarily, is simply finding a way to get a live stream and image data represented to the interface.

```
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
```

### And so the issues faced are

- Get an image representation
- Get a live feed stream to the interface
- Get it displaying correctly and accurately on the interface

### To get started for your Raspberry Pi 3 B+ or 4

We need the Python Image Library (PIL) installed, numpy and OpenCV for one potential solution, you need TKinter and you need

## PIL (Python Image Library)

### uninstall PIL if installed
```
sudo pip uninstall pil
```

### download and compile the JPEG library
```
wget http://www.ijg.org/files/jpegsrc.v8c.tar.gz    
tar xvfz jpegsrc.v8c.tar.gz
cd jpeg-8c
./configure --enable-shared --prefix=$CONFIGURE_PREFIX
make
sudo make install
```

### link the libraries correctly - RASPBERRY PI ONLY
```
sudo ln -s /usr/lib/arm-linux-gnueabi/libjpeg.so /usr/lib
sudo ln -s /usr/lib/arm-linux-gnueabi/libfreetype.so /usr/lib
sudo ln -s /usr/lib/arm-linux-gnueabi/libz.so /usr/lib
```

### install rest of the libraries, as well as freetrype and zlib
```
sudo apt-get install libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev
```

### re-install PIL
```
sudo pip install pil
```

## OR TRY
```
sudo apt-get update
sudo apt-get install libjpeg-dev -y
sudo apt-get install zlib1g-dev -y
sudo apt-get install libfreetype6-dev -y
sudo apt-get install liblcms1-dev -y
sudo apt-get install libopenjp2-7 -y
sudo apt-get install libtiff5 -y
```

### and then the environment
```	
virtualenv -p python3 PillowEnv
```
```
source PillowEnv/bin/activate
```
```
pip install pillow
```

## TKinter
```
sudo apt-get install python-tk -y
```

## OpenCV

### Install OpenCV
```
sudo apt install cmake build-essential pkg-config git -y
```

### OpenCV dependencies
```
sudo apt install libjpeg-dev libtiff-dev libjasper-dev libpng-dev libwebp-dev libopenexr-dev -y && sudo apt install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libdc1394-22-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev -y
```

### OpenCV Interface packages
```
sudo apt install libgtk-3-dev libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5 -y && sudo apt install libatlas-base-dev liblapacke-dev gfortran -y && sudo apt install libhdf5-dev libhdf5-103 -y
```

## OpenCV compilation packages (Including Numpy) 
``` 
sudo apt install python3-dev python3-pip python3-numpy -y && sudo apt-get install libopencv-dev python3-opencv *opencv* -y
```

## OR 
[go to the link here and follow all the instructions to the T](https://robu.in/how-to-install-opencv-in-raspberry-pi/#:~:text=%20How%20to%20Install%20OpenCV%20in%20Raspberry%20Pi,no%20longer%20need%20to%20have%20such...%20More%20). 

## Installing Imageio
```
sudo pip install imageio
```

## CODE

### Foreword
Now we have the base files installed and the libraries we want to work with, a secondary more viable solution is potentially available in version 1.2. It makes used of a collaboration from H4KR alkasm [Alexander Reynolds](https://stackoverflow.com/users/5087436/alkasm), [Satyam Singh Niranjan](https://www.codespeedy.com/author/satyam_singh/) and the guys at [FreeNove](https://freenove.com/) since I wanted to try and improve their boilerplate code and give it some extra Oomph with and interface and live stream and turn it from ranging into Ultrasound. Kind of like the pregnancy ultrasound you see at Hospitals.

### The juicy bit, code
Not yet tested since it is 12 past midnight and I am tired.

```
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
```

# NevinsMcTwis.py
## Web Scraper

### Designed to be a scraper which is autonomous and can be used as a plugin

NevinsMcTwis.py is a project in it's infancy. The purpose of the project is to use the built-in functions of Beautiful Soup, Pandas and or Scrapy to autonomously run reccursive searches based on a single or a set of URL's and to be used as a plugin for other AI or autonomous systems .

### NevinsMcTwis.py
```
# TODO: Make this more intuitive and question the directory - see ~/csvout.py (it's broken btw).
# Check which directory we are in and change if set/required
def dircheck(path):
    # Check current working directory.
    retval = os.getcwd()
    # If equal to specified, notify.
    if retval == path:
        print "Current working directory %s" % retval
    elif retval != path:
        # Now change the directory if not equal.
        os.chdir( path )
    # Prompt the current / new (specified) working directory.
    print "Directory changed successfully %s" % retval
 
# start scraping with (everything including tags) definitions below
def scrape(url, y, x):
    log = []

    # open and read the url.
    r = urllib2.urlopen(url).read()
    soup = BeautifulSoup(r, "lxml" and "lxml-xml")

    # set the printing type.
    print type(soup.prettify()[y:x])

    # print from line 0 to line x = EOF
    content = type(soup.prettify()[y:x])
    log.append(content)

    #print log
    csv_writer(content, log, checker(logFile_name))
    log_parse(url, y, x, soup, r)


# TODO: 
# Seive and get all <script>'s / <script a>
# Seive through and remove all a into array (carefull this one will grow, details later).
# Seive through and grab keyword refs required / found as per req.
# For each keyword relevant to search criteria grab the ref, datatype, relevance
# ASSERTIONS, SANITISATIONS AND INSERTIONS.

def log_parse(url, y, x, s, r):
    # Lists to store the scraped data in
    names = []
    years = []
    imdb_ratings = []
    metascores = []
    votes = []
    links = []

    
    print type(s.prettify()[y:x])
    
    for link in s.find_all('a'):
        contents = link.get('href')
        links.append(contents)

    # Assistance 2: Extract data from individual movie container.
    for container in movie_containers: #Go to src

        # If the movie has Metascore, then extract:
        if container.find('div', class_ = 'ratings-metascore') is not None:

            # The name
            name = container.h3.a.text
            names.append(name)

            # The year
            year = container.h3.find('span', class_ = 'lister-item-year').text
            years.append(year)

            # The IMDB rating
            imdb = float(container.strong.text)
            imdb_ratings.append(imdb)

            # The Metascore
            m_score = container.find('span', class_ = 'metascore').text
            metascores.append(int(m_score))

            # The number of votes
            vote = container.find('span', attrs = {'name':'nv'})['data-value']
            votes.append(int(vote))

            check(names, years, imdb_ratings, metascores, votes, links)

def unique(url):
    response = get(url)         
    print(response.text[:1000])
    return response.text[:1000]
        
def check(n, y, r, meta, v, lnx):
    test_df = pd.DataFrame({'movie': n,
                       'year': y,
                       'imdb': r,
                       'metascore': meta,
                       'votes': v,
                       'links': lnx})
    print(test_df.info())
    test_df  # TODO: Pipe this to db. 

# TODO: As it goes deeper, learn, update terms.abs
def search_terms():
    #Set out the search terms in here and their syntactical analysis.abs
    terms = ["criminal", "firstly"]

    return terms

######################  Export to Excel CSV  ######################

    # Now that we have the data, it is time to save it. The Excel Comma Separated Format is a nice choice. 
    # It can be opened in Excel so you can see the data and process it easily. We have to imported
    # the Python csv module and the datetime module to get the record date. But we modify the 
    # saving section to save data row by row.

# First we check the filename and format is correct

def checker(logFile_name):
    # The pattern to match against.
    pattern = re.match(r'(.*\.)csv', logFile_name, re.M|re.I)
    # If a match is recorded, continue to execute the script.
    if pattern:
        f = logFile_name
        print ("setting export filename to "+logFile_name+".")
    else:
        print "logfile is not the correct file format or contains unaccepted characters, should be \"Examp1e.csv\"."
        exit()
    # Set the file name.
    return f

def csv_writer(c, l, f):      
    # open a csv file with append, so old data will not be erased
    with open(f, 'a') as csv_file:
        writer = csv.writer(csv_file)
        # The for loop
        for c in l:
            writer.writerow([c, datetime.now()]) # Changed from l to c. (check this is csv should have no carriage n)
    csv_file.close()
    print "Data gathered from "+url+" and can be found in "+logFile_name+"."

############################MAIN CODE AND NOTES############################

# call to function.
dircheck("/home/russell/Desktop/")

# set the url or add a list ['', '', ''] and so forth. (uncomment to use).
url = ['http://www.russellclarke.co.uk/', 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1']
#url = ['', '', '', '']
#url = {"", "", "", ""}

# Start from line number.
y = 0
# To ending line number.
x = 100000

# Set the logfile name and extension (should match the character pattern Example_2.csv)
logFile_name = "test.csv"

scrape(url, y, x)
```

# What else is in the repo?

### Other projects which have been completed are...
There are other projects in Py repository which were started and uploaded here which have since moved to another repository.

[MAC Daddy](https://github.com/RussC-Xer0n3/Py/blob/main/mac_daddy.py) and [ip](https://github.com/RussC-Xer0n3/Py/blob/main/ip.py) are two examples of minified projects which were moved to separate related repositories[ip here](https://github.com/RussC-Xer0n3/IP-Port) and [MAC here](https://github.com/RussC-Xer0n3/MAC).

### Check out
Why not check out [Shapes---python](https://github.com/RussC-Xer0n3/Shapes---python) whilst you are here, very interesting spacecraft code in there.
<head>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type">
    <meta charset="UTF-8">
    <meta name="description" content="Projects and Portfolio">
    <meta name="keywords" content="HTML, CSS, JavaScript, PHP, MySQLi, Python, Java, C, C++, C#, Time, Shapes">
    <meta name="author" content="Russell Clarke">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<footer class="w3-container w3-teal w3-center w3-margin-top">
  <p>Find me on social media.</p>
  <a href="https://www.facebook.com/profile.php?id=100075972987666"><i class="fa fa-facebook-official w3-hover-opacity"></i></a>
  <a href="https://www.instagram.com/russellclarke821"><i class="fa fa-instagram w3-hover-opacity"></i></a>
  <a href="https://www.pinterest.co.uk/russellclarke821/"><i class="fa fa-pinterest-p w3-hover-opacity"></i></a>
  <a href="https://twitter.com/Developing821"><i class="fa fa-twitter w3-hover-opacity"></i></a>
  <a href="https://www.linkedin.com/in/russell-clarke-09a1a5238"></a><i class="fa fa-linkedin w3-hover-opacity"></i>
  <p>Powered by <a href="https://www.w3schools.com/w3css/default.asp" target="_blank">w3.css</a></p>
</footer>
