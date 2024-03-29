from django.db import models
from django.contrib.auth.models import User
from artisianshop.models import Product
# Create your models here.


class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    review=models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)