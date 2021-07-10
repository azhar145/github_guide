from yahoo_fin import options 
import pandas as pd
from yahoo_fin import stock_info as f
import textwrap 

pd.options.display.max_columns = 50
pd.options.display.max_rows = 1000
pd.options.display.max_colwidth =180
pd.set_option('display.max_colwidth', 0)
pd.set_option("display.expand_frame_repr", False)

dd_most_active=pd.DataFrame(f.get_day_most_active())
print('---------------  Most Active -----------------------')
print(dd_most_active)
print('\n\n')


print('---------------------- Day Gainers ---------------------')        
dd_day_gainers=pd.DataFrame(f.get_day_gainers())
print(textwrap.shorten(dd_day_gainers.dtype(str), width=70))
print('\n\n')

print('---------------------- Day Losers  ---------------------')        
dd_day_losers=pd.DataFrame(f.get_day_losers())
print(dd_day_losers)
print('\n\n')



ticker=input("Enter ticker: ")

#ticker='^ndx'
x="calls"
y="puts"


print('\n\n')
print('stock live  price ------ >  ',f.get_live_price(ticker).round(2))
print('stock pre market price ---> ',f.get_premarket_price(ticker).round(2))

print('\n\n')

nflx_dates = options.get_expiration_dates(ticker)
chain = options.get_options_chain(ticker)
chain[x]

#######################################################
c=chain[x]
#print(c)
df=pd.DataFrame(c)
print(df.shape)
#dfc=df.sort_values(by='Volume')
dfc=df.sort_values(by='Volume', ascending=False)
#print(df)
#print(dfa.Date.dt.date.unique())
print('*****************************************************************************************************')
print("calls")
print(dfc.head(4))
print('*****************************************************************************************************')
print('\n\n')
#######################################################
#######################################################
p=chain[y]
#print(c)
df=pd.DataFrame(p)
print('*****************************************************************************************************')
print(df.shape)
dfp=df.sort_values(by='Volume', ascending=False)
#print(df)
#print(dfa.Date.dt.date.unique())
print("puts")
print(dfp.head(4))
print('*****************************************************************************************************')
print('\n\n')
nflx_dates= options.get_expiration_dates(ticker)
print(nflx_dates)

################################################################################
dfd=pd.DataFrame()
dfd=get_puts(tickers, '06/11/2021')
print(dfd)




'''
info = {}
for date in nflx_dates:
        info[date] = options.get_options_chain(ticker)
#print(info)
#print(info.Date.dt.date.unique())



chain["puts"]
options.get_options_chain("nflx", "April 26, 2019")
 
options.get_options_chain("nflx", "05/03/19")
 
options.get_options_chain("nflx", "05/10/2019")
options.get_calls("nflx")
 
options.get_calls("nflx", "04/26/19")
 
 
options.get_puts("nflx")
 
options.get_puts("nflx", "04/26/19")



####################################################
#How to get options data for each expiration date

nflx_dates= options.get_expiration_dates("nflx")
 
info = {}
for date in nflx_dates:
    info[date] = options.get_options_chain("nflx")
    
info["October 18, 2019"]

##################################################

# How to get options data for every stock in the Dow
from yahoo_fin import stock_info as si
 
dow_tickers = si.tickers_dow()
 
# replace DOW with DWDP in ticker list
dow_tickers.remove("DOW")
dow_tickers.append("DWDP")
 
# scrape the options data for each Dow ticker
dow_data = {}
for ticker in dow_tickers:
    try:
        dow_data[ticker] = options.get_options_chain(ticker)
    except Exception:
        print(ticker + " failed")
        
        
dow_data["AAPL"]["calls"]
 
dow_data["WMT"]["calls"]

'''
