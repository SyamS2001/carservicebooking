
from django.db import models

class CarService(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service =models.CharField(max_length=7000)
    date =models.DateField()
    dec =models.TextField(max_length=7000)

    def __str__(self):
        return self.name

