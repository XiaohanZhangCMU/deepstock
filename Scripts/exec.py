#!/usr/bin/env python

import scrape_bloomberg as blmbg
import scrape_twitter as twttr
import smart_plot as smplt
import commands
import os

if __name__ == "__main__":

    # add more stocks to watch in here. 
    watch_list = {  #'facebook'    : 'FB:US',
                    'capitalone'  : 'COF:US',
                    'apple'       : 'AAPL:US',
                    'tesaro'      : 'TSRO:US',
                    'tesla'       : 'TSLA:US',
                    'pfizer'      : 'PFE:US',
                    'alibaba'     : 'BABA:US'
                    'nintendo'    : '7974:JP'
                 }
        
    dirs = ['../Bloomberg/', '../Twitter/', '../Graphics/']
    for dir in dirs:
        if not os.path.exists(dir):
            commands.getstatusoutput('mkdir '+dir)

    # lprd := duration twitter being listened to in [Seconds]
    lprd = 1200

    blmbg.collect_stockdata (watch_list, dirs[0])    
    twttr.collect_rumors (watch_list, lprd, dirs[1])    
    smplt.stock_plot (watch_list,dirs[2],dirs[0])
    smplt.twitter_hist(watch_list,dirs[2],dirs[1])

    print ("... normal end of program")
