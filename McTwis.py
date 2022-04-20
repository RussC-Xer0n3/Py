#!/usr/bin/python

#Generic beautiful soup DOM scraper

from bs4 import BeautifulSoup
from datetime import datetime
import re
import urllib2
import csv
import os

#   Scraping Techniques - module 1:

#   BeautifulSoup is simple and great for small-scale web scraping. But if you are interested in scraping 
#   data at a larger scale, you should consider using these other alternatives:

#   Scrapy, a powerful python scraping framework

#   Try to integrate your code with some public APIs. The efficiency of data retrieval is much higher than
#   scraping webpages. For example, take a look at Facebook Graph API, which can help you get hidden data 
#   which is not shown on Facebook webpages.

#   Consider using a database backend like MySQL to store your data when it gets too large.


# Check which directory we are in and change if set/required
def dircheck(log):
    path = log

    # Check current working directory.
    retval = os.getcwd()
    
    if retval == path:
        print "Current working directory %s" % retval
    elif retval != path:
        # Now change the directory
        os.chdir( path )

    # Prompt the current working directory.
    print "Directory changed successfully %s" % retval

# start scraping with definitions below
def scrape(url, y, x):
    log = []

    # open and read the url.
    r = urllib2.urlopen(url).read()
    soup = BeautifulSoup(r, 'html.parser')

    # set the printing type.
    print type(soup.prettify()[y:x])

    # print from line 0 to line x = EOF
    content = soup.prettify()[y:x]
    log.append(content)

    #print log
    csv_writer(content, log, checker(logFile_name))

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
        print 'logfile is not the correct file format or contains unaccepted characters, should be \"Examp1e.csv\" .'
        exit()
    # Set the file name.
    return f

def csv_writer(c, l, f):      
    # open a csv file with append, so old data will not be erased
    with open(f, 'a') as csv_file:
        writer = csv.writer(csv_file)
        # The for loop
        for c in l:
            writer.writerow([l, datetime.now()])
    csv_file.close()
    print "Data gathered from "+url+" and can be found in "+logFile_name+"."

############################MAIN CODE############################

# call to function.
dircheck("/home/russia/Desktop/Scraper")

# set the url or add a list ['', '', ''] and so forth. (uncomment to use).
url = 'http://www.russellclarke.co.uk/'
#url = ['', '', '', '']

# Start from line number.
y = 0
# To ending line number.
x = 10000

# Set the logfile name and extension (should match the character pattern Example_2.csv)
logFile_name = "random.csv"

scrape(url, y, x)

#BeautifulSoup(YOUR_MARKUP, "lxml")

#  markup_type=markup_type))