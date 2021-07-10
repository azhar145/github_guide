import talib as ta
import yfinance as yf
import pandas as pd
import datetime as dt
import sys
import numpy as np
#from talib import stream
import matplotlib.pyplot as plt
def m(x):
    x='pupu yar'
    return(x)
'''
import talib as ta
print(help(ta))
print(help(ta.CDLSHORTLINE))
'''
pd.options.display.max_columns=155
pd.options.display.max_rows=6500000
ticker='TSLA'
u=[]
df = yf.download(ticker, '2021-05-1','2021-05-27', index=False)
##print(df.shape)
df.reset_index(inplace = True)

df['day'] = df['Date'].dt.day_name()
df['ticker']=ticker
##df['Volume']=(df['Volume']/1000)
##df['Date'] = df['Date'].resample(rule='D').mean()
df['Volume']=df['Volume'].round(1)
df['Simple MA_3'] = ta.SMA(df['Close'].astype(int),3)
df['Simple MA_10'] = ta.SMA(df['Close'].astype(int),10)
df['Day_swing']=df['High']-df['Low']
df['Yest_Close']=df['Close'].shift(+1)
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
##df['EMA'] = ta.EMA(df['Close'], timeperiod = 4)
##df['CDLGRAVESTONEDOJI']=ta.CDLGRAVESTONEDOJI(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLLADDERBOTTOM']=ta.CDLLADDERBOTTOM(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLSPINNINGTOP']=ta.CDLSPINNINGTOP(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLUPSIDEGAP2CROWS']=ta.CDLUPSIDEGAP2CROWS(df['Open'],df['High'], df['Low'], df['Close'])
##df['stream_CDLDOJI']=ta.stream_CDLDOJI(df['Open'],df['High'], df['Low'], df['Close'])
##df['stream_CCI']=ta.stream_CCI(df['High'], df['Low'], df['Close'], timeperiod=3)
####print(df.shape)
##df['CDL2CROWS']=ta.CDL2CROWS(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDL3BLACKCROWS']=ta.CDL3BLACKCROWS(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDL3INSIDE']=ta.CDL3INSIDE(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDL3OUTSIDE']=ta.CDL3OUTSIDE(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDL3STARSINSOUTH']=ta.CDL3STARSINSOUTH(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDL3WHITESOLDIERS']=ta.CDL3WHITESOLDIERS(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLABANDONEDBABY']=ta.CDLABANDONEDBABY(df['Open'],df['High'], df['Low'], df['Close'])
##
##df['CDLBELTHOLD']=ta.CDLBELTHOLD(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLBREAKAWAY']=ta.CDLBREAKAWAY(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLCLOSINGMARUBOZU']=ta.CDLCLOSINGMARUBOZU(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLCOUNTERATTACK']=ta.CDLCOUNTERATTACK(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLCONCEALBABYSWALL']=ta.CDLCONCEALBABYSWALL(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLDARKCLOUDCOVER']=ta.CDLDARKCLOUDCOVER(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLDOJI']=ta.CDLDOJI(df['Open'],df['High'], df['Low'], df['Close'])
####df['CDLDOJISTAR']=ta.CCDLDOJISTAR(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLDRAGONFLYDOJI']=ta.CDLDRAGONFLYDOJI(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLENGULFING']=ta.CDLENGULFING(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLEVENINGDOJISTAR']=ta.CDLEVENINGDOJISTAR(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLGAPSIDESIDEWHITE']=ta.CDLDARKCLOUDCOVER(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLDARKCLOUDCOVER']=ta.CDLDARKCLOUDCOVER(df['Open'],df['High'], df['Low'], df['Close'])
##
##df['CDLEVENINGSTAR']=ta.CDLEVENINGSTAR(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLDARKCLOUDCOVER']=ta.CDLDARKCLOUDCOVER(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLDARKCLOUDCOVER']=ta.CDLDARKCLOUDCOVER(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLDARKCLOUDCOVER']=ta.CDLDARKCLOUDCOVER(df['Open'],df['High'], df['Low'], df['Close'])
###################33
###https://www.programmersought.com/article/9630741113/
### https://libraries.io/pypi/TA-Lib
##df['CDL2CROWS']=ta.CDL2CROWS(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDL3BLACKCROWS']=ta.CDL3BLACKCROWS(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDL3INSIDE']=ta.CDL3INSIDE(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDL3LINESTRIKE']=ta.CDL3LINESTRIKE(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDL3OUTSIDE']=ta.CDL3OUTSIDE(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDL3STARSINSOUTH']=ta.CDL3STARSINSOUTH(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDL3WHITESOLDIERS']=ta.CDL3WHITESOLDIERS(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLABANDONEDBABY']=ta.CDLABANDONEDBABY(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLADVANCEBLOCK']=ta.CDLADVANCEBLOCK(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLBELTHOLD']=ta.CDLBELTHOLD(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLBREAKAWAY']=ta.CDLBREAKAWAY(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLCLOSINGMARUBOZU']=ta.CDLCLOSINGMARUBOZU(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLCONCEALBABYSWALL']=ta.CDLCONCEALBABYSWALL(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLCOUNTERATTACK']=ta.CDLCOUNTERATTACK(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLDARKCLOUDCOVER']=ta.CDLDARKCLOUDCOVER(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLDOJI']=ta.CDLDOJI(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLDOJISTAR']=ta.CDLDOJISTAR(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLDRAGONFLYDOJI']=ta.CDLDRAGONFLYDOJI(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLENGULFING']=ta.CDLENGULFING(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLEVENINGDOJISTAR']=ta.CDLEVENINGDOJISTAR(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLEVENINGSTAR']=ta.CDLEVENINGSTAR(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLGAPSIDESIDEWHITE']=ta.CDLGAPSIDESIDEWHITE(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLGRAVESTONEDOJI']=ta.CDLGRAVESTONEDOJI(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLHAMMER']=ta.CDLHAMMER(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLHANGINGMAN']=ta.CDLHANGINGMAN(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLHARAMI']=ta.CDLHARAMI(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLHARAMICROSS']=ta.CDLHARAMICROSS(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLHIGHWAVE']=ta.CDLHIGHWAVE(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLHIKKAKE']=ta.CDLHIKKAKE(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLHIKKAKEMOD']=ta.CDLHIKKAKEMOD(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLHOMINGPIGEON']=ta.CDLHOMINGPIGEON(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLIDENTICAL3CROWS']=ta.CDLIDENTICAL3CROWS(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLINNECK']=ta.CDLINNECK(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLINVERTEDHAMMER']=ta.CDLINVERTEDHAMMER(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLKICKING']=ta.CDLKICKING(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLKICKINGBYLENGTH']=ta.CDLKICKINGBYLENGTH(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLLADDERBOTTOM']=ta.CDLLADDERBOTTOM(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLLONGLEGGEDDOJI']=ta.CDLLONGLEGGEDDOJI(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLLONGLINE']=ta.CDLLONGLINE(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLMARUBOZU']=ta.CDLMARUBOZU(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLMATCHINGLOW']=ta.CDLMATCHINGLOW(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLMATHOLD']=ta.CDLMATHOLD(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLMORNINGDOJISTAR']=ta.CDLMORNINGDOJISTAR(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLMORNINGSTAR']=ta.CDLMORNINGSTAR(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLONNECK']=ta.CDLONNECK(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLPIERCING']=ta.CDLPIERCING(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLRICKSHAWMAN']=ta.CDLRICKSHAWMAN(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLRISEFALL3METHODS']=ta.CDLRISEFALL3METHODS(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLSEPARATINGLINES']=ta.CDLSEPARATINGLINES(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLSHOOTINGSTAR']=ta.CDLSHOOTINGSTAR(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLSHORTLINE']=ta.CDLSHORTLINE(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLSPINNINGTOP']=ta.CDLSPINNINGTOP(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLSTALLEDPATTERN']=ta.CDLSTALLEDPATTERN(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLSTICKSANDWICH']=ta.CDLSTICKSANDWICH(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLTAKURI']=ta.CDLTAKURI(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLTASUKIGAP']=ta.CDLTASUKIGAP(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLTHRUSTING']=ta.CDLTHRUSTING(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLTRISTAR']=ta.CDLTRISTAR(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLUNIQUE3RIVER']=ta.CDLUNIQUE3RIVER(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLUPSIDEGAP2CROWS']=ta.CDLUPSIDEGAP2CROWS(df['Open'],df['High'], df['Low'], df['Close'])
##df['CDLXSIDEGAP3METHODS']=ta.CDLXSIDEGAP3METHODS(df['Open'],df['High'], df['Low'], df['Close'])

