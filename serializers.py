from rest_framework import serializers
from .models import UserAPI


class UserApiSerializer(serializers.Serializer);
    name = serializers.CharField(max_lenght=50)
    email = serializers.Charfield()
    password = serializers.Charfield()