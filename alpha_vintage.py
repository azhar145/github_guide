
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import pandas as pd

pd.options.display.max_rows=9999
pd.options.display.max_columns=15
df=pd.DataFrame()
d1=[]

ts = TimeSeries(key='MUY7K7XOWL48HELB', output_format='pandas')
##data, meta_data = ts.get_intraday(symbol='AMZN',interval='1day', outputsize='full')
print(ts.get_intraday(symbol='NDX',interval='hourly',outputsize='full'))
##print(ts.get_daily('^SPX',outputsize='full'))
##df=pd.DataFrame(data)
##
##
##print(df)

##
##for x in range(df.shape[0]):
##    d1=d1.append(df['open'].str)

##print(df.shape)
##df=df.append(d1, ignore_index=True)
##print(df.shape)
##print(df.head(4))

##data['close'].plot()
##plt.title('Intraday Times Series for the MSFT stock (1 min)')
##plt.show()
