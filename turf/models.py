from django.db import models

# Create your models here.

# turf [id,name,location,phone,fee]

class Turf(models.Model):

    name = models.CharField(max_length=200)

    location = models.CharField(max_length=200)

    phone = models.CharField(max_length=200,null=True)

    fee = models.PositiveIntegerField()

    def __str__(self):
        return self.name