
from rest_framework import serializers
from django.contrib.auth.models import User
from slot_v2.models import Bookingv2
from datetime import datetime


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","email","password"]

class BookingV2Serializer(serializers.ModelSerializer):

    turf = serializers.StringRelatedField()

    class Meta:

        model = Bookingv2

        fields = "__all__"

        read_only_fields = ["id","booking_endtime"]

    def validate(self,validated_data):

        booking_date = validated_data.get("booking_date")

        if booking_date<datetime.today().date():

            raise serializers.ValidationError("Enter valid date")

        return validated_data
        