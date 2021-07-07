import plotly.graph_objs as go
import pandas as pd
import yfinance as yf
import numpy as np
from datetime import time
from numerize import numerize
from yahoo_fin import stock_info as f
import yahoo_fin.stock_info as si
from googlefinance import getQuotes as gg
import json




pd.options.display.max_rows=9999
pd.options.display.max_columns=26
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)


########################################################## daily ##################################################

perda='55d'
intervla='1d'


g=input("Enter ticker: ")
perd=perda
intervl=intervla

# [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]



#df=pd.DataFrame()
#Interval required 5 minutes
data = yf.download(g, period=perd, interval=intervl,prepost = True)

df=pd.DataFrame(data)
df.reset_index(drop=False,inplace=True)
df['ticker']=g
#df['Open']=df['Open']


df2=df

df['Opena']=''
df['green']=''
df['greenby']=''

for x in df.index:
    df['Opena'].loc[x]=int(df['Open'].loc[x])
    if df['Close'].loc[x]-df['Open'].loc[x] > 0:



        df['green'].loc[x]='Green'
        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
                                        #            print(x,'  ','Green','  ',df['ns'].loc[x])
    else:

        df['green'].loc[x]='Red'
        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
#print(df)
#print('\n',' 1-day    ',g,'\n')

df2['direct']=''
df2['down']=''
df2['a_Close']=''
df2['a_High']=''
df2['a_Low']=''
df2['a_Open']=''
df2['HA']=''
df2['Opena']=''
df2['green']=''
df2['greenby']=''


for x in df.index:

    df['Opena'].loc[x]=int(df['Open'].loc[x])
    if df['Close'].loc[x]-df['Open'].loc[x] > 0:
        df['green'].loc[x]='Green'
        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
        #            print(x,'  ','Green','  ',df['ns'].loc[x])
    else:
        df['green'].loc[x]='Red'
        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]

   # df2['a_Close'].loc[x]=1/4*(df['Open'].loc[x]+df2['High'].loc[x]+df2['Low'].loc[x]+df['Close'].loc[x])
   # df2['a_High']=max(df['High'].loc[x],df2['Open'].loc[x],df2['Close'].loc[x])
   # df2['a_Low']=min(df['Low'].loc[x],df2['Open'].loc[x],df2['Close'].loc[x])
   # df2['a_Open'].loc[x]=1/2*(df2['Open'].shift(1).loc[x]+df2['Close'].shift(1).loc[x])
#    df2['a_Open'].loc[x]=1/2*(df2['Open'].loc[x].shift(1)+df2['Close'].loc[x].shift(1))
   # df2['cx'].loc[x]=df2['a_Close'].loc[x]-df2['a_Open'].loc[x] 
    
    df2['a_Close'].loc[x]=1/4*(df['Open'].loc[x]+df2['High'].loc[x]+df2['Low'].loc[x]+df['Close'].loc[x])
    df2['a_Open'].loc[x]=1/2*(df2['Open'].shift(1).loc[x]+df2['Close'].shift(1).loc[x])
    df2['High'].loc[x]=df2['High'].loc[x]
    df2['Low'].loc[x]=df2['Low'].loc[x]
    df2['a_High'].loc[x]=max(df['High'].loc[x],df2['a_Open'].loc[x],df2['a_Close'].loc[x])
    df2['a_Low'].loc[x]=min(df['Low'].loc[x],df2['a_Open'].loc[x],df2['a_Close'].loc[x])
 #   df2['a_Open'].loc[x]=1/2*(df2['Open'].shift(1).loc[x]+df2['Close'].shift(1).loc[x])
    df2['HA'].loc[x]=df2['a_Close'].loc[x]-df2['a_Open'].loc[x]



#   if df2['a_Close'].loc[x] > df2['a_Open'].loc[x]:
    if df2['HA'].loc[x] > 0:    
        df2['direct'].loc[x]='HA_Green'
    elif df2['HA'].loc[x] < 0:
        df2['direct'].loc[x]='HA_Red'


#df2=df2[['Date','Volume', 'ticker', 'Opena', 'green', 'greenby', 'direct', 'HA','a_High','a_Low', 'High', 'a_Close', 'a_Open','Close']]

df2=df2[['ticker','Date','Volume','Close', 'direct', 'HA','green', 'greenby','Opena','a_High','a_Low', 'High', 'a_Close', 'a_Open']]




