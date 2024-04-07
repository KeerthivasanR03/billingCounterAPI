from django.db import models
from django.contrib.auth.models import User
import uuid

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)

class Bill(models.Model):
    billNumber = models.CharField(max_length=200, default=uuid.uuid4())
    employee = models.ForeignKey(to=User, related_name='employee_bill', on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    total = models.FloatField()

class Order(models.Model):
    bill = models.ForeignKey(to=Bill, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()



    
