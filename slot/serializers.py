
from rest_framework import serializers
from datetime import datetime


class BookingSerializer(serializers.Serializer):

    team_name = serializers.CharField()

    phone = serializers.CharField()

    def validate(self,validated_data):
    
        phone = validated_data.get("phone")
    
        if len(phone)<9:
    
            raise serializers.ValidationError("phone number must have 9 digits")
    
        return validated_data

    turf = serializers.IntegerField()

    booking_date = serializers.DateField()

    def validate(self,validated_data):
    
        booking_date = validated_data.get("booking_date")
    
        if booking_date<datetime.today().date():
    
            raise serializers.ValidationError("Invalid date")

        return validated_data

    booking_time = serializers.TimeField()

    duration = serializers.DurationField()