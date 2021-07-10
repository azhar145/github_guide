import yfinance as yf
import pandas as pd
import numpy as np
##import plotly.graph_objs as go

##############################################################  
#define the ticker symbol
##tickerSymbol = 'MSFT'
##
###get data on this ticker
##tickerData = yf.Ticker(tickerSymbol)
##tickerData.calendar
##tickerData.recommendations
##tickerData.actions
###get the historical prices for this ticker
##tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2021-5-25')
##
###see your data
####print(tickerDf.head(3))
####print(tickerData.calendar)
##
##
##tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')
##print(tickerDf)
##############################################################

##data = yf.download(tickers='ndx', period='5d', interval='5m')
###Print data
##print(data.iloc[:,[4,5]])

# Import the plotting library 
import matplotlib.pyplot as plt 
 
# Import the yfinance. If you get module not found error the run !pip install yfiannce from your Jupyter notebook 
import yfinance as yf   
 
# Get the data of the stock AAPL 
data = yf.download('AAPL','2016-01-01','2018-01-01') 
 
# Plot the close price of the AAPL 
data.Close.plot() 
plt.show() 
