from django.shortcuts import render
from alpha_vantage.timeseries import TimeSeries
api_key = "IUAPAEP4N3KFQ5QW"
from .forms import StockPurchaseForm

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