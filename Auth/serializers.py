from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import Registration


class RegSerializers(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=False, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    c_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Registration
        fields = ('__all__')


    def validate(self, attrs):
        if attrs['password'] != attrs['c_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()

        return user


class LogSerializers(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = ('username', 'password')