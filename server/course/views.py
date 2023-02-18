from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView

from .models import Course
from .permissions import IsSuperAdminPermission, IsStudentPermission
from rest_framework import generics

from .serializers import CourseSerializer, StudentCourseSerializer, TeacherCourseSerializer


# Create your views here.

class CreateCourseView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperAdminPermission]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class DeleteCourseView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperAdminPermission]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class UpdateCourseView(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperAdminPermission]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class RegisterCourseView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStudentPermission]
    serializer_class = StudentCourseSerializer
    queryset = Course.objects.all()


class AssignCourseView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperAdminPermission]
    serializer_class = TeacherCourseSerializer
    queryset = Course.objects.all()
