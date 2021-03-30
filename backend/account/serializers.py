from rest_framework import serializers as sz

from .models import User

class UserSerializer(sz.ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "nickname", "password")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user