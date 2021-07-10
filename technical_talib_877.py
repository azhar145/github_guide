import talib as ta
import yfinance as yf
import pandas as pd
import datetime as dt
import sys

pd.options.display.max_columns=25
pd.options.display.max_rows=1500000
ticker='NDX'
u=[]
df = yf.download(ticker, '2021-04-1','2021-05-27', index=False)
##print(df.index)
df.reset_index(inplace = True)
##df.index.name = None
##df.columns=['dd','dda','ddda','d','r','g']
df['day'] = df['Date'].dt.day_name()
##print(df.iloc[:,:])
##print(df.head(4))
##print(df['Date'])
##sys.exit()
df['ticker']=ticker
df['Simple MA_3'] = ta.SMA(df['Close'],3)
df['Simple MA_10'] = ta.SMA(df['Close'],10)
df['MA_3>10']=df['Simple MA_3']-df['Simple MA_10']
df['MA_3>10']=df['Simple MA_3']-df['Simple MA_10']
df['Day_swing']=df['High']-df['Low']
df['CCI']=ta.CCI(df['High'], df['Low'], df['Close'], timeperiod=3)
df['stream_WILLR']=ta.stream_WILLR(df['High'], df['Low'], df['Close'], timeperiod=3)
df['CDLDOJI']=ta.CDLDOJI(df['Open'],df['High'], df['Low'], df['Close'])
df['Yest_Close']=df['Close'].shift(+1)
df['delta']=df['Yest_Close']-df['Close']
df['delta_cl_op']=df['Yest_Close']-df['Open']
df['*']='*'
##df['MA']=[]  
##if (df['Simple MA_3'].any() > df['Simple MA_10'].any()  and (df['Close'].any() > df['Simple MA_3'].any()) and (df['Close'].any() > df['Simple MA_10'].any())):
##    df['MA']='(MA > MA10), (stock > MA3,MA10) - HIGH-HIGH'
####    df['MA']='oo'
##elif df['Simple MA_3'].any() > df['Simple MA_10'].any() and df['Close'].any() < df['Simple MA_3'].any() and df['Close'].any() > df['Simple MA_10'].any():
##    df['MA']='(MA3 > MA10), (MA10 < stock < MA3) - HIGH-Betweeen'
##elif  df['Simple MA_3'].any() > df['Simple MA_10'].any() and df['Simple MA_3'].any()  > df['Close'].any() and  df['Simple MA_10'].any()  > df['Close'].any():
##    df['MA']='(MA3 > MA10), (stock < MA3,MA10) - HIGH-LOWLOW'
##    
##elif  df['Simple MA_3'].any() < df['Simple MA_10'].any() and df['Close'].any() > df['Simple MA_10'].any() and df['Close'].any() < df['Simple MA_3'].any():
##    df['MA']='(MA3 < MA10), (MA3 < stock < MA10) - LOW-Between'
##elif df['Simple MA_3'].any() < df['Simple MA_10'].any() and df['Close'].any() < df['Simple MA_3'].any() and  df['Close'].any() < df['Simple MA_10'].any():
##    df['MA']='(MA3 < MA10), (stock < MA3,MA10) - LOW-LOWLOW'
##elif  df['Simple MA_3'].any() < df['Simple MA_10'].any() and df['Simple MA_10'].any()  < df['Close'].any() < df['Simple MA_3'].any():
##    df['MA']='(MA3 < MA10), (stock < MA3,MA10) - LOW-Between'
##else:
##    pass

df['EMA'] = ta.EMA(df['Close'], timeperiod = 4)
print(df)
##df = df.reindex(columns=['MA','Open', 'Simple MA_3', 'High', 'Yest_Close', 'ticker', 'CCI', 'MA_3>10', 'Simple MA_10', 'CDLDOJI', 'stream_WILLR', 'Day_swing', '*', 'delta', 'delta_cl_op', 'EMA', 'Close', 'Volume', 'Date', 'Low', 'day', 'Adj Close'])
##df=df[['MA','Date','day','ticker','Close','*','delta','Day_swing','delta_cl_op','CCI','Open', 'High', 'Low', 'Adj Close', 'Volume', 'ticker','Yest_Close',
##       'Simple MA_3', 'Simple MA_10', 'MA_3>10', 
##       'stream_WILLR', 'CDLDOJI', 'EMA']]   
print(df.columns.tolist())

##import pandas_datareader.data as web
##import datetime
##import talib as ta
##
##start = datetime.datetime.strptime('12/1/2015', '%m/%d/%Y')
##end = datetime.datetime.strptime('2/20/2016', '%m/%d/%Y')
##f = web.DataReader('GOOG', 'yahoo', start, end)
##print ('Closing Prices',ta.RSI(f.Close,2))
####print f['Close'].describe()
####print f.Close
####print ta.RSI(f.Close,2)
####print ta.SMA(f.Close,2)
####print ta.SMA(f.Volume,4)
####print ta.ATR
####print ta.ATR(f.High,f.Low,f.Close,3)
