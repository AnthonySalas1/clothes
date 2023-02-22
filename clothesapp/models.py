from django.db import models

class Item(models.Model):
    id = models.AutoField(primary_key=True)

    product = models.CharField(max_length=100)

    price = models.DecimalField( max_digits=6, decimal_places=2,default=0.00)

    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.product