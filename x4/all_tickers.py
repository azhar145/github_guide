import plotly.graph_objs as go
import pandas as pd
import yfinance as yf
import numpy as np
from datetime import time
from numerize import numerize
import time

pd.options.display.max_rows=9999
pd.options.display.max_columns=26
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)



def ff(g):
    import yfinance as yf
    import pandas as pd
    import numpy as np
    import datetime
    from datetime import time
    from numerize import numerize
    df=pd.DataFrame()
    print('   ','inside def ',yf.download(g, start='2021-07-02', end='2021-07-21'))
###====================================
i=0
k=0
df=pd.DataFrame()
df2=pd.DataFrame()
f = open('/home/ec2-user/environment/x3/stocks/x4/lista.txt','r')
for p in f.read().strip().split('\n'):

    i=i+1
    if len(p) > 0:

        df=yf.download(p, period='2d')
        if df.size==0:
            pass
        print(i,'   ',df.size)
        print(p,' ----->  ',df.shape)
        df.reset_index(inplace=True)
        df['ticker']=p
        df=df.drop_duplicates(subset=['Date','ticker'], keep='first', inplace=False, ignore_index=False)
        df2=df2.append(df)
        df2['Open']=df2['Open'].round(2)
        df2['Close']=df2['Close'].round(2)
        df2['Low']=df2['Low'].round(2)
        df2['High']=df2['High'].round(2)
        df2['Adj Close']=df2['Adj Close'].round(2)
        df2['Volume']=(df2['Volume'])
        df2['ticker']=df['ticker']
        k=k+1
        if k==270:
            k=0
            print("----------------- sleep for 3 secs -----------------")
            time.sleep(3)
f.close()

df3=pd.DataFrame()
df3=df2
df3['bx']=''


for x in df3.index:
    df3['Volume'].loc[x]=df3['Volume'].loc[x]
    df3['bx'].loc[x]=df3['Volume'].loc[x]
    
    if len(df3['Volume'].loc[x]) == 8:
        df3['bx'].loc[x]=numerize.numerize(np.float32(df3['Volume'].loc[x]).item())
    else:
        pass
df3.reset_index(inplace=True)
for x in df3.index:
#    print(x)
    df3['bx'].loc[x]=numerize.numerize((df3['bx'].loc[x]))
print('no of tickes in text file, i=',i,'\n\n',df3)



