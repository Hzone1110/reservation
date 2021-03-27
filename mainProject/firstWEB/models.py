from django.db import models


# Create your models here.
class Appoint(models.Model):
    subject = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