##doji=ta.CDLDOJI(df['Open'],df['High'], df['Low'], df['Close'])
##num_signals=sum(doji[:2]>0)
##plt.plot(doji[:252])
##df['Close'].plot()

##df = pd.DataFrame(df,columns=['CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE', 'CDL3LINESTRIKE','Date'])
##df.plot(x='Date', y=['CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE', 'CDL3LINESTRIKE'], kind = 'scatter')
##plt.show()

df['Volume']=df['Volume']/400000
df = pd.DataFrame(df,columns=['Date','day','Close','Open','Volume'])

df = pd.DataFrame(df,columns=['Date','day','Close','Open','Volume','CDLDOJI'])

##df = pd.DataFrame(df,columns=['Date','day','Close','Open','Volume','****','stream_WILLR' ,'CDLDOJI' ,'EMA'  ,'CDLGRAVESTONEDOJI' ,'CDLLADDERBOTTOM' ,'CDLSPINNINGTOP' ,'CDLUPSIDEGAP2CROWS' ,'stream_CDLDOJI' ,'stream_CCI' ,'CDL2CROWS' ,'CDL3BLACKCROWS' ,'CDL3INSIDE' ,'CDL3OUTSIDE' ,'CDL3STARSINSOUTH' ,'CDL3WHITESOLDIERS' ,'CDLABANDONEDBABY' ,'CDLBELTHOLD' ,'CDLBREAKAWAY' ,'CDLCLOSINGMARUBOZU' ,'CDLCOUNTERATTACK' ,'CDLCONCEALBABYSWALL' ,'CDLDARKCLOUDCOVER' ,'CDLDOJI' ,'##',
##                              'CDLDOJISTAR' ,'CDLDRAGONFLYDOJI' ,'CDLENGULFING' ,'CDLEVENINGDOJISTAR' ,'CDLGAPSIDESIDEWHITE' ,'CDLDARKCLOUDCOVER' ,'CDLEVENINGSTAR' ,'CDLDARKCLOUDCOVER' ,'CDLDARKCLOUDCOVER' ,'CDLDARKCLOUDCOVER' ,'CDL2CROWS' ,'CDL3BLACKCROWS' ,'CDL3INSIDE' ,'CDL3LINESTRIKE' ,'CDL3OUTSIDE' ,'CDL3STARSINSOUTH' ,'CDL3WHITESOLDIERS' ,'CDLABANDONEDBABY' ,'CDLADVANCEBLOCK' ,'CDLBELTHOLD' ,'CDLBREAKAWAY' ,'CDLCLOSINGMARUBOZU' ,'CDLCONCEALBABYSWALL' ,'CDLCOUNTERATTACK' ,'CDLDARKCLOUDCOVER' ,'CDLDOJI' ,'CDLDOJISTAR' ,'CDLDRAGONFLYDOJI' ,'CDLENGULFING' ,'CDLEVENINGDOJISTAR' ,'CDLEVENINGSTAR' ,'CDLGAPSIDESIDEWHITE' ,'CDLGRAVESTONEDOJI' ,'CDLHAMMER' ,'CDLHANGINGMAN' ,'CDLHARAMI' ,'CDLHARAMICROSS' ,'CDLHIGHWAVE' ,'CDLHIKKAKE' ,'CDLHIKKAKEMOD' ,'CDLHOMINGPIGEON' ,'CDLIDENTICAL3CROWS' ,'CDLINNECK' ,'CDLINVERTEDHAMMER' ,'CDLKICKING' ,'CDLKICKINGBYLENGTH' ,'CDLLADDERBOTTOM' ,'CDLLONGLEGGEDDOJI' ,'CDLLONGLINE' ,'CDLMARUBOZU' ,'CDLMATCHINGLOW' ,'CDLMATHOLD' ,'CDLMORNINGDOJISTAR' ,'CDLMORNINGSTAR' ,'CDLONNECK' ,'CDLPIERCING' ,'CDLRICKSHAWMAN' ,'CDLRISEFALL3METHODS' ,'CDLSEPARATINGLINES' ,'CDLSHOOTINGSTAR' ,'CDLSHORTLINE' ,'CDLSPINNINGTOP' ,'CDLSTALLEDPATTERN' ,'CDLSTICKSANDWICH' ,'CDLTAKURI' ,'CDLTASUKIGAP' ,'CDLTHRUSTING' ,'CDLTRISTAR' ,'CDLUNIQUE3RIVER' ,'CDLUPSIDEGAP2CROWS' ,'CDLXSIDEGAP3METHODS'])
##


