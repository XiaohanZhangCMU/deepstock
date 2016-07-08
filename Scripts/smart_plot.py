from numpy import *
from scipy.integrate import trapz, cumtrapz
from glob import *
import matplotlib
matplotlib.use("PDF")  # non-interactive plot making
import matplotlib.pyplot as plt
import os, csv
import sys, getopt
from itertools import islice
from subprocess import call
from pylab import *
import time   
import json
import pandas as pd
import matplotlib.pyplot as plt


#
# ----------------------------------------------------------------------------
#
#    plot_set_up -- call before any plt.plot(...)
#
# ----------------------------------------------------------------------------
#
def plot_set_up( type ):
   global plot_colors, leglocs, plot_markers
   global params
#
#      type
#       0   1 plot landscape
#       1   1 plot portrait
#

   plot_colors = ["r", "orange", "b", "m", "c", "k" ]
   plot_markers = ["o", "s", "D"]
   leglocs = [1,2,3,4,5,6,7,8,9]
   paper_width = 11.0   # inches
   paper_height = 8.5  
   
#legend location 
#String Number
#upper right  1
#upper left   2
#lower left   3
#lower right  4
#right        5
#center left  6
#center right 7
#lower center 8
#upper center 9

   params = {'legend.fontsize': 12,
             'legend.linewidth': 0.75,
             'legend.frameon': True,
             'legend.numpoints': 1,
             'figure.figsize': (paper_width,paper_height),
             'axes.linewidth': 1.125,
             'axes.titlesize': 10,       # plot title
             'axes.labelsize': 25,
             'axes.labelcolor': 'k',
             'xtick.major.size': 10,     # major tick size in points
             'xtick.minor.size': 5,      # minor tick size in points
             'xtick.major.pad': 6,       # distance to major tick label in points
             'xtick.minor.pad': 4,       # distance to the minor tick label in points
             'xtick.color': 'k',         # color of the tick labels
             'xtick.labelsize': 10,      # fontsize of the tick labels
             'ytick.major.size': 10,     # major tick size in points
             'ytick.minor.size': 5,      # minor tick size in points
             'ytick.major.pad': 6,       # distance to major tick label in points
             'ytick.minor.pad': 4,       # distance to the minor tick label in points
             'ytick.color': 'k',         # color of the tick labels
             'ytick.labelsize': 10 }     # fontsize of the tick labels

   plt.rcParams.update(params)
   plt.subplots_adjust(left=0.2, right=0.8,
                    bottom=0.2, top=0.8) # nice margins on page
   return
#
# ----------------------------------------------------------------------------
#
#    plot_start
#
# ----------------------------------------------------------------------------
#
def plot_start():
   global plot_colors

#           1 plot on 11.0 x 8.5 (landscape)
#           has nice margins around, plot is
#           centered on page with rectangular shape
#           saved as pdf with transparent background
#
#           PPT on OS X. drag-drop .pdf onto slide.
#           scaling then changes uniformly the size of
#           all fonts, line thicknesses etc.
#
   plot_set_up( 0 )
   plt.figure()
   plot_set_up( 0 )
#   
   return

#
# ----------------------------------------------------------------------------
#
#    plot_finish
#
# ----------------------------------------------------------------------------
#
def plot_finish(data_index):

   plt.annotate(' ',xy=(0.02, 0.92), xycoords='axes fraction')
   plt.grid(True)
   
   plot_file_name = 'stock-watch.pdf'
   print 'plt_file_name = ', plot_file_name

   if os.path.isfile( plot_file_name ):
      os.remove( plot_file_name )
   plt.savefig( plot_file_name, transparent=True)

   open = 0
   if open == 1:
      err = os.system("which acroread")
      pdfcmmd = 'acroread '
      if err != 0:
         err = os.system("which open")
         pdfcmmd = 'open '
         if err != 0:
            print 'Install acroread or evince to open result plot.'
            exit(0)
         
#      os.system(pdfcmmd + plot_file_name)

#   fileList = glob('*.pdf')
#   for f in fileList:
#      system('pdftops -eps {0}'.format(f))

   return
#

def time_to_float(datetime):

   year = int(datetime.split(' ')[0].split('-')[0])
   month = int(datetime.split(' ')[0].split('-')[1])
   day = int(datetime.split(' ')[0].split('-')[2])
   hour = int( datetime.split(' ')[1].split(':')[0])
   minute = int( datetime.split(' ')[1].split(':')[1])
   second = float( datetime.split(' ')[1].split(':')[2])
   return 10000*year + 100*month + day + hour/100.0 + minute/10000.0 + second/1000000.0


# ----------------------------------------------------------------------------
#
#    begin main
#
# ----------------------------------------------------------------------------
#
def stock_plot(watch_list, dirname, stock_dir):
   
   set_printoptions(threshold='nan')
   plot_start()
   fig = plt.figure()

   for csvfile in watch_list.keys():
      valarr = np.zeros((0,2))
      reader = csv.reader(open(stock_dir+csvfile+'.csv'),delimiter = ' ', quotechar='|')
      for datetime, open_amount, day_min, day_max, prev_close, min_52w, max_52w, return_1yr, return_ytd in reader:
          valarr = np.vstack([valarr, [time_to_float(datetime), day_max]])

      plt.plot( valarr[:,0], valarr[:,1], '-o', linewidth=3.0)
      legend(watch_list.keys(),loc=2)
       
   plot_finish(-1)

   return 0


def twitter_hist(watch_list, dirname, twitter_dir):

    tweets_data_path = twitter_dir+'twitter_data.txt'
    tweets_data = []
    tweets_file = open(tweets_data_path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue

    print len(tweets_data)

    tweets = pd.DataFrame()

    tweets['facebook'] = tweets['text'].apply(lambda tweet: word_in_text('facebook', tweet))
    tweets['capitalone'] = tweets['text'].apply(lambda tweet: word_in_text('capitalone', tweet))
    tweets['apple'] = tweets['text'].apply(lambda tweet: word_in_text('apple', tweet))
    tweets['tesla'] = tweets['text'].apply(lambda tweet: word_in_text('tesla', tweet))

    print tweets['facebook'].value_counts()[True]
    print tweets['capitalone'].value_counts()[True]
    print tweets['apple'].value_counts()[True]
    print tweets['tesla'].value_counts()[True]

    prg_langs = ['facebook', 'capitalone', 'apple','tesla']
    tweets_by_prg_lang = [tweets['facebook'].value_counts()[True], tweets['capitalone'].value_counts()[True], tweets['apple'].value_counts()[True],  tweets['tesla'].value_counts()[True]]
    
    x_pos = list(range(len(prg_langs)))
    width = 0.8
    fig, ax = plt.subplots()
    plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')
    ax.set_ylabel('Number of tweets', fontsize=15)
    ax.set_title('News: facebook vs. capitalone vs. apple vs. tesla', fontsize=10, fontweight='bold')
    ax.set_xticks([p + 0.4 * width for p in x_pos])
    ax.set_xticklabels(prg_langs)
    plt.grid()

    plt.savefig( dirname+'bar-companies-mentioned.pdf', transparent=True)

    return 0

   
