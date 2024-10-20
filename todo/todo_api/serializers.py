from rest_framework import serializers
from .models import Geek
from djoser.serializers import UserSerializer, UserCreateSerializer as BaseUserSerializer

class GeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geek
        fields = ["name", "tg_name", "tg_id", "create_date", "status","start_date", "cancel_date","user"]


# class UserCreateSerializer(BaseUserSerializer):
#     class Meta(BaseUserSerializer.Meta):
#         fields = ['id', 'email', 'username', 'password']

# class CurrentUserSerializer(UserSerializer):
#     class Meta(UserSerializer.Meta):
#        fields = ['id', 'email', 'username', 'password']