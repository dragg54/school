from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics

from .serializers import AuthSerializer


# Create your views here.

class CreateUser(generics.ListCreateAPIView):
    serializer_class = AuthSerializer
    queryset = User.objects.all()
