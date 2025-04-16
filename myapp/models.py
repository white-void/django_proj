from django.db import models
import datetime
# Create your models here.


class metadata(models.Model):
    name = models.CharField(max_length=100)
    auth = models.CharField(max_length=100)
    age = models.PositiveIntegerField(max_length=3)
    date = models.DateField(datetime.date)