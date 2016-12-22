from __future__ import unicode_literals

from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=50)
    image_name = models.CharField(max_length=100)
    ingridients = models.CharField(max_length=200)
    instructions = models.TextField()
    vote_count = models.IntegerField(default=0)
    available = models.BooleanField(default=True)