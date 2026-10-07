from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import authentication,permissions
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView

from datetime import time,timedelta,datetime

from slot_v2.serializers import SignUpSerializer
from django.contrib.auth.models import User
from slot_v2.models import Bookingv2
from slot_v2.serializers import BookingV2Serializer

# Create your views here.

class SignUpView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = SignUpSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            user_object = User.objects.create_user(**cleaned_data)

            serializer_instance = SignUpSerializer(user_object)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class BookingV2ListCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        qs = Bookingv2.objects.all()

        serializer_instance = BookingV2Serializer(qs,many=True)

        return Response(data=serializer_instance.data)

    def post(self, request):

        form_data = request.data

        serializer_instance = BookingV2Serializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            turf_id = cleaned_data.get("turf")
            booking_date = cleaned_data.get("booking_date")
            booking_time = cleaned_data.get("booking_time")
            duration = cleaned_data.get("duration")

            booking_end_datetime = (
                datetime.combine(booking_date, booking_time) + duration
            )

            booking_endtime = booking_end_datetime.time()

            existing_bookings = Bookingv2.objects.filter(
                turf=turf_id,
                booking_date=booking_date
            )

            for booking in existing_bookings:

                existing_start = booking.booking_time
                existing_end = booking.booking_endtime

                if booking_time < existing_end and booking_endtime > existing_start:

                    raise ValidationError(
                        {
                            "booking_time": "This turf is already booked for the selected time."
                        }
                    )

            cleaned_data["booking_endtime"] = booking_endtime

            qs = Bookingv2.objects.create(**cleaned_data)

            serializer_instance = BookingV2Serializer(qs)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class Bookinv2RetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = BookingV2Serializer
    queryset = Bookingv2.objects.all()