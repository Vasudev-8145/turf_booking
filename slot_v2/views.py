from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

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

    def get(self,request):

        qs = Bookingv2.objects.all()

        serializer_instance = BookingV2Serializer(qs,many=True)

        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data = request.data

        serializer_instance = BookingV2Serializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            turf_id = cleaned_data.get("turf")
            booking_date = cleaned_data.get("booking_date")
                        
            last_booking_object = Bookingv2.objects.filter(turf=turf_id,booking_date=booking_date).last()

            time_duration = cleaned_data.get("duration")
            booking_date_time = (datetime.combine(booking_date,last_booking_object.booking_time)+time_duration).time()
            cleaned_data["booking_endtime"] = booking_date_time

            qs = Bookingv2.objects.create(**cleaned_data)
            serializer_instance = BookingV2Serializer(qs)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)