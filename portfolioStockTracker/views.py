from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from alpha_vantage.timeseries import TimeSeries
api_key = "IUAPAEP4N3KFQ5QW"

# Create your views here.
def portfolio_stock_finder(request):
    if request.method == 'POST':
        name = request.POST.get('company')
        ts = TimeSeries(key=api_key,output_format='pandas')
        symbols = ts.get_symbol_search(name.upper())
        s = symbols[0]
        if s.empty:
            return render(request,'error.html')
        s = s[['1. symbol', '2. name']]
        s.reset_index(inplace=True,drop=True)
        stocks = s.values.tolist()
        radio_buttons = []
        for stock in stocks:
            radio_buttons.append({'value': stock[0], 'label': stock[1]})
        return render(request,'portfolio_symbols.html',{'radio_buttons': radio_buttons})
    else:
        return render(request, 'stock_name.html')