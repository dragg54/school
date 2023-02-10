from rest_framework import serializers

class AuthSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        
        email = validated_data["email"]
        role = "student"
