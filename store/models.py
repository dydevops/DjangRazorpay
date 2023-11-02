from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField(default=0)
    order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name   