print(df)
print(ta.CDLDOJI(df['Open'],df['High'], df['Low'], df['Close']))
##df=df.cumsum(),
##ax = df.plot(x='Date', y='Close', kind='line',color='red',grid=True)
##df.plot(x='Date', y='Volume',  ax=ax, kind = 'bar',color='blue',grid=True)
##df.plot(x='Date', y='Close', kind = 'line', color='red',grid=True)
##df.plot(x='Date', y=['Volume','Close'], kind = 'bar',grid=True)
df.set_index('Date').plot(figsize=(10,5), grid=True)
plt.show()

##df['CDLDOJI']


##print(df.dtypes)
##
##df['test']=m(df['delta'])
##dft = df.reindex(columns=['test','Open', 'Simple MA_3', 'High', 'Yest_Close', 'ticker', 'CCI','ADX','CDLSHORTLINE','CDLGRAVESTONEDOJI',
##                          'CDLLADDERBOTTOM','CDLSPINNINGTOP','CDLUPSIDEGAP2CROWS','stream_CDLDOJI','stream_CCI',
##                          'Simple MA_10', 'CDLDOJI', 'stream_WILLR', 'Day_swing', '*',
##                          'delta', 'delta_cl_op', 'EMA', 'Close', 'Volume', 'Date', 'Low',
##                          'day', 'Adj Close'])
##
##df=dft[['test','Date','day','ticker','Close','*','delta','Day_swing','delta_cl_op',
##        'Open',
##        'High', 'Low', 'Adj Close', 'Volume', 'ticker','Y,##print(df['Simple MA_10'][10:])



