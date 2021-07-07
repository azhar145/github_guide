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

print('\n',' 1- day    ',g,'\n')

########################################################################################################################################
########################################################## Hourly ##################################################

perda='1d'
intervla='60m'


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


print(df2.tail(5))

print('\n',' 1- day    ',g,'\n')

########################################################################################################################################

