import pandas as pd
pd.options.display.max_rows=9999
pd.options.display.max_columns=15
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)
tickers_list=input("Enter ticker: ").upper()
#tickers_list='^NDX'
#tickers_list='MELI'
#tickers_list='ISRG' 

#tickers_list = ['NDX']
##########################################################################################################

import numpy,datetime
import sys
import calendar
# Fetch the data
import yfinance as yf
import textwrap
wrapper = textwrap.TextWrapper(width=100)
import yahoo_fin
from yahoo_fin import stock_info






data = yf.download(tickers_list,'2020-10-1')[['Open','Close','Volume']]
df=pd.DataFrame(data)
#print(df.head)
df.reset_index(drop=False,inplace=True)
df.style.set_properties(subset=['text'], **{'width': '300px'})


d1=[]
for x in range(df.shape[0]):
    d1[x]=d1.append("X")

df['ticker']=tickers_list
#df['ticker']=tickers_list[0]
df['up_down']=df['Close']-df['Open']
#df['z']=calendar.day_name[df['Date'].weekday()]
df['day']=df['Date'].dt.weekday_name
df['Datea']=df['Date'].dt.date


#df=df.iloc[1:]
#tt=df.shape[0]+1
#df.loc[len(df)]=['8','8','5','ttt','0']

#df.reset_index(drop=False,inplace=True)
#print(df.tail(4))

#df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
#df['Datea']=pd.to_datetime(df['Date'])

#df['Date'] = pd.to_datetime(df.Date, format='%Y-%m-%d')
#print(df['Date'])
#ts = pd.to_datetime(pd.Series(str(df['Date']))) 
#print(ts)
#d = ts.strftime('%m.%d')
#b1=d
#print(b1)
#b1=(pd.Series(df['Date']))
b1=df['Datea']
b2=df['ticker']
b3=df['up_down'].astype(int)
b4=df['Open'].astype(int)
b5=df['Close'].astype(int)
#b6=df['Date'].dt.weekday_name
b6=df['day']
#b6['p']=b6['Date'].split()[1]
b7=df['Volume']
#print(b1,'******',b6)
'''
print(type(pd.Series(df['Date'].dtype)))
print(type(df['ticker']))
print(type(df['up_down'].astype(int)))
print(type(df['Open'].astype(int)))
print(type(df['Close'].astype(int)))
'''
aa=pd.concat([b1,b6,b2,b3,b4,b5,b7],axis=1)
aa.loc[len(aa)]=['','','8','8','5','ttt','0']
aa=aa[1:]
#print(aa.columns)

#print(aa)
#aa=pd.concat(pd.Series(df['Date'].dtype),df['ticker'])
#aa=pd.concat(([pd.Series(df['Date'].dtype)),df['Date'].dt.weekday_name,df['ticker'],df['up_down'].astype(int),df['Open'].astype(int),df['Close'].astype(int)])
#print(aa)
#######################################################################################################



'''
#print(df.index)
#aa=pd.concat([df['Date'],df['Date'].dt.day_name(),df['ticker'],df['up_down'].astype(int),df['Open'].astype(int),df['Close'].astype(int),df['Volume']/1000000],axis=1)
#aa.append("",'test','x')

#print(aa.columns)
'''


#bb2=df['Close'].astype(int)
bb2=df
bb=bb2.iloc[0:]
#bb2.drop(bb2.index[:0],inplace=True)
bb.reset_index(inplace=True,drop=True)
#print(bb.head(3))
#bb.append([['','','test','','','','']],ignore_index=True)
#bb=bb.T
#bb[rowsa]=["z","z","dd","2","2","2","2"]
#bb=bb.T
#print(bb.index)
##bb=pd.DataFrame([['','','mmm','','','','']],columns=['Date','Date','ticker','up_down','Open','Close','Volume'])
#bb.append("",'test','x','','','',''])
#print(bb)
bb=bb['Close'].astype(int)
#print(bb)
#print(aa.head(4))
'''
aa=aa[4:]
bb=bb[3:]
'''
#gg=pd.concat([aa,bb],axis=1)
#gg=pd.concat([aa[1:],bb['Close'][0:]],axis=1)
#print(gg)        