##
##u3=df4['Close'][10:]
##u1=(df4['Simple MA_10'][10:])
##u2=df4['Simple MA_3'][10:]
##
##print(df4.shape)
##k=0
##for x in range(11,75):
####for x in range(10,30):
##    if u2.iloc[x]  > u1.iloc[x] and u3.iloc[x] > u2.iloc[x]:
##        print(k,'  ',x,"high-high",
##              '(MA3>MA20:',(u2.iloc[x]-u1.iloc[x]).round(2),')',
##              '(Price>MA3: (',(u3.iloc[x]-u2.iloc[x]).round(2),') ',
##              '(Price>MA20: (',(u3.iloc[x]-u1.iloc[x]).round(2)
##              ,') ')
####              u3.iloc[x]-u2.iloc[x],') ',u3.iloc[x]-u3.iloc[x],'   ',u1.iloc[x], '   ',u2.iloc[x])
##
##    elif u2.iloc[x]==u1.iloc[x]:
##        print('*************')
##
##    elif u3.iloc[x]==u2.iloc[x]:
##        print('*************')
##
##    elif u2.iloc[x]  > u1.iloc[x] and (u1.iloc[x] < u3.iloc[x] <  u2.iloc[x]):
##        print(x,"High-Between",
##              '(MA3>MA20:',(u2.iloc[x]-u1.iloc[x]).round(2),')',
##              '(Price>MA3: (',(u3.iloc[x]-u2.iloc[x]).round(2),') ',
##              '(Price>MA20: (',(u3.iloc[x]-u1.iloc[x]).round(2)
##              ,') ')
##
####              u3.iloc[x],'   ',u1.iloc[x], '   ',u2.iloc[x])
##
##    elif u2.iloc[x]  > u1.iloc[x] and (u3.iloc[x] <  u2.iloc[x] and u3.iloc[x] < u2.iloc[x]):
##        print(x,"High-LowLow",
##              '(MA3>MA20:',(u2.iloc[x]-u1.iloc[x]).round(2),')',
##              '(Price<MA3: (',(u3.iloc[x]-u2.iloc[x]).round(2),') ',
##              '(Price<MA20: (',(u3.iloc[x]-u1.iloc[x]).round(2)
##              ,') ')
####u3.iloc[x],'   ',u1.iloc[x], '   ',u2.iloc[x])
##
###############################################################################################################
##    elif u2.iloc[x]  < u1.iloc[x] and u3.iloc[x] > u2.iloc[x] and u3.iloc[x] > u1.iloc[x]:
##        print(x,"Low-high",
##              '(MA3 < MA20:',(u2.iloc[x]-u1.iloc[x]).round(2),')',
##              '(Price>MA3: (',(u3.iloc[x]-u2.iloc[x]).round(2),') ',
##              '(Price>MA20: (',(u3.iloc[x]-u1.iloc[x]).round(2)
##              ,') ')
####              u3.iloc[x]-u2.iloc[x],') ',u3.iloc[x]-u3.iloc[x],'   ',u1.iloc[x], '   ',u2.iloc[x])
##
##    elif u2.iloc[x]  < u1.iloc[x] and (u3.iloc[x] >  u2.iloc[x]) and (u3.iloc[x] <  u1.iloc[x]):
##        print(x,"Low-Between",
##              '(MA3 < MA20:',(u2.iloc[x]-u1.iloc[x]).round(2),')',
##              '(Price>MA3:(',(u3.iloc[x]-u2.iloc[x]).round(2),') ',
##              '(Price>MA20:(',(u3.iloc[x]-u1.iloc[x]).round(2)
##              ,') ')                
####              u3.iloc[x],'   ',u1.iloc[x], '   ',u2.iloc[x])
##
##    elif u2.iloc[x]  < u1.iloc[x] and (u3.iloc[x] <  u2.iloc[x]) and (u3.iloc[x] <  u1.iloc[x]):
##        print(x,"Low-LowLow",
##              '(MA3 < MA20:',(u2.iloc[x]-u1.iloc[x]).round(2),')',
##              '(Price<MA3: (',(u3.iloc[x]-u2.iloc[x]).round(2),') ',
##              '(Price<MA20: (',(u3.iloc[x]-u1.iloc[x]).round(2)
##
##             ,') ')
####u3.iloc[x],'   ',u1.iloc[x], '   ',u2.iloc[x])
##       
##        
##    else:
##        pass
##    print('k=',k)
##    k=k+1
##
##