#df2['greenby']=df2['greenby'].round(2)
df2['Close']=df2['Close'].round(2)
#df2['a_Open']=df2['a_Open'].round(2)
#df2['a_Close']=df2['a_Close'].round(2)
df2['High']=df2['High'].round(2)
#df2['a_High']=df2['a_High'].round(2)


print(df2.tail(5))

print('\n','=================> 1- day    ',g,'\n')

########################################################################################################################################
########################################################## Hourly ##################################################

#perda='1d'
perda=input("Enter no of days (only enter number do not enter days): ")
perda=perda+'d'
#intervla='60m'
intervla=input("Enter minutes 5min, 10min, 15 min, 60min (only enter number, do not enter min): ")
intervla=intervla+'m'

#g=input("Enter ticker: ")
perd=perda
intervl=intervla

# [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]



#df=pd.DataFrame()
#Interval required 5 minutes
data = yf.download(g, period=perd, interval=intervl,prepost = True)

df=pd.DataFrame(data)
df.reset_index(drop=False,inplace=True)
df['ticker']=g

df['x']=df['Datetime'].dt.time
df['d']=df['Datetime'].dt.day_name()
df['u']=df['Datetime'].dt.date



#df['Open']=df['Open']


df2=df


#print('\n',df2,'\n')
df['Opena']=''
df['green']=''
df['greenby']=''

for x in df.index:
    df['Opena'].loc[x]=int(df['Open'].loc[x])
    if df['Close'].loc[x]-df['Open'].loc[x] > 0:



        df['green'].loc[x]='Green'
        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
                                        #            print(x,'  ','Green','  ',df['ns'].loc[x])
    else:

        df['green'].loc[x]='Red'
        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
#print(df)
#print('\n',' 1-day    ',g,'\n')

df2['direct']=''
df2['down']=''
df2['a_Close']=''
df2['a_High']=''
df2['a_Low']=''
df2['a_Open']=''
df2['HA']=''
df2['Opena']=''
df2['green']=''
df2['greenby']=''


for x in df.index:

    df['Opena'].loc[x]=int(df['Open'].loc[x])
    if df['Close'].loc[x]-df['Open'].loc[x] > 0:
        df['green'].loc[x]='Green'
        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
        #            print(x,'  ','Green','  ',df['ns'].loc[x])
    else:
        df['green'].loc[x]='Red'
        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]

   # df2['a_Close'].loc[x]=1/4*(df['Open'].loc[x]+df2['High'].loc[x]+df2['Low'].loc[x]+df['Close'].loc[x])
   # df2['a_High']=max(df['High'].loc[x],df2['Open'].loc[x],df2['Close'].loc[x])
   # df2['a_Low']=min(df['Low'].loc[x],df2['Open'].loc[x],df2['Close'].loc[x])
   # df2['a_Open'].loc[x]=1/2*(df2['Open'].shift(1).loc[x]+df2['Close'].shift(1).loc[x])
#    df2['a_Open'].loc[x]=1/2*(df2['Open'].loc[x].shift(1)+df2['Close'].loc[x].shift(1))
   # df2['cx'].loc[x]=df2['a_Close'].loc[x]-df2['a_Open'].loc[x] 
    
    df2['a_Close'].loc[x]=1/4*(df['Open'].loc[x]+df2['High'].loc[x]+df2['Low'].loc[x]+df['Close'].loc[x])
    df2['a_Open'].loc[x]=1/2*(df2['Open'].shift(1).loc[x]+df2['Close'].shift(1).loc[x])
    df2['High'].loc[x]=df2['High'].loc[x]
    df2['Low'].loc[x]=df2['Low'].loc[x]
    df2['a_High'].loc[x]=max(df['High'].loc[x],df2['a_Open'].loc[x],df2['a_Close'].loc[x])
    df2['a_Low'].loc[x]=min(df['Low'].loc[x],df2['a_Open'].loc[x],df2['a_Close'].loc[x])
 #   df2['a_Open'].loc[x]=1/2*(df2['Open'].shift(1).loc[x]+df2['Close'].shift(1).loc[x])
    df2['HA'].loc[x]=df2['a_Close'].loc[x]-df2['a_Open'].loc[x]



#   if df2['a_Close'].loc[x] > df2['a_Open'].loc[x]:
    if df2['HA'].loc[x] > 0:    
        df2['direct'].loc[x]='HA_Green'
    elif df2['HA'].loc[x] < 0:
        df2['direct'].loc[x]='HA_Red'


