from django import forms
from .models import StockPurchase

class StockPurchaseForm(forms.ModelForm):
    class Meta:
        model = StockPurchase
        fields = ['stock', 'purchase_price', 'quantity']