'''
#cc=pd.merge(aa,bb,how='inner',left_index=True, 
  right_index=True)
#cc=aa.merge(bb, how='inner', on=None, left_on=None, right_on=None, left_index=True, right_index=True, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
'''



#print(aa.head(4),bb[1:].head(4))
#aa=aa[1:]
aa.reset_index(inplace=True,drop=True)

cc=pd.merge(aa,bb, left_index=True, right_index=True)
#cc=bb.join(aa)
#cc=pd.merge([aa,bb],right,how='inner',on=None,left_index=True,right_index=False, left_on=None, right_on=None)

cc['nxtday_delta']=cc['Open'].astype(int)-cc['Close_y'].astype(int)
cc.drop(cc.index[cc.shape[0]-1],inplace=True) 
cc['cl_cl_delta']=cc['Close_x'].astype(int)-cc["Close_y"].astype(int)

p=10
#cc=cc.query('abs(nxtday_delta) < abs(20)' and 'abs(cl_cl_delta) < abs(20)' and 'abs(up_down) < abs(20)')
#cc=cc.query('abs(nxtday_delta)  < 300')
#cc=cc.query('abs(up_down)  < 300')
#cc=cc.query('abs(cl_cl_delta)  < 300')

print(cc)
###########################################################
dd=cc.tail(14)
print(dd)
Next_day_delta_close_to_open=abs(dd['nxtday_delta']).sort_values(axis=0, ascending=True)
print('Next_day_delta_close_to_open (yesterday close,todays open delta','\n')
print('Mean ',Next_day_delta_close_to_open.mean())
print('Max  ',Next_day_delta_close_to_open.max())
print('min  ',Next_day_delta_close_to_open.min())
print('count ',Next_day_delta_close_to_open.count())  
##########################################################
daily_up_down=abs(dd['up_down']).sort_values(axis=0, ascending=True, inplace=False)
print('\n','daily_up_down (same day): ','\n')
print('Mean ',daily_up_down.mean())
print('Max ',daily_up_down.max())
print('min ',daily_up_down.min())
print('count ',daily_up_down.count())
print('###########################################################################################################') 
print('cl_cl_delta')
#print(b2,'   ',b1,'   ',abs(cc['cl_cl_delta']).sort_values(axis=0, ascending=True, inplace=False))
cl_cl_delta=abs(dd['cl_cl_delta']).sort_values(axis=0, ascending=True, inplace=False)
print('\n','daily_up_down (same day): ','\n')
print('Mean ',cl_cl_delta.mean())
print('Max ',cl_cl_delta.max())
print('min ',cl_cl_delta.min())
print('count ',cl_cl_delta.count())
print('###########################################################################################################') 
########################################################################################################################
########################################################################################################################


dedented_text = textwrap.dedent(str(cc))
#print(cc.query=('cl_cl_delta' < 300))
print("marker")

 #print(cc)
#print(dedented_text)
 #print(df)
 
print('\n\n\n')
#print(abs(cc['cl_cl_delta']).sort_values(axis=0, ascending=True, inplace=False))
print('###########################################################################################################')
print('Next_day_delta_close_to_open (yesterday close, todays open delta')
#print(pd.concat(b2,abs(cc['nxtday_delta']),axis=0))
#print(type(b2))
#b2=b2.astype('Int64')
#Next_day_delta_close_to_open=Next_day_delta_close_to_open.astype('Int64')
Next_day_delta_close_to_open=abs(cc['nxtday_delta']).sort_values(axis=0, ascending=True)
#print(type(Next_day_delta_close_to_open))
print('Next_day_delta_close_to_open (yesterday close,todays open delta','\n')
print('Mean ',Next_day_delta_close_to_open.mean())
print('Max  ',Next_day_delta_close_to_open.max())
print('min  ',Next_day_delta_close_to_open.min())
print('count ',Next_day_delta_close_to_open.count())  
print('###########################################################################################################')   
print('\n\n\n')

