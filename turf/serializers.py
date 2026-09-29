
from rest_framework import serializers

class TurfSerializer(serializers.Serializer):

    id = serializers.CharField(read_only=True)

    name =  serializers.CharField()

    location = serializers.CharField()

    phone = serializers.CharField()

    fee = serializers.IntegerField()

    
    def validate(self,validated_data):

        phone = validated_data.get("phone")

        if len(phone)<9:

            raise serializers.ValidationError("phone number must have 9 digits")

        return validated_data

    def validate(self,validated_data):

        fee = validated_data.get("fee")

        if fee<600:

            raise serializers.ValidationError("fee must be greater than 600")

        return validated_data

class UserSerializer(serializers.Serializer):

    username = serializers.CharField()

    email = serializers.EmailField()

    password = serializers.CharField()



        

