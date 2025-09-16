from django.db import models

# Create your models here.
class Flight(models.model):
    origin = models.charField(max_length=64)
    destination = models.charField(max_lenght=64)
    duration = models.integerField()