from django.shortcuts import render
from rest_framework import generics

from student.models import StudentProfile
from student.serializers import StudentSerializer

# Create your views here.
class CreateStudentProfileAPIView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = StudentProfile.objects.all()