#   Scraping Rules

#   You should check a websites Terms and Conditions before you scrape it. 
#   Be careful to read the statements about legal use of data. 
#   Usually, the data you scrape should not be used for commercial purposes.

#   Do not request data from the website too aggressively with your program (also known as spamming), 
#   as this may break the website. Make sure your program behaves in a reasonable manner 
#   (i.e. acts like a human). One request for one webpage per second is good practice.

#   The layout of a website may change from time to time, so make sure to revisit the site and 
#   rewrite your code as needed


#   Created by Russell Clarke 09/03/2018 for educational purposes.
#   Assisted from Tutorial located - https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
#   License - Ask.

# import libraries

import urllib2
from bs4 import BeautifulSoup

# specify the url as an array of URLs.
quote_page = ['http://www.bloomberg.com/quote/SPX:IND', 
              'http://www.bloomberg.com/quote/CCMP:IND',
              'http://www.licenseplatesdirect.com/licenseplate3.php?number=DT12',
              'http://www.russellclarke.co.uk/index.html']

# change the data extraction code into a for loop, 
# which will process the URLs one by one and store 
# all the data into a variable data in tuples.

# for loop
data = []
for pg in quote_page:

# query the website and return the html to the variable page
 page = urllib2.urlopen(pg)

# parse the html using beautiful soap and store in variable `soup`

 soup = BeautifulSoup(page, 'html.parser')
# Take out the <div> of name and get its value
 name_box = soup.find('h1', attrs={'class': 'name'})
 name = name_box.text.strip() # strip() is used to remove starting and trailing
# get the index price
 price_box = soup.find('div', attrs={'class':'price'})
 price = price_box.text.strip()
# get some data from my site
 russ_data = soup.find('p', attrs={'class':'notice'})
 russ = russ_data.text.strip()
# append takes one argument so make a list or array of results
 results = [name, price, russ]
 data.append(results)

 print data



############################Export to Excel CSV############################

# Now that we have the data, it is time to save it. The Excel Comma Separated Format is a nice choice. 
# It can be opened in Excel so you can see the data and process it easily. But first, we have to import
# the Python csv module and the datetime module to get the record date. BUt we modify the saving section 
# to save data row by row.

import csv
from datetime import datetime

# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
 # The for loop
    for name, price in data:
        writer.writerow([name, price, datetime.now()])

#   Advanced Scraping Techniques

#   BeautifulSoup is simple and great for small-scale web scraping. But if you are interested in scraping 
#   data at a larger scale, you should consider using these other alternatives:

#   Scrapy, a powerful python scraping framework

#   Try to integrate your code with some public APIs. The efficiency of data retrieval is much higher than
#   scraping webpages. For example, take a look at Facebook Graph API, which can help you get hidden data 
#   which is not shown on Facebook webpages.

#   Consider using a database backend like MySQL to store your data when it gets too large.
