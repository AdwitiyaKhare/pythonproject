from django.db import models

class NSEFuture(models.Model):
    contract_type = models.CharField(max_length=100)
    expiry_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add more fields as needed
