from rest_framework import serializers

from .models import Student
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ['username', 'password']

    def create(self, validate_data):
        user= User(**validate_data)
        password= validate_data.pop('password')
        user.set_password(password)
        user.save()
        return user   

class StudentSerializer(serializers.ModelSerializer):

    academic_year= serializers.ChoiceField(choices=Student.ayChoices)

    class Meta:
        model= Student
        fields= ['name', 'academic_year']