#df2=df2[['x','d','u','Volume', 'ticker', 'Opena', 'green', 'greenby', 'direct', 'HA','a_High','a_Low', 'High', 'a_Close', 'a_Open','Close']]
df2=df2[['ticker','x','d','u','Volume','Close', 'direct', 'HA','green', 'greenby','Opena','a_High','a_Low', 'High', 'a_Close', 'a_Open']]




#df2['greenby']=df2['greenby'].round(2)
df2['Close']=df2['Close'].round(2)
#df2['a_Open']=df2['a_Open'].round(2)
#df2['a_Close']=df2['a_Close'].round(2)
df2['High']=df2['High'].round(2)
#df2['a_High']=df2['a_High'].round(2)


print(df2.tail(215))

print('\n','=========>  1- min    ',g,'\n')

########################################################################################################################################


print('\n\n')

#ticker=input("Enter ticker: ")

ticker=g

#ticker='^ndx'
x="calls"
y="puts"

##########################################################################################################
print('\n\n')
print(" haha more to the story")
print('Ticker -----> ',f.get_quote_data(ticker)['symbol'],'           Industry: ',yf.Ticker(ticker).info['industry'])   
print('Shortname -----> ',f.get_quote_data(ticker)['shortName'])
print('stock live  price ------ >  ',f.get_live_price(ticker),'      ', 'Prev Yesterday Cloe :',yf.Ticker(ticker).info['regularMarketPreviousClose'],
       '   Change:',(f.get_live_price(ticker)-yf.Ticker(ticker).info['regularMarketPreviousClose']))
#print('stock postmarket price ------ >  ',yf.Ticker(ticker).info['postMarketPrice'])
print('Day Low ---->   ',yf.Ticker(ticker).info['dayLow'],'    Day High ',yf.Ticker(ticker).info['dayHigh'])

#print('stock pre market price ---> ',f.get_premarket_price(ticker).round(2))
#print('stock post market price ----> ',f.get_postmarket_price(ticker))
print('stock market status ---> ',f.get_market_status())
print('dd regularMarketVolume----> ', f.get_quote_data(ticker)['regularMarketVolume']/1000000, 'Million')
print('dd averageDailyVolume10Day----> ', f.get_quote_data(ticker)['averageDailyVolume10Day']/1000000, 'Million')
print('dd averageDailyVolume3Mont ----> ', f.get_quote_data(ticker)['averageDailyVolume3Month']/1000000, 'Million')
print('dd averageAnalystRating ----> **************** ', f.get_quote_data(ticker)['averageAnalystRating'])

print('EarningsQuarterlyGrowth---> ',yf.Ticker(ticker).info['earningsQuarterlyGrowth'])

#print(si.get_next_earnings_date(ticker))

#print(si.get_earnings(ticker))
#earnings_in_week = si.get_earnings_in_date_range("07/16/2021", "07/23/2021")
#print(earnings_in_week)
#print(help(f))

print('\n\n')
#print(help(si))
print(yf.Ticker(ticker).info['longBusinessSummary'])


#print(gg.getQuotes('AAPL'))



'''
print('dd Next Earning Date --------> ',f.get_next_earnings_date(ticker))
print('dd Days range ------> ',f.get_quote_data(ticker)['regularMarketDayRange'])
############# below is long
print('dd quote table -----> ',f.get_quote_data(ticker))
m=f.get_holders(ticker)
print('dd holders ----> ',m)
print('\n\n\n')
#########################################################################
#########################################################################
print("Volume up or down - (current volume vs 10 days volume),(current volume vs last 3 months)")

if (f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume10Day']) < 0:
    print('22 ----> 10 days (volume low yest vs last 10days)',(f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume10Day']))

if (f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume10Day']) >  0:
        print('22 ----> 10 days (volume high yest vs last 10days)',(f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume10Day']))

if (f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume3Month']) < 0:
        print('22 ----> 3 mnths (volume low yest vs last 3mnths)',(f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume3Month']))

if (f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume3Month']) >  0:
                    print('22 ----> 3 mnths (volume high yest vs last 3mnths)',(f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume3Month']))
####################################################
################################################
print('\n')
print('23 ----> ',f.get_stats(ticker))
print('\n')
print('24 ----> ',f.get_stats_valuation(ticker))
print('\n')
print('Analysts ---->  ',f.get_analysts_info(ticker))
print(f.info)
print('\n\n')
###########################################################################################################
'''
