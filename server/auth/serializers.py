from django.contrib.auth.models import User
from rest_framework import serializers


class AuthSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = super(AuthSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'first_name', 'last_name')
