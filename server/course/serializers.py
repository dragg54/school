from rest_framework import serializers
from .models import Course, StudentCourse, SupervisorCourse


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class StudentCourseSerializer(serializers.ModelSerializer):
    def create(self):
        student = self.request.user
        student_course = StudentCourse.objects.create(
            student=student
        )
        student_course.save()
        return student_course

    class Meta:
        model = StudentCourse
        fields = "__all__"


class SupervisorCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupervisorCourse
        fields = "__all__"
