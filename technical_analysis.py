
##import yfinance as yf
##import pandas as pd
##from ta.utils import dropna
##from ta.volatility import BollingerBands
##from ta import add_all_ta_features  


# https://www.tradersinsight.news/ibkr-quant-news/technical-analysis-with-python/
import yahoo_fin.stock_info as si
import pandas as pd
from ta import add_all_ta_features

# pull data from Yahoo Finance
df = si.get_data('aapl')

pd.options.display.max_columns=25
pd.options.display.max_rows=1500000

##df = yf.download('AAPL', '2019-1-1','2019-12-27')
# Initialize Bollinger Bands Indicator
##indicator_bb = BollingerBands(close=df["Close"], window=20, window_dev=2)
### Add Bollinger Bands features
##df['bb_bbm'] = indicator_bb.bollinger_mavg()
##df['bb_bbh'] = indicator_bb.bollinger_hband()
##df['bb_bbl'] = indicator_bb.bollinger_lband()
### Add Bollinger Band high indicator
##df['bb_bbhi'] = indicator_bb.bollinger_hband_indicator()
### Add Bollinger Band low indicator
##df['bb_bbli'] = indicator_bb.bollinger_lband_indicator()
##
####dfa=pd.concat([df['bb_bbm'],df['bb_bbh'],df['bb_bbl'],df['bb_bbhi'],df['bb_bbli']],axis=1)
####print(dfa)
##print(df)

df= add_all_ta_features(df,open='open', high='high', low='low', close='adjclose', volume='volume')

print(df[['open', 'high', 'low', 'close', 'adjclose', 'volume', 'ticker']],df.momentum_stoch_signal.tail(),df.momentum_ppo_signal.tail())
