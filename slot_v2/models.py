from django.db import models
from turf.models import Turf

# Create your models here.


class Bookingv2(models.Model):

    team_name = models.CharField(max_length=200)

    phone = models.CharField(max_length=15)

    turf = models.ForeignKey(Turf,on_delete=models.CASCADE)

    booking_date = models.DateField()

    booking_time = models.TimeField()

    booking_endtime = models.TimeField(
        editable=False,
        null=True
    )

    duration = models.DurationField()

    def __str__(self):
        return self.team_name

