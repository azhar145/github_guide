'''
import requests
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
print(data)
import pandas.io.formats.style
data = response.json()
print(data["bpi"]["USD"]["rate"])


#from colorama import Fore, Back, Style
import seaborn as sns
cm = sns.diverging_palette(-5, 5, as_cmap=True)
'''
##############################
####################################
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

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go
df = yf.download(tickers='BTC-USD', period = '42h', interval = '15m')
df.reset_index(inplace=True)
df['x']=df['Datetime'].dt.time
df['d']=df['Datetime'].dt.day_name()
df['u']=df['Datetime'].dt.date
print(df.columns)
df=df[[
    'x','d','u','Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]


print(df)
#print(Fore.RED + df.loc[:5,:]+Stlye.RESET_ALL)


#print(Fore.RED + 'jjjj')
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL)
#print('back to normal now')


#df=df.style.background_gradient(cmap="Blues")
#Fore.RED
#print(df.loc[:12,:])
#Style.RESET_ALL




'''
    if x < 130:
        print(x,'   ',df['Close'].loc[x].round(2),'         ',df['Volume'].loc[x])

    else:
        print(Back.YELLOW)

        print(x,'   ',df['Close'].loc[x].round(2),'         ',df['Volume'].loc[x])
        print(Style.RESET_ALL)

'''
#    if x < 12:
#        print(Back.YELLOW)
#        print(df[x])
#        print(Sytle.RESET_ALL)
#    else:    
#        print(df[x])
