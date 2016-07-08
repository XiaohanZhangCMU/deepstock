*****************************************************************
                      About DeepStock functionals: 
*****************************************************************

* Scrape tweets and stock data about companies in watch_list.
* Mining data for predictions. 
* [Learn more](https://xfdm@bitbucket.org/xfdm/deepstock.git)

*****************************************************************
                      Install dependent packages: 
*****************************************************************

easy_install --prefix=/home/xzhang11/usr/ beautifulsoup4-4.4.1
easy_install --prefix=/home/xzhang11/usr/ oauth2
easy_install --prefix=/home/xzhang11/usr/ tweepy
easy_install --prefix=/home/xzhang11/usr/ pandas (takes 5 mins)

export PYTHONPATH=
$PYTHONPATH:/home/xzhang11/usr//lib/python2.7/site-packages

Other python package dependency:
1) numpy, scipy, matplotlib

*****************************************************************
                      Run DeepStock on mac/linux: 
*****************************************************************

Interactive or automatically every 7 hrs on a server.
cd Scripts && python exec.py
crontab -e  ' */420 * * * * ~/DeepStock/autorun.sh '

stock data from bloomberg and tweet rumors are stored in 
Twitter/ and Bloomberg/

*****************************************************************
                      Contribution guides:
*****************************************************************

* Add more watching company in exec.py. 
* Apply fancy ML models to Twitter/*.txt and Bloomberg/*.csv
* contact: xiaohanzhang1985@gmail.com