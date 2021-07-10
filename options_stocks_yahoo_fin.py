from yahoo_fin import options

# gets the data for nearest upcoming expiration date
options.get_option_chain("nflx")

# specific expiration date
options.get_options_chain("nflx", "04/26/2019")


# get call options only
options.get_calls("nflx", "04/26/2019")


# get put options only
options.get_puts("nflx", "04/26/2019")


###################################

from yahoo_fin import stock_info as si

# pulls historical OHLC data into a pandas data frame
si.get_data("nflx")

# or some other ticker
si.get_data("insert ticker here")
