import talib as ta
import yfinance as yf
import pandas as pd
import datetime as dt
import sys
import numpy as np
from talib import stream
import matplotlib.pyplot as plt
def m(x):
    x='pupu yar'
    return(x)
'''
import talib as ta
print(help(ta))
print(help(ta.CDLSHORTLINE))
'''
pd.options.display.max_columns=255
pd.options.display.max_rows=6500000
ticker='^NDX'
u=[]
df = yf.download(ticker, '2021-02-1','2021-07-27', index=False)
df.reset_index(inplace = True)

df['day'] = df['Date'].dt.day_name()
df['ticker']=ticker
##df['Volume']=(df['Volume']/1000)
##df['Date'] = df['Date'].resample(rule='D').mean()
df['Volume']=df['Volume'].round(1)

df['Simple MA_3'] = ta.SMA(df['Close'].astype(int),3)
df['Simple MA_10'] = ta.SMA(df['Close'].astype(int),10)
df['Day_swing']=df['High']-df['Low']
df['Yest_Close']=df['Close'].shift(-1)
df['delta']=df['Close']-df['Yest_Close']
df['delta_cl_op']=df['Open']-df['Yest_Close']
df['*']='*'
df['CCI']=ta.CCI(df['High'], df['Low'], df['Close'], timeperiod=3)
#Commodity Channel Index (Momentum Indicators)
df['ADX']=ta.ADX(df['High'], df['Low'], df['Close'], timeperiod=3)
##Average Directional Movement Index (Momentum Indicators)
df['CDLSHORTLINE']=ta.CDLSHORTLINE(df['Open'],df['High'],df['Low'],df['Close'])
#Aroon (Momentum Indicators)
##df['CDL2CROWS']=ta.CDL2CROWS(df['High'], df['Low'], df['Close'], timeperiod=3)
#Two Crows (Pattern Recognition)
##df['CDLHARAMI']=ta.CDLHARAMI(df['High'], df['Low'], df['Close'], timeperiod=3)
#Two Crows (Pattern Recognition)


df['stream_WILLR']=ta.stream_WILLR(df['High'], df['Low'], df['Close'], timeperiod=3)
df['CDLDOJI']=ta.CDLDOJI(df['Open'],df['High'], df['Low'], df['Close'])

df['Volume']=df['Volume']/400000
df['Volume_1a']=df['Volume']
df['Volume_1']=df['Volume_1a'].shift(1)
df['Yest_Closea']=df['Close']
df['Yest_Close']=df['Yest_Closea'].shift(1)
df['Close_delta']=df['Yest_Close']-df['Close']
##df['Volume_1']=df['Volume_1'].shift(-1)
df['Volume_delta']=100-df['Volume']/(df['Volume_1'])*100
##df = pd.DataFrame(df,columns=['Date','day','Close','Open','Volume'])

##for x in (df.index):
##
##    print(df.loc[x,'Volume'],df.loc[x,'Close'])
##    if df[[x],'Close_delta'] < 0 and df['Volume_delta'] < 0:
##        df['vol_price']='Negative'
##    elif df['Close_delta'] > 0 and df['Volume_delta'] > 0:
##        df['vol_price']='Positive'
##    else:
##        df['vol_price']='no'

##df = pd.DataFrame(df,columns=['Date','day','Open','Close','Volume','Volume_1','Volume_delta','Yest_Close','Close_delta'])
df = pd.DataFrame(df,columns=['Date','day','Close','Volume','Simple MA_3','Simple MA_10','CDLDOJI'])
print(df)

##print(ta.CDLDOJI(df['Open'],df['High'], df['Low'], df['Close']))


df.set_index('Date').plot(figsize=(10,5), grid=True,  marker = 'o')
##plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

