#!/bin/bash

source /home/xzhang11/.bashrc

cd /home/xzhang11/PriceWatch

python scrape_bloomberg.py

python scrape_twitter.py