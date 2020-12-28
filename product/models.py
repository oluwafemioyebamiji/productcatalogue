from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete= models.CASCADE, related_name="products")
    name = models.CharField(max_length=256)
    price = models.FloatField()
    shippingcost = models.FloatField()
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name