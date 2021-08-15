from django.db import models



class Product(models.Model):
    name=models.CharField(max_length=255)
    type=models.CharField(max_length=255)
    build=models.CharField(max_length=255)
# Create your models here.
