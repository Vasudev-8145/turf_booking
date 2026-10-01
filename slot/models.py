from django.db import models
from turf.models import Turf

# Create your models here.

# booking[team_name,phone,date,turf,time,duration]

class Booking(models.Model):

    team_name = models.CharField(max_length=200)

    phone = models.CharField(max_length=15)

    turf = models.ForeignKey(Turf,on_delete=models.CASCADE)

    booking_date = models.DateField()

    booking_time = models.TimeField(
        editable=False,
        null=True
    )

    duration = models.DurationField()

    def __str__(self):
        return self.team_name