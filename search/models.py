from django.db import models
import cgi
import os
import requests
import csv
import json
import pandas as pd
import numpy as np
import re

class Product(models.Model):
    product_name = models.TextField()
    product_nutrient = models.TextField()
    product_unit = models.TextField()

    def __str__(self):
        return "{} - {} - {}".format(self.product_name, self.product_nutrient, self.product_unit)
