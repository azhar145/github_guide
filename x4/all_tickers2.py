import plotly.graph_objs as go
import pandas as pd
import yfinance as yf
import numpy as np
from datetime import time
from numerize import numerize

pd.options.display.max_rows=9999
pd.options.display.max_columns=26
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)


########################################################## daily ##################################################

perda='2d'
intervla='1d'

g=['A','AA','AAC','AACG','AAIC','AAIC^B','AAIC^C','AAL','AAMC'
        ]

f = open('/home/ec2-user/environment/x3/stocks/x4/lista.txt','r')
i=0
for p in f:
    i=i+1
    uu=f.read()
    print(uu,'\n')


f.close()



'''
#g=input("Enter ticker: ")
perd=perda
intervl=intervla

# [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]


#df=pd.DataFrame()
#Interval required 5 minutes

df2=pd.DataFrame()
for x in g:
#    print(x)
#    df = yf.download(x, period=perd, interval=intervl,prepost = True)
    df = yf.download(x, period=perd,prepost = True)
    df.reset_index(inplace=True)
    df['ticker']=x
    df2=pd.concat([df2,df],axis=0)


df2['Close']=df2['Close'].round(2)
df2['Open']=df2['Open'].round(2)
df2['Low']=df2['Low'].round(2)
df2['High']=df2['High'].round(2)
df2['Adj Close']=df2['Adj Close'].round(2)

df2=df2.drop_duplicates(subset=['Date','ticker'], keep='first', inplace=False, ignore_index=False)

print(df2)
'''

