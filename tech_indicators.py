# load packages
import yahoo_fin.stock_info as si
import pandas as pd
from ta import add_all_ta_features
from ta.momentum import RSIIndicator
from ta.trend import macd
 
##tkr=input("Enter stock ticker: ")

# pull data from Yahoo Finance
data = si.get_data("T")
# add technical analysis features
data = add_all_ta_features(
    data, open="open", high="high", low="low", close="adjclose", volume="volume")

rsi_21 = RSIIndicator(close = data.adjclose, window = 21)
 
##data["rsi_21"] = rsi_21.rsi()
##data["macd"] = macd(data.adjclose, window_slow = 26, window_fast = 12)

print('  ',rsi_21)


##################################
import pandas as pd
from ta.utils import dropna
from ta.volatility import BollingerBands


# Load datas
df = pd.read_csv('ta/tests/data/datas.csv', sep=',')

# Clean NaN values
df = dropna(df)

# Initialize Bollinger Bands Indicator
indicator_bb = BollingerBands(close=df["Close"], window=20, window_dev=2)

# Add Bollinger Bands features
df['bb_bbm'] = indicator_bb.bollinger_mavg()
df['bb_bbh'] = indicator_bb.bollinger_hband()
df['bb_bbl'] = indicator_bb.bollinger_lband()

# Add Bollinger Band high indicator
df['bb_bbhi'] = indicator_bb.bollinger_hband_indicator()

# Add Bollinger Band low indicator
df['bb_bbli'] = indicator_bb.bollinger_lband_indicator()

# Add Width Size Bollinger Bands
df['bb_bbw'] = indicator_bb.bollinger_wband()

# Add Percentage Bollinger Bands
df['bb_bbp'] = indicator_bb.bollinger_pband()

##############################3
import pandas as pd
import ta

# Load data
df = pd.read_csv("../test/data/datas.csv", sep=",")

# Clean nan values
df = ta.utils.dropna(df)

window = 12
df[f"roc_{window}"] = ta.momentum.ROCIndicator(close=df["Close"], window=window).roc()



#################################

# https://github.com/bukosabino/ta/blob/master/examples_to_use/visualize_features.ipynb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('seaborn')

# Load data
df = pd.read_csv('../test/data/datas.csv', sep=',')
df = ta.utils.dropna(df)

plt.plot(df[40500:41000].Close)
plt.plot(df[40700:41000].volatility_bbh, label='High BB')
plt.plot(df[40700:41000].volatility_bbl, label='Low BB')
plt.plot(df[40700:41000].volatility_bbm, label='EMA BB')
plt.title('Bollinger Bands')
plt.legend()
plt.show()



plt.plot(df[40500: 41000].Close)
plt.plot(df[40500: 41000].volatility_dch, label='High DC')
plt.plot(df[40500: 41000].volatility_dcl, label='Low DC')
plt.title('Donchian Channel')
plt.legend()
plt.show()


plt.plot(df[40500:41000].trend_macd, label='MACD')
plt.plot(df[40500:41000].trend_macd_signal, label='MACD Signal')
plt.plot(df[40500:41000].trend_macd_diff, label='MACD Difference')
plt.title('MACD, MACD Signal and MACD Difference')
plt.legend()
plt.show()



plt.plot(df[40700:41000].trend_kst, label='KST')
plt.plot(df[40700:41000].trend_kst_sig, label='KST Signal')
plt.plot(df[40700:41000].trend_kst_diff, label='KST - KST Signal')
plt.title('Know Sure Thing (KST)')
plt.legend()
plt.show()

import ta
