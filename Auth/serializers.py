from time import strftime

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Registration, BlogPost, Category, TodoList


class RegSerializers(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    c_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Registration
        fields = '__all__'

    def validate(self, attrs):
        if attrs['password'] != attrs['c_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'], username=validated_data['username'] )
        user.set_password(validated_data['password'])
        user.save()

        return user


class LogSerializers(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = ('email', 'password')


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'


