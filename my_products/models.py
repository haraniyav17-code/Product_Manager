from django.db import models

class ProductDetails(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.TextField()
    type=models.CharField(max_length=50)




