
from rest_framework import serializers

class BookingSerializer(serializers.Serializer):

    team_name = serializers.CharField()

    phone = serializers.CharField()

    turf = serializers.IntegerField()

    booking_date = serializers.DateField()

    booking_time = serializers.TimeField()

    duration = serializers.CharField()