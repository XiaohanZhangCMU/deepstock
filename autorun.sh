#!/bin/bash

# collect data & rumor every 7 hrs
# crontab -e 
# */420 * * * *	~/DeepStock/autorun.sh 


source /home/xzhang11/.bashrc

cd /home/xzhang11/DeepStock/Scripts

python exec.py