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
