from django.db import models
from django.contrib.auth.models import User

class Trade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trade_type = models.CharField(max_length=100)
    trade_date = models.DateField()
    trade_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Add more fields as needed
