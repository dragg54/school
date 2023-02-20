from django.shortcuts import render
from rest_framework import generics, status, serializers
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.templatetags.rest_framework import data
from rest_framework.views import APIView
from .models import Student
from .permissions import IsAdminPermission
from .serializers import StudentSerializer


# Create your views here.
class CreateStudentProfileAPIView(APIView):
    def post(self, request, *args, **kwargs):
        permission_classes = [IsAuthenticated, IsAdminPermission]
        matric_number = self.request.POST.get('matric_number')
        existing_student = Student.objects.filter(matric_number=matric_number)
        if existing_student:
            print(matric_number)
            return Response("student already exists", status=status.HTTP_409_CONFLICT)
        serializers = StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)


class GetAllStudentProfile(generics.ListAPIView):
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminPermission]
    queryset = Student.objects.all()


class GetStudentProfile(generics.RetrieveAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsAdminPermission]
    lookup_field = 'pk'
    queryset = Student.objects.all()


class DeleteStudentProfile(generics.RetrieveDestroyAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsAdminPermission]
    lookup_field = 'pk'
    queryset = Student.objects.all()


class UpdateStudentProfile(generics.UpdateAPIView):
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user = self.request.user
        if user:
            profile = Student.objects.get(user_id=user)
            serializer = StudentSerializer(profile, data = request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

