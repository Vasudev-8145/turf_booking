from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from slot.models import Booking
from slot.serializers import BookingSerializer
# Create your views here.

class BookingListCreateView(APIView):

    def get(self,request):

        qs = Booking.objects.all()

        serializer_instance = BookingSerializer(qs,many=True)

        return Response(data=serializer_instance.data)