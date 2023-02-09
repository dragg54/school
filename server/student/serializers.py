from rest_framework import serializers

from student.models import StudentProfile

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = "__all__"