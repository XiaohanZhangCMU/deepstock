import scrape_bloomberg as blmbg
import scrape_twitter as twttr
import smart_plot as smplt

if __name__ == "__main__":

    # add more stocks to watch in here. 
    watch_list = {  'facebook'    : 'FB:US',
                    'capitalone'  : 'COF:US',
                    'apple'       : 'AAPL:US',
                    'tesaro'      : 'TSRO:US',
                    'tesla'       : 'TSLA:US',
                    'pfizer'      : 'PFE:US',
                    'alibaba'     : 'BABA:US'
                 }
        
    stock_dir = '../Bloomberg/'
    twitter_dir = '../Twitter/'
    graphic_dir = '../Graphics/'

    blmbg.collect_stockdata (watch_list, stock_dir)    
    twttr.collect_rumors   (watch_list, twitter_dir)
    
    smplt.stock_plot(watch_list,graphic_dir,stock_dir)
    smplt.twitter_hist(watch_list,graphic_dir,twitter_dir)

    print ("... normal end of program")
