from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from slot.models import Booking
from slot.serializers import BookingSerializer
from turf.models import Turf
# Create your views here.

class BookingListCreateView(APIView):

    def get(self,request):

        qs = Booking.objects.all()

        serializer_instance = BookingSerializer(qs,many=True)

        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data = request.data

        serializer_instance = BookingSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            turf = cleaned_data.get("turf")
            
            turf_object = Turf.objects.get(id=turf)
            cleaned_data["turf"] = turf_object
            
            Booking.objects.create(**cleaned_data)
            
            response_data = {
                "status":"booked"
            }
            
            return Response(data=response_data)

        else:

            return Response(data=serializer_instance.errors)

class BookingRetrieveUpdateDeleteView(APIView):

    def get(self,request,pk=None):

        qs = Booking.objects.get(id=pk)

        serializer_instance = BookingSerializer(qs)

        return Response(data=serializer_instance.data)

    def post(self,request,pk=None):

        form_data = request.data

        serializer_instance = BookingSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            Booking.objects.filter(id=pk).update(**cleaned_data)

            booking = Booking.objects.get(id=pk)

            serializer_instance = BookingSerializer(booking)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):

        Booking.objects.get(id=pk).delete()

        return Response(data={"message":"deleted..."})