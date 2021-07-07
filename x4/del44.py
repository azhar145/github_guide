import plotly.graph_objs as go
import pandas as pd
import yfinance as yf
import numpy as np
from datetime import time
from numerize import numerize
p='tsla'
df=yf.download(p, period='10d')
df.reset_index(inplace=True)
print(df)
df['dd']=''
for x in df.index:
#    df['dd'].loc[x]='ddd'+str(x)
    df['dd'].loc[x]=df['Volume'].loc[x]/2
#    df['dd'].loc[x]=df['dd'].loc[x].append('33')
    df['dd'].loc[x]=numerize.numerize(np.float32(df['Volume'].loc[x]).item())
print(df)
