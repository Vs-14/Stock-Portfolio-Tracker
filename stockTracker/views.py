from django.shortcuts import render
from .forms import basicForm
from alpha_vantage.timeseries import TimeSeries
from keys import MY_KEY
api_key = MY_KEY


# Create your views here.

def tracker(request):
    if request.method == 'POST':
        name = request.POST.get('name')
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
            combined = 'Company Name:' + stock[1] + '\t\tSymbol:' + stock[0]
            #radio_buttons.append({'value': stock[0], 'label': combined})
            radio_buttons.append({'value': stock[0], 'label': stock[1]})
        return render(request,'symbol.html',{'radio_buttons': radio_buttons})

    else:
        # render the form
        form = basicForm()
        return render(request, 'track.html', {'form': form})