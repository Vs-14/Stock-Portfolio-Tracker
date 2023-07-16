from django.shortcuts import render
from alpha_vantage.timeseries import TimeSeries
import plotly.express as ex
from keys import MY_KEY
api_key = MY_KEY

# Create your views here.
def symbol(request):
    ticker = request.POST.get('stock')
    ts = TimeSeries(key=api_key,output_format='pandas')
    data,other = ts.get_daily_adjusted(symbol=ticker,outputsize='full')
    data.reset_index(inplace=True)
    data = data.rename(columns={'5. adjusted close': 'price'})
    current_price = data['price'][0]
    if 'BSE' in ticker: #to include currency symbol
        current_price = 'Rs' + str(current_price)
    else:
        current_price = '$' + str(current_price)

    data = data.iloc[::-1] #reverse order of df to take moving averages from old to new
    ma100 = data.price.rolling(100).mean()
    ma200 = data.price.rolling(200).mean()

    fig = ex.line(data,x='date',y='price',title=f'Stock Price history for {ticker} its current price is {current_price}')
    #fig.add_scatter(x=data['date'], y=ma100, name='MA100') #adding the ma100 plot
    #fig.add_scatter(x=data['date'], y=ma200, name='MA200') #adding the ma200 plot
    graph = fig.to_html(full_html=False)
    return render(request, 'tracker_data.html',{'graph':graph})