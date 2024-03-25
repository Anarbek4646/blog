from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from . import serializers

# Create your views here.


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer




class UserLoginViews(generics.CreateAPIView):
    pass


class UserLogoutViews(generics.CreateAPIView):
    pass