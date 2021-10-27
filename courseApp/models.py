from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    ratings = models.DecimalField(max_digits=10, decimal_places=3)
