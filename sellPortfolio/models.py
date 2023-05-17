from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StockSell(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.CharField(max_length=10)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_date = models.DateTimeField(auto_now_add=True)