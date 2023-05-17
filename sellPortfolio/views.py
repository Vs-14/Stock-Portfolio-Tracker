from django.shortcuts import render
from .models import StockSell
from portfolioSymbol.models import StockPurchase

# Create your views here.
def sell(request):
    uid = request.POST.get('entry_uid')
    symbol = request.POST.get('entry_symbol')
    p = request.POST.get('entry_p')
    q = request.POST.get('entry_q')
    cp = request.POST.get('entry_current_price')
    if '$' in p:
        p = float(p[1:])
        cp = float(cp[1:])
    else:
        p = float(p[2:])
        cp = float(cp[2:])
    return render(request, 'sell.html', {'uid':uid,'symbol':symbol,'p':p,'q':q,'cp':cp})

def sold(request):
    username = request.user
    symbol = request.POST.get('symbol')
    p = request.POST.get('buying_price')
    q = request.POST.get('quantity')
    cp = request.POST.get('current_price')
    uid = request.POST.get('uid')
    print(p,q,cp,uid)

    #to manage the purchased db
    purchase_data = StockPurchase.objects.filter(id=uid)
    data = purchase_data.values()[0]
    quantity = data['quantity']
    if int(q) == quantity:
        purchase_data.delete()
    else:
        modified = StockPurchase.objects.get(id=uid)
        modified.quantity = quantity-int(q)
        modified.save()

    #to manage sold db
    selling_data = StockSell(user=username,stock=symbol,purchase_price=p,quantity=q,selling_price=cp)
    selling_data.save()

    diff = (float(cp)-float(p))*int(q)
    diff = round(diff,2)
    if cp >= p:
        if 'BSE' in symbol:
            p = "Rs" + str(p)
            cp = "Rs" + str(cp)
        else:
            p = "$" + str(p)
            cp = "$" + str(cp)
        text_info = q + ' shares of ' + symbol + ' bought at ' + p + ' sold at ' + cp + ' for a profit of ' + str(diff)
    else:
        if 'BSE' in symbol:
            p = "Rs" + str(p)
            cp = "Rs" + str(cp)
            diff = "Rs" + str(diff)
        else:
            p = "$" + str(p)
            cp = "$" + str(cp)
            diff = "$" + str(diff)
        text_info = q + ' shares of ' + symbol + ' bought at ' + p + ' sold at ' + cp + ' for a loss of ' + str(diff)

    return render(request, 'sold.html', {'text_info':text_info})