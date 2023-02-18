from datetime import date

from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        date_admitted = validated_data['date_admitted']
        student = Student.objects.create(
            level=date.year - date_admitted.year
        )
        student.save()
        return student

    class Meta:
        model = Student
        fields = "__all__"
