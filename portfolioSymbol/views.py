from django.shortcuts import render
from alpha_vantage.timeseries import TimeSeries
from .forms import StockPurchaseForm
from keys import MY_KEY
api_key = MY_KEY

# Create your views here.
def portfolio_symbol(request):
    stock = request.POST.get('stock')
    ts = TimeSeries(key=api_key,output_format='pandas')
    data = ts.get_quote_endpoint(stock)
    data = data[0]
    data.reset_index(drop=True,inplace=True)
    purchase_price = float(data['05. price'])
    form = StockPurchaseForm(initial={'purchase_price':purchase_price, 'stock':stock})
    return render(request, 'portfolio_stock_data.html',{'form':form})