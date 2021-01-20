from django.contrib.auth import login
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny
from knox.views import LoginView as KnoxLoginView
from .models import Registration
from .serializers import RegSerializers, LogSerializers


class SignIn(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegSerializers
    permission_classes = (AllowAny,)


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LogSerializers

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)