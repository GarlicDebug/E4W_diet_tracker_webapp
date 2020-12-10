from django.contrib.auth.models import User
from django.db import models


class Meal(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, null=True)
    date = models.TextField()
    time = models.TextField()
    description = models.TextField()
    quantity = models.TextField()
