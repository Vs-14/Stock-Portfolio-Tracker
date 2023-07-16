from django.shortcuts import render
from portfolioSymbol.models import StockPurchase
import pytz
from keys import MY_KEY

from alpha_vantage.timeseries import TimeSeries
api_key = MY_KEY

# Create your views here.
def checkPortfolio(request):
    user_data = StockPurchase.objects.filter(user=request.user).values()
    data = []
    for entry in user_data:
        uid = entry['id'] #primary key of each purchase [use later for submit btn as value]
        symbol = entry['stock']
        p = float(entry['purchase_price'])
        q = int(entry['quantity'])
        d = entry['purchase_date'] #gets server date in utc
        ist = pytz.timezone('Asia/Kolkata')
        d = d.astimezone(ist) #converting to ist
        date = d.strftime('%Y-%m-%d %H:%M') #keeping only relevant time
        total = p*q
        total = round(total,2)

        ts = TimeSeries(key=api_key,output_format='pandas')
        info = ts.get_quote_endpoint(symbol)
        info = info[0]
        info.reset_index(drop=True,inplace=True)
        current_price = float(info['05. price'])
        current_total = q*current_price
        current_total = round(current_total,2)

        #change = str(round(((current_total-total)/total)*100),2) + '%'
        change = str(round((((current_total-total)/total)*100),2)) + '%'

        if 'BSE' in symbol:
            p = 'Rs' + str(p)
            total = 'Rs' + str(total)
            current_price = 'Rs' + str(current_price)
            current_total = 'Rs' + str(current_total)
        else:
            p = '$' + str(p)
            total = '$' + str(total)
            current_price = '$' + str(current_price)
            current_total = '$' + str(current_total)
            
        d = {'uid':uid,'symbol':symbol,'p':p,'q':q,'date':date,'total':total,'current_price':current_price,'current_total':current_total,'change':change}
        data.append(d)
    return render(request, 'check_portfolio.html', {'data':data})