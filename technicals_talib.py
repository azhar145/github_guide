import talib as ta
import yfinance as yf
import pandas as pd
import datetime as dt
import sys
from talib import stream

def m(x):
    x='pupu yar'
    return(x)
'''
import talib as ta
print(help(ta))
print(help(ta.CDLSHORTLINE))
'''
pd.options.display.max_columns=25
pd.options.display.max_rows=1500000
ticker='TSLA'
u=[]
df = yf.download(ticker, '2021-01-1','2021-05-27', index=False)
##print(df.shape)
df.reset_index(inplace = True)
df['day'] = df['Date'].dt.day_name()
df['ticker']=ticker
##df['Volume']=(df['Volume']/1000)
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
df['EMA'] = ta.EMA(df['Close'], timeperiod = 4)
df['CDLGRAVESTONEDOJI']=ta.CDLGRAVESTONEDOJI(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLLADDERBOTTOM']=ta.CDLLADDERBOTTOM(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLSPINNINGTOP']=ta.CDLSPINNINGTOP(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLUPSIDEGAP2CROWS']=ta.CDLUPSIDEGAP2CROWS(df['Open'],df['High'], df['Low'], df['Close'])
df['stream_CDLDOJI']=ta.stream_CDLDOJI(df['Open'],df['High'], df['Low'], df['Close'])
df['stream_CCI']=ta.stream_CCI(df['High'], df['Low'], df['Close'], timeperiod=3)
##print(df.shape)
##print(df.dtypes)

##df['test']=m(df['delta'])
##u3=df['Close'].real()
##u1=df['Simple MA_10'].real()
##u2=df['Simple MA_3'].real()
##print(df)
##if u1 > -10000 :
##    df['test]=m(df['delta'])
    
##u3=df['Close'][10:]
##u1=(df['Simple MA_10'][10:])
##u2=df['Simple MA_3'][10:]

##print(type(u3),len(u3))
##if u3.item() > -2 :
##       print("kaku")

df['k']=''
df['p']=''
def test2(pp):
    m=pp
    g=pp/100
    return(m,g)
    
print(df)
for x in range(1,df.shape[0]):
    
##    print(x,'   ',df.iloc[x,[0,1,2,3]])
    df['k'].iloc[x]=test2(df.iloc[x,3])[0]

print(df['k'])
##    print(x, mm)
##    df['kk'].iloc[x,14]=test2(df.iloc[x,0])
##    df['kk']=test2(df.iloc[x,0])

##print(df['kk'])

##dft = df.reindex(columns=['test','Open', 'Simple MA_3', 'High', 'Yest_Close', 'ticker', 'CCI','ADX','CDLSHORTLINE','CDLGRAVESTONEDOJI',
##                          'CDLLADDERBOTTOM','CDLSPINNINGTOP','CDLUPSIDEGAP2CROWS','stream_CDLDOJI','stream_CCI',
##                          'Simple MA_10', 'CDLDOJI', 'stream_WILLR', 'Day_swing', '*',
##                          'delta', 'delta_cl_op', 'EMA', 'Close', 'Volume', 'Date', 'Low',
##                          'day', 'Adj Close'])
##
##df=dft[['test','Date','day','ticker','Close','*','delta','Day_swing','delta_cl_op',
##        'Open',
##        'High', 'Low', 'Adj Close', 'Volume', 'ticker','Yest_Close',
##       'Simple MA_3', 'Simple MA_10', 
##       'stream_WILLR', 'CDLDOJI', 'EMA','CCI','ADX','CDLSHORTLINE','CDLGRAVESTONEDOJI','CDLLADDERBOTTOM'
##        ,'CDLSPINNINGTOP','CDLUPSIDEGAP2CROWS','stream_CDLDOJI','stream_CCI'
##        ]]
##df4=df.iloc[9:,[0,1,2,3,4,5,6]]
##print(df4)




##
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
