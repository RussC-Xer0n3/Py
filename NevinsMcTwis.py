#!/usr/bin/python

# PROJECT ON HOLD FOR NOW #

# This needs to be completely objective and work with minimal 
# effort and config at best a list or URLs and some search terms.
# Docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# Source 1: http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html
# Source 2: https://www.dataquest.io/blog/web-scraping-beautifulsoup/
# Source 3: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# Source 4: https://stackoverflow.com/questions/8841205/insert-tab-delimited-values-into-database

# Theory 1: https://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input - click booooomb.

#Generic beautiful soup DOM scraper
# TODO: Step 1. Read the csv module. http://docs.python.org/library/csv.html. This does what you want.
# TODO: Step 2. Read up on context managers, also.
# TODO: Make this parse through and acquire desired info objectively.
# TODO: Call CSV reader and parse? Arrays?
# TODO: Front end GUI eventually?
# TODO: Definitely finish this as it will be very fit for purpose eventually.

import pandas as pd
from bs4 import BeautifulSoup
from requests import get

from datetime import datetime
import re
import urllib2
import csv
import os
#import subzero #- something else for later

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

'''

#   BeautifulSoup is simple and great for small-scale web scraping. But if you are interested in scraping 
#   data at a larger scale, you should consider using these other alternatives:

#   Scrapy, a powerful python scraping framework

#   Try to integrate your code with some public APIs. The efficiency of data retrieval is much higher than
#   scraping webpages. For example, take a look at Facebook Graph API, which can help you get hidden data 
#   which is not shown on Facebook webpages.

#   Consider using a database backend like MySQL to store your data when it gets too large.

#for the parsegroup(pg) in list_of_urls:

# Setup the terms required for searching as a list / array
# terms = ["price", "value", "cost"]
# Query the search terms in the scraper later on.
# lookFor_Terms = re.search(r'(*.)', terms, re.M|re.I|re.U)

# with open("char.txt") as si:
# Look for URLs which have data that matches a set
# lookFor_Cites = re.search(r'http://()\.(*.\.)(*.\.)', sitedata, re.M|re.I|re.U)

# all of the elements that are within div tags and are also members of class "ec_statements."
# letters = soup.find_all("div", class_="ec_statements")

# Take out the <div>(Tag) of what we're searching for (attributes and name) and get its value
# name_box = soup.find('h1', attrs={'class': 'query'})
# name = name_box.text.strip() # strip() is used to remove starting and trailing

# HREF's - firstly we need to get the list of urls or the urls from a file.

soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

for link in soup.find_all('a'):
    hrefs = (link.get('href'))
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie

# Text
print(soup.get_text())

# Tags
soup.p #<p>some stuff</p>
soup.p.class #gets the class of the p tags also note: can add elements and tags together

# To parse a document, pass it into the BeautifulSoup constructor. 
# You can pass in a string or an open filehandle:

with open("index.html") as f:
    soup = BeautifulSoup(f)

import sys and csv
filename = input('Enter a file name: ')
reader = csv.reader(open(sys.argv[0], "filename"))
for row in reader:
    print row

#print link.next_sibling
#print link.next_element
    
#for heading in soup.find_all(re.compile("^h[1-6]")):
    #print(heading.name + ' ' + heading.text.strip())
    #gaff = soup.body.find_all(text=('the'), limit=1) 
    #print gaff
'''
##DB##
'''
Tab sv 


As long as tabs are only used as delimiters in your file you should be able to do something like this:

import re

# connect to MySQLdb

with open(file_name) as f:
    for line in f:
        id, title, genre = re.split(r'\t+', line)
        # execute INSERT statement

>>> import MySQLdb
>>> conn = MySQLdb.connect (host = "localhost",
                             user = "me",
                             passwd = "password",
                             db = "my-db")
>>> cursor = conn.cursor ()
>>> # for loop  # how to read from the txt file to insert it as required?
>>>     # cursor.execute (INSERT...)
>>> conn.commit()
>>> conn.close()

Comma sv
import re

# connect to MySQLdb

with open(file_name) as f:
    for line in f:
        id, title, genre = re.split(r'\n+', line)
        # execute INSERT statement

with open('your_data_file.dat','r') as source:
    rdr= csv.reader( source, delimiter='\t', quotechar='')
    for row in rdr:
        # you have your columns with which to do your insert.
conn.commit()

from contextlib import closing

with open('your_data_file.dat','r') as source:
    rdr= csv.reader( source, delimiter='\t', quotechar='')
    with closing(conn.cursor()) as cursor:
        for row in rdr:
            # you have your columns with which to do your insert.
conn.commit()
'''
