from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from turf.models import Turf
from turf.serializers import TurfSerializer,UserSerializer

# Create your views here.

class AdminCreateView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            User.objects.create_superuser(**form_data)

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)

class TurfListCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self,request):

        qs = Turf.objects.all()

        serializer_instance = TurfSerializer(qs,many=True)

        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data = request.data

        serializer_instance = TurfSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            Turf.objects.create(**form_data)

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)

class TurfRetreiveUpdateDeleteView(APIView):

    def get(self,request,pk=None):

        qs = Turf.objects.get(id=pk)

        serializer_instance = TurfSerializer(qs)

        return Response(data=serializer_instance.data)

    def post(self,request,pk=None):

        form_data = request.data

        serializer_instance = TurfSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            Turf.objects.filter(id=pk).update(**form_data)

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):

        Turf.objects.get(id=pk).delete()

        return Response(data={"message":"deleted..."})