from django.db import models


# Create your models here.
class Meal(models.Model):
    date = models.TextField()
    time = models.TextField()
    description = models.TextField()
