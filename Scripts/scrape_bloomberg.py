#!/usr/bin/env python

# install procedures for mac: (requiring root access)
# 1) download beautifulsoup. 2) tar -xvf cd 3) python setup.py install 
# install procedures for remote linux server: (no root access required)
# 1) download beautifulsoup. 2) tar -xvf cd 
# 3) easy_install --prefix=/home/xzhang11/usr/ beautifulsoup4-4.4.1
# 4) edit .bashrc s.t., 
# export PYTHONPATH=$PYTHONPATH:/home/xzhang11/usr//lib/python2.7/site-packages

# To-do:
# Find good text mining package(NLTK maybe). add text-mining of language clustering to each company, write the info out
# Bash script to automatically run this function 3 times a day
# Add email alert 
# Add statistics predictions. 
# 

import os, csv, datetime
from bs4 import BeautifulSoup, NavigableString
from urllib import urlopen

# remove whitespace of a string
def strip1(str):
    if "Yr Return" in str:
        s = str.split()[1]
    else:
        s = str.split()[0]
    return s

def strip2(str):
    s =[strip1(str.split('-')[0]),strip1(str.split('-')[1])];    
    return s

# In:  html is url obj contains bloomberg stock. csvname an absolute file name.
# Data format:
# time() | open amount | day min | day max | prev close | 52w min | 52w max | 1yr return | YTD return

def parse_html_bloomberg(html, csvname):
    soup = BeautifulSoup(html,"html.parser")
    for section in soup.find_all('div', {"class":"data-table data-table_detailed"}):
        for cell in section.findChildren():    
            if len(cell.findChildren())==0:
                continue            
            name_cell = cell.findChildren()[0]
            val_cell  = cell.findChildren()[1]
            name = strip1(name_cell.contents[0])
            if name == 'Open':
                open_amount = strip1(val_cell.contents[0])
            if name == 'Day':
                [day_min,day_max] = strip2(val_cell.contents[0])
                days = strip2(val_cell.contents[0])                
            if name == 'Previous':
                prev_close = strip1(val_cell.contents[0])
            if name == '52Wk':
                [min_52w, max_52w] = strip2(val_cell.contents[0])
            if name == 'Yr':
                return_1yr = strip1(val_cell.contents[0])
            if name == 'YTD':
                return_ytd = strip1(val_cell.contents[0])
        #end cell loop
        break
    # end section loop

    # begin writing out data, appending to the existing file.
    with open(csvname, "a") as csv_file:
        csv_writer = csv.writer(csv_file,delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)        
        csv_writer.writerow( [datetime.datetime.now(), open_amount, day_min, day_max, prev_close, min_52w, max_52w, return_1yr, return_ytd ])
    csv_file.close()


def collect_stockdata(watch_list, dirname):
    
    # some path constants.

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    csvfiles = []
    comnames = []
    for name, code in watch_list.items():
        print '#-------------# grep '+name+' stock data ... #-------------#'
        html = urlopen('http://www.bloomberg.com/quote/'+code).read()
        csvname = dirname+name+'.csv'
        parse_html_bloomberg( html, csvname )
        csvfiles.append(csvname)
        comnames.append(name)

    buy = 1
    sell= 1
    if buy or sell:
        os.system("mail -s 'From mc2:PriceWatch' xzhang11@stanford.edu < /dev/null")

    return 0
