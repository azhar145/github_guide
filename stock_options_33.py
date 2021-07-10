from wallstreet import Stock, Call, Put

# stocks
s = Stock('AAPL')
s.price
s.change
s.last_trade


#options
g = Call('GOOG', d=12, m=2, y=2016, strike=700)
g.price
g.implied_volatility()
g.delta()
g.vega()
g.underlying.price



# combined.
g = Call('GOOG', d=12, m=2, y=2016)
g
Call(ticker=GOOG, expiration='12-02-2016')
g.strikes
(580, 610, 620, 630, 640, 650, 660, 670, 680, 690, 697.5, 700, 702.5, 707.5, 710, 712.5, 715, 720, ...)
g.set_strike(712.5)
g
Call(ticker=GOOG, expiration='12-02-2016', strike=712.5)

g = Put("GOOG")
g.expirations
