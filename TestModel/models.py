from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(verbose_name='名称', max_length=20, default='')
    price = models.DecimalField(verbose_name='价格', max_digits=7, decimal_places=2, default=0.0)
