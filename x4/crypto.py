# Raw Package
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore, Back, Style

from IPython.display import HTML
from datetime import time
from numerize import numerize
from colorama import Fore, Back, Style

import pandas as pd
from yahoo_fin import stock_info as f
import textwrap
#pd.set_option("max_colwidth", 12)
from yahoo_fin import news as g
import html5lib
import numpy as np
from numerize import numerize
pd.options.display.max_columns = 50
pd.options.display.max_rows = 1000
#pd.options.display.max_colwidth =180
pd.set_option('display.max_colwidth', 26)
pd.set_option("display.expand_frame_repr", False)


def hourly():
    #Data Source
    import yfinance as yf
    #Data viz
    import numpy as np
    from numerize import numerize
    import plotly.graph_objs as go
    df = yf.download(tickers='BTC-USD', period = '42h', interval = '15m')
    df.reset_index(inplace=True)
    df['x']=df['Datetime'].dt.time
    df['d']=df['Datetime'].dt.day_name()
    df['u']=df['Datetime'].dt.date
    print(df.columns)
    df=df[[
    'x','d','u', 'Close', 'Adj Close', 'Volume']]

    #df['Open']=df['Open'].round(0)
    #df['High']=df['High'].round(0)
    #df['Low']=df['Low'].round(0)
    df['Close']=df['Close'].round(0)
    df['Adj Close']=df['Adj Close'].round(0)
    df['Adj Close_1_hr']=df['Adj Close'].shift(4)
    df['Adj Close_24_hr']=df['Adj Close'].shift(24)
    df['7day']=df['Adj Close'].shift(168)
    df['7day_delta']=df['Adj Close']-df['7day']
    
    for x in df.index:
                        df['Volume'].loc[x]=numerize.numerize(np.float32(df['Volume'].loc[x]).item())

 #   df['Volume']=df['Volume'].round(0)
    df['1hr_delta']=df['Adj Close']-df['Adj Close_1_hr']
    df['24hr_delta']=df['Adj Close']-df['Adj Close_24_hr']
    print(df.tail(22))
    print('\n')
    print("Above is hourly mtsr price (every 15 mins)")

#print(Fore.RED + df.loc[:5,:]+Stlye.RESET_ALL)


def day():
    import yfinance as yf
    #Data viz
    import plotly.graph_objs as go
    df = yf.download(tickers='BTC-USD', period = '4mo', interval = '1d')
    df2=yf.download(tickers='mstr', period = '4mo', interval = '1d')[['Open','Close','Volume']]
    df2.reset_index(inplace=True)
    df2['d']=df2['Date'].dt.day_name()
    df2['u']=df2['Date'].dt.date
    

   # df.reset_index(inplace=True)
   # df=df[['Date','Close', 'Adj Close', 'Volume']]
    df.reset_index(inplace=True)
    df['d']=df['Date'].dt.day_name()
    df['u']=df['Date'].dt.date
    df['Adj Close_1_dy']=df['Adj Close'].shift(1)
    df['Adj Close_7_dy']=df['Adj Close'].shift(7)

    df['1_dy_delta']=df['Adj Close']-df['Adj Close_1_dy']
    df['7_dy_delta']=df['Adj Close']-df['Adj Close_7_dy']
    df=df[['d','u', 'Low', 'Close', 'Adj Close', 'Volume', 
               'Adj Close_1_dy', 'Adj Close_7_dy', '1_dy_delta', '7_dy_delta'
                     ]]
    df['Low']=df['Low'].round(0)
    df['Close']=df['Close'].round(0)
    df['Adj Close']=df['Adj Close'].round(0)
    df['1_dy_delta']=df['1_dy_delta'].round(0)
    df['7_dy_delta']=df['7_dy_delta'].round(0)
    df['Adj Close_1_dy']=df['Adj Close_1_dy'].round(0)
    df['Adj Close_7_dy']=df['Adj Close_7_dy'].round(0)
    df=df.tail(120)
#    print(df.tail(120))
    print('\n\n')
    df2=df2[['u','Close','Volume']]
    df2=df2.tail(120)
#    print(df2.tail(120))
    df3=pd.concat([df,df2],axis=1)
    df4= pd.merge(left=df, right=df2, on="u")
  

    print('\n\n')
    df4.rename(columns={'Close_y':'MSTR_close','Volume_y': 'MSTR_volume'},inplace=True)
    df4['MSTR_close']=df4['MSTR_close'].round(0)
    for x in df4.index:
                df4['Volume_x'].loc[x]=numerize.numerize(np.float32(df4['Volume_x'].loc[x]).item())
                df4['MSTR_volume'].loc[x]=numerize.numerize(np.float32(df4['MSTR_volume'].loc[x]).item()) 



    print(df4.tail(30))
    print('\n')
    print("Above is daily bitcoin price and daily mtsr stock price")
def stocks():
    import pandas as pd
    pd.options.display.max_rows=9999
    pd.options.display.max_columns=15
    pd.set_option("display.max_columns", 100)
    pd.set_option('display.width', 1000)
#    tickers_list=input("Enter ticker: ").upper()
    #tickers_list='^NDX'
    #tickers_list='MELI'
    #tickers_list='ISRG' 

    #tickers_list = ['NDX']
    ##########################################################################################################

    import numpy,datetime
    import sys
    import calendar
    # Fetch the data
    import yfinance as yf
    import textwrap
    wrapper = textwrap.TextWrapper(width=100)
    import yahoo_fin
    from yahoo_fin import stock_info

    tickers_list='mstr'
    data = yf.download(tickers_list,'2020-10-1')[['Open','Close','Volume']]
    df=pd.DataFrame(data)
    #print(df.head)
    df.reset_index(drop=False,inplace=True)
    df.style.set_properties(subset=['text'], **{'width': '300px'})
    df['Close']=df['Close'].round(0)

    print(df.tail(10)) 
    d1=[]
    for x in range(df.shape[0]):
            d1[x]=d1.append("X")

            df['ticker']=tickers_list
            #df['ticker']=tickers_list[0]
            df['up_down']=df['Close']-df['Open']
            #df['z']=calendar.day_name[df['Date'].weekday()]
            df['day']=df['Date'].dt.day_name()
            df['Datea']=df['Date'].dt.date
hourly()
day()
#stocks()
