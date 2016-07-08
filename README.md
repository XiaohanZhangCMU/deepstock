*****************************************************************
                      DeepStock: 
*****************************************************************

* Scrape tweets and stock data about companies in watch_list.
* Mining data for predictions. 
* [Learn more](https://xfdm@bitbucket.org/xfdm/deepstock.git)

*****************************************************************
                      Install dependent packages: 
*****************************************************************

easy_install --prefix=/home/xzhang11/usr/ beautifulsoup4-4.4.1
export PYTHONPATH=
$PYTHONPATH:/home/xzhang11/usr//lib/python2.7/site-packages

Python package Dependency:
1) numpy, scipy, matplotlib
2) pandas
3) beautifulsoup
4) tweepy

*****************************************************************
                      Run: 
*****************************************************************

Interactive or automatically every 7 hrs on a server.
cd Scripts && python exec.py
crontab -e  ' */420 * * * * ~/DeepStock/autorun.sh '

*****************************************************************
                      Contribution guides:
*****************************************************************

* Add more watching company in exec.py. 
* Apply fancy ML models to Twitter/*.txt and Bloomberg/*.csv
* contact: xiaohanzhang1985@gmail.com