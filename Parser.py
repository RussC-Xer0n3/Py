#! /bin/env python

#https://docs.python.org/3/library/html.parser.html
import HTMLParser
import csv
import os

path = "" #windows uses backslash in their working directory structuring unix and linux use forwardslash
logFile_name = "output.csv"

def MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
        print('')

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        print('')

    def handle_data(self, data):
        print("", data)
        csv_writer()

def csv_writer(c, l, f):      
    # open a csv file with append, so old data will not be erased
    with open(f, 'a') as csv_file:
        writer = csv.writer(csv_file)
        # The for loop
        for c in l:
            writer.writerow([c, datetime.now()]) # Changed from l to c. (check this is csv should have no carriage n)
    csv_file.close()
    print "Data gathered from "+path+" and can be found in "+logFile_name+"."

def dircheck(path):
    # Check current working directory.
    retval = os.getcwd()
    # If equal to specified, notify.
    if retval == path:
        print "Current working directory %s" % retval
        print "Would you like to change the path to the file? Y/N"
        answer = raw_input()
        if answer is (Y or yes):
            print('Please enter the directory path')
            path = raw_input()
            os.chdir(path)
            if retval != os.getcwd(retval):
                print('That path does not exist')
            elif retval == os.getcwd(retval):
                path = retval
                print("Directory changed successfully %s" % retval)
            return            
        elif answer is (N or no):
            path = retval
            return

dircheck( path )
parser = MyHTMLParser( path )
parser.feed( path ) #'<html><head><title>Test</title></head>'
            #'<body><h1>Parse me!</h1></body></html>'
