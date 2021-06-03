# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

#Data viz
##import plotly.graph_objs as go

pd.options.display.max_rows=9999
pd.options.display.max_columns=15
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)



g='TSLA'
perd='2d'
intervl='1m'

# [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]

##g=input("Enter Ticker :")
#perd=input("Enter no of days '5d','2d','1d' :")
#intervl=input("Enter mins '5m','1m' :")


#df=pd.DataFrame()
#Interval required 5 minutes
data = yf.download(tickers=g, period=perd, interval=intervl)

df=pd.DataFrame(data)
df3=pd.DataFrame()
k=1

for x in range(df.shape[0]):
    df3[x]=([df.iloc[x,2],df.iloc[x,1],df.iloc[x,3]])
    
    k=k+1
    if k > 7:
        break

df3=df3.T
print(df3)

##
##df=pd.DataFrame(data)
###print(df.tail(5)) 
##df.reset_index(drop=False,inplace=True)
###df.set_index()
###print(df.shape[0],'   ','\n\n',df.tail(5)) 
###dp=pd.DataFrame()
##dp=pd.DataFrame()
##for x in range(df.shape[0]):
##    dp=dp.append(df.iloc[x,[0,1]])
##
###    dp[x]=pd.DataFrame([df.iloc[x,0],df.iloc[x,5],df.iloc[x,6]/1000])
##    #dp=pd.DataFrame([df.iloc[x,0],df.iloc[x,5]])
###  print(df.iloc[x,0],df.iloc[x,5],df.iloc[x,6]/1000)
##print('\n\n\n')
###print(dp)
##dp=pd.DataFrame(dp)
##dp.columns=['a','b']
###print(dp)
##
##d=[]
##for x in range(dp.shape[0]):
##    d.append(g)
##
##
##df4=pd.DataFrame(d)
###print(df4)
##df4.columns=['Ticker']
##print(df4['Ticker'],df4['Ticker'].shift(-2))
##
##
##
##df3=pd.concat([df4,dp],axis=1)
##
##df4=pd.DataFrame([df3['a'],df3['b']/10,df3['a']])
##df4=df4.T
####print(df4)
##
####df5=pd.DataFrame([df3['b'],df3['b'].round(2)/225,df3.iloc[:,1],df3.iloc[:,2],df3.iloc[:,0]+
####                  'dddd'+df3.iloc[:,1]])
####print('df5:','\n\n',df5.T)
##
##
##print('\n\n')
##
###print(df3.tail(8))
##
