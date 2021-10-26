from django.db import models


class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    travelPoint = models.DecimalField(max_digits=10, decimal_places=3)
