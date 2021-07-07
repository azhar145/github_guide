import yfinance as yf
import pandas as pd
pd.options.display.max_columns = 50
pd.options.display.max_rows = 1000
#pd.options.display.max_colwidth =180
pd.set_option('display.max_colwidth', 16)
pd.set_option("display.expand_frame_repr", False)

#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.width',15)
#pd.set_option('display.max_colwidth', -1)

print('/n/n','babu','/n/n')
ticker=input('Enter ticker: ')
ca=input('call or put: c or p: ')
if ca=='c':
    ca='call'
elif ca=='p':
    ca='put'
else:
    ca='put'


b= yf.Ticker(ticker)
contracts=input("Number of contracts: ")
#contracts = contractsd * 100
#if contracts=="":
#    contracts=1200

#bh=b.history(start="2021-06-15", end="202-06-27", interval="1m")
print(b.info)
print('Ticker: ',b.info['symbol'],'  Prev close: ',b.info['previousClose'],' RegularMarketPrie: ',b.info['regularMarketPrice'], ' delta: ',b.info['regularMarketPrice']-b.info['previousClose'],'day low: ',b.info['dayLow'])
#print('Ticker: ',b.info['symbol'],' Avg_Volume: ',b.info["averageVolume"],'   ','Last_10_days: ',b.info["averageVolume10days"])
#print('Options',b.options[0],'      ',b.option_chain(date=(b.options[0])).calls)

callsa=b.option_chain(date=(b.options[0])).calls
putsa=b.option_chain(date=(b.options[0])).puts
#print(callsa.columns)
#print(callsa)
#print(putsa)


if ca=='c':
    callsa['expa']=callsa
#    exp =callsa
#else:
#    exp=putsa
#    callsav['exp']=putsa

callsav=callsa[['lastTradeDate', 'strike', 'lastPrice', 'bid', 'ask',
           'change', 'percentChange', 'volume', 'openInterest',
                  'impliedVolatility', 'inTheMoney']]
#callsav['m']=callsav['bid']-callsav['ask']
callsav['n']=callsav['strike']-b.info['regularMarketPrice']
callsav['regularMarketPrice']=b.info['regularMarketPrice']
#print(callsav.sort_values(by='n', ascending=False).head(135))
callsav['ca']=ca
callsav['ticker']=b.info['symbol']
callsav['s_strike']=callsav['strike'].shift(1)
callsav['s_bid']=callsav['bid'].shift(1)
callsav['s_ask']=callsav['ask'].shift(1)


callsav['xbid']=callsav['ask']-callsav['s_bid']

callsav['xbid']=callsav['ask']-callsav['s_bid']
callsav['xask']=callsav['s_ask']-callsav['bid']
callsav['xstrike']=callsav['strike']-callsav['s_strike']
callsav['mid']=callsav['xbid']+callsav['xask']/2
#callsav['profit']=int(contracts)*callsav['mid']
callsav['profit']=int(contracts)*100
#callsav['profit']=callsav['profit']*float(callsav['mid'])
#callsav['profit']=callsav['profit'].round(2)
callsav['loss']=(callsav['xstrike']-callsav['mid'])*int(contracts)
#callsav['loss']=callsav['loss'].round(2)

callav=callsav[['regularMarketPrice','ca','strike','n','bid', 'ask','inTheMoney','s_strike','s_bid','s_ask','xbid','xask','mid','xstrike','profit','loss']]
#print(callav.iloc[98:101,:])
#print(callav)

