from rest_framework import serializers
from .models import Course, StudentCourse, TeacherCourse


class CourseSerializer(serializers):
    class Meta:
        model = Course
        fields = "__all__"


class StudentCourseSerializer(serializers):
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


class TeacherCourseSerializer(serializers):
    class Meta:
        model = TeacherCourse
        fields = "__all__"
