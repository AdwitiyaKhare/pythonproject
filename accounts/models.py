from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    # Add more fields as needed
