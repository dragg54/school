from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.templatetags.rest_framework import data
from rest_framework.views import APIView

from .models import StudentProfile
from .permissions import IsStudentPermission
from .serializers import StudentSerializer


# Create your views here.
class CreateStudentProfileAPIView(APIView):
    def post(self, request, *args, **kwargs):
        permission_classes = [IsAuthenticated, IsStudentPermission]
        matric_number = self.request.POST.get('matric_number')
        existing_student = StudentProfile.objects.filter(matric_number=matric_number)
        if existing_student:
            print(matric_number)
            return Response("student already exists", status=status.HTTP_409_CONFLICT)
        serializers = StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