print('up_down (same day)')
#print(b2,'   ',b1,'    ', abs(cc['up_down']).sort_values(axis=0, ascending=True, inplace=False))
daily_up_down=abs(cc['up_down']).sort_values(axis=0, ascending=True, inplace=False)
print('\n','daily_up_down (same day): ','\n')
print('Mean ',daily_up_down.mean())
print('Max ',daily_up_down.max())
print('min ',daily_up_down.min())
print('count ',daily_up_down.count())
print('###########################################################################################################')  
print('\n\n\n')
print('cl_cl_delta')
#print(b2,'   ',b1,'   ',abs(cc['cl_cl_delta']).sort_values(axis=0, ascending=True, inplace=False))
cl_cl_delta=abs(cc['cl_cl_delta']).sort_values(axis=0, ascending=True, inplace=False)
print('\n','daily_up_down (same day): ','\n')
print('Mean ',cl_cl_delta.mean())
print('Max ',cl_cl_delta.max())
print('min ',cl_cl_delta.min())
print('count ',cl_cl_delta.count())
print('###########################################################################################################') 
print(cl_cl_delta.shape)
#k=1
#print(cc['cl_cl_delta'].index)
#while (k < abs(cc['cl_cl_dleta']).shape[0]):
#    if abs(cc[cl_cl_delta]).iloc[k,6]> 300:

#        k=k+1
#print('Out of ',cc['cl_cl_delta'].shape[0],' we have cl_cl_dleta ', k, '  times >')






#html = cc.to_html()
#print(html)
 #print(cc[:cc.shape[0]-1i



'''







##################################     Moving Average #####################################################



#print(len(cc['Close_x']))
######################################################################################
numbers=cc['Close_x']
window_size =5

i = 0
moving_averages = []
while i < len(numbers) - window_size :
    
    this_window = numbers[i : i + window_size ]
    

    window_average = sum(this_window) / window_size
    
    moving_averages.append(window_average)
##    print('*** ',i,len(numbers),window_size,this_window,'*',window_average,'**',moving_averages)
    i += 1

d1=[]
for x in range(len(numbers)):
    
    if x >= window_size:
        d1.append(numbers[x])

d2=[]
k1=0

print('\n')

print('\n')

#for x in range(window_size,len(numbers)):
##    if x >= window_size:
#    print(x,numbers[x],moving_averages[x-window_size])
###########################################################################################
numbers=cc['Close_x']
window_size13 =20 

i = 0
moving_averages13 = []
while i < len(numbers) - window_size13 :
    
    this_window13 = numbers[i : i + window_size13 ]
    

    window_average13 = sum(this_window13) / window_size13
    
    moving_averages13.append(window_average13)
##    print('*** ',i,len(numbers),window_size,this_window,'*',window_average,'**',moving_averages)
    i += 1

d1=[]
for x in range(len(numbers)):
    
    if x >= window_size13:
        d1.append(numbers[x])

d2=[]
k1=0

print('\n')

print('\n')

for x in range(window_size13,len(numbers)):
##    if x >= window_size:
    if int(numbers[x]) - int(moving_averages13[x-window_size13]) == 0 or int(numbers[x]) - int(moving_averages[x-window_size]) == 0 or int(moving_averages13[x-window_size13])-int(moving_averages[x-window_size]) == 0:
       print('********************************************************************************************************','\n')
       print(x,'$$$$$$$$$  crossing over---- (',int(numbers[x]) - int(moving_averages13[x-window_size13]),',',(int(numbers[x]) -
           int(moving_averages13[x-window_size13]),')',numbers[x],'(stock_price)',
           moving_averages13[x-window_size13],'(20d)',moving_averages[x-window_size],'(5d) $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'))
       print('\n','********************************************************************************************************')                                                                                                                            
    #   print("Crossing over")
    elif (moving_averages[x-window_size]) - (moving_averages13[x-window_size13]) > 0 and numbers[x] > (moving_averages[x-window_size]): 
        print(x,' ---- ',numbers[x],'(stock_price)',moving_averages[x-window_size],'(5d)',moving_averages13[x-window_size13],'(20d)',
                '  ',str('*********** 5d > 20d ** price > 5d,20d ******** Above ds ********* '))
   #     if ( numbers[x] - int(moving_averages13[x-window_size13])) < 0.5 or (numbers[x] - int(moving_averages13[x-window_size13])) < -0.5:  
   #        print("Crossing over")   
    elif int(moving_averages[x-window_size]) - int(moving_averages13[x-window_size13]) > 0  and numbers[x] < int(moving_averages[x-window_size]) and numbers[x] > int(moving_averages13[x-window_size13]):
        print(x,'  ',numbers[x],'(stock_price)',moving_averages[x-window_size],'(5d)', moving_averages13[x-window_size13],'(20d)',
                 '  ',str('*********** 5d > 20d **  20d < price < 5d ******** Between (5d > 20d) ********* '))
 #               str('5d > 20d'),'  ',str('20d < price < 5d'))
   #     if ( numbers[x] - int(moving_averages13[x-window_size13])) < 0.5 or (numbers[x] - int(moving_averages13[x-window_size13])) < -0.5:
        
   #        print("Crossing over")
    elif int(moving_averages[x-window_size]) - int(moving_averages13[x-window_size13]) > 0  and numbers[x] < int(moving_averages13[x-window_size13]) and numbers[x] < int(moving_averages[x-window_size]):
         print(x,'   ',numbers[x],'(stock_price)',moving_averages[x-window_size],'(5d)',moving_averages13[x-window_size13],'(20d)',str('5d > 20d'),'  ',str('price < 5d,20d'))
  
    elif int(moving_averages[x-window_size]) - int(moving_averages13[x-window_size13]) < 0 and numbers[x] < int(moving_averages[x-window_size]) and numbers[x] > int(moving_averages13[x-window_size13]):
         print(x,'   ',numbers[x],'(stock_price)', moving_averages[x-window_size],'(5d)',moving_averages13[x-window_size13],'(20d)',str('5d < 20d'),'  ',str('20d < price <5d '))
    elif (moving_averages[x-window_size]) - (moving_averages13[x-window_size13]) < 0 and numbers[x] < (moving_averages[x-window_size]) and numbers[x] < (moving_averages13[x-window_size13]):
         print(x,' ---- ',numbers[x],'(stock_price)',moving_averages[x-window_size],'(5d)',moving_averages13[x-window_size13],'(20d)','  ',str('*********** 5d < 20d ** price < 5d,20d ******** Below ds ********* ')) 
## ***********************************
    elif (moving_averages[x-window_size]) - (moving_averages13[x-window_size13]) < 0 and numbers[x] > (moving_averages[x-window_size]
            and numbers[x] > moving_averages13[x-window_size13]):
         print(x,' new ',numbers[x],'(stock_price)',moving_averages[x-window_size],'(5d)',moving_averages13[x-window_size13],'(20d)'
                '  ',str('*********** 5d < 20d **   price > 5d,20d ******** Below/Above (5d < 20d) ********* ')
                 )
    elif (moving_averages[x-window_size]) - (moving_averages13[x-window_size13]) < 0 and numbers[x] > (moving_averages[x-window_size]
        and numbers[x] < moving_averages13[x-window_size13]):

        print(x,' new ',numbers[x],'(stock_price)',moving_averages[x-window_size],'(5d)',moving_averages13[x-window_size13],'(20d)'
                 '  ',str('*********** 5d < 20d ** 5d < price > 20d ******** Below/Between (5d < 20d) ********* ')                       
                  )

    elif (moving_averages[x-window_size]) - (moving_averages13[x-window_size13]) < 0 and numbers[x] < (moving_averages[x-window_size]
         and numbers[x] < moving_averages13[x-window_size13]):
 
         print(x,' new ',numbers[x],'(stock_price)',moving_averages[x-window_size],'(5d)',moving_averages13[x-window_size13],'(20d)'
                  '  ',str('*********** 5d < 20d ** 5d,20d < price  ******** Below/Below (5d < 20d) ********* ')                    
                   )        
## ***********************************         
        

#   f ( numbers[x] - int(moving_averages13[x-window_size13])) < 0.5 or (numbers[x] - int(moving_averages13[x-window_size13])) < -0.5:
#         print("Crossing over")          


 #   elif int(moving_averages[x-window_size]) - int(moving_averages13[x-window_size13]) > 0 and x >  int(moving_averages[x-window_size]) and x < int(moving_averages13[x-window_size13]): 
 #      print(x,numbers[x],moving_averages13[x-window_size13],'     ',moving_averages[x-window_size],str('5d > 20d'),'  ',str('price higher'))     
    else: print(x,' check  ',numbers[x],'(stock_price)', moving_averages[x-window_size],'(5d)',moving_averages13[x-window_size13],'(20d)') 
#    print(x,numbers[x],moving_averages13[x-window_size13],'     ',moving_averages[x-window_size], str('Downtrend'),str('price between'))    
###########################################################################################

#print(cc)







#print(cc)
#print(dedented_text)
#print(df)

print('\n\n\n')
#print(abs(cc['cl_cl_delta']).sort_values(axis=0, ascending=True, inplace=False),'   ',abs(cc['nxtday_delta']).sort_values(axis=0, ascending=True, inplace=False))

#print(abs(cc['up_down']).sort_values(axis=0, ascending=True, inplace=False))

#html = cc.to_html()
#print(html)
#print(cc[:cc.shape[0]-1i

#df = yahoo_fin.stock_info.get_data('a', interval='1d')
#moving_average = [df['close'][i-5:i].mean() for i in range(5, df.shape[0]+1)]
#print(moving_average,df['close'],'\n')
#for i in range (5,df.shape[0]+1):
#    moving_average = [df['close'][i-5:i].mean()
#    print(df['close'],moving_average,'\n')
###############################################
# tina 
#import yfinance as yf
#data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")


#data2=pd.get_data_yahoo(tickers="SPY",period='5d',interval="1m",prepost = True,threads = True)
#print(data2)

#############################################


import yfinance as yf
msft = yf.Ticker(tickers_list)

# get stock info
#print(msft.recommendations.sort_values(by='Date'))
print('\n\n\n\n')

print(msft.options)
print('\n\n\n\n')
opt = msft.option_chain('2021-05-14')
df2=pd.DataFrame(opt)

print(df2)

#print('\n\n\n\n')
#print(msft.major_holders)
#print('\n\n\n\n')
#rint(msft.institutional_holders)
#print('\n\n\n\n')
#print(msft.sustainability)
#print('\n\n\n\n')
#print(msft.calendar)
###################################################################
#from yahoo_fin import options
#print(get_calls('nflx', '06/19/2020'))
import yahoo_fin
from yahoo_fin import options
from yahoo_fin import news
 
#print(news.get_yf_rss("nflx"))
print('\n\n\n')
#print(get_expiration_dates('amzn'))
#print(news.get_yf_rss("nflx"))
#print(yahoo_fin.options.get_expiration_dates(tickers_list))
#print(yahoo_fin.options.get_options_chain(tickers_list, date=None, raw=True))
print(yahoo_fin.options.get_options_chain('amzn', date=None, raw=True))
'''
