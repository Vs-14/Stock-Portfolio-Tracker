from django.shortcuts import render
from portfolioSymbol.models import StockPurchase

# Create your views here.
def DB_entry(request):
    username = request.user
    symbol = request.POST['symbol']
    price = request.POST['buying_price']
    quantity = request.POST['quantity']
    purchase = StockPurchase(user=username, stock=symbol, purchase_price=price, quantity=quantity)
    purchase.save()
    total = float(price)*int(quantity)
    total = round(total,2)
    if 'BSE' in symbol:
        price = 'Rs' + str(price)
        total = 'Rs' + str(total)
    else:
        price = '$' + str(price)
        total = '$' + str(total)
    return render(request, 'purchase.html', {'symbol':symbol, 'price':price, 'quantity':quantity, 'total':total})