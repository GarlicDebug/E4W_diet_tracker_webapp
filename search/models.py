from django.db import models
import cgi
import os

class Product(models.Model):
    product_nutrient = models.TextField()
    product_amount = models.TextField()
    product_unit = models.TextField()

    def __str__(self):
        return "{} - {} {}".format(self.product_nutrient, self.product_amount, self.product_unit)
