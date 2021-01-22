from django.contrib.auth import login
from rest_framework import generics, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny
from knox.views import LoginView as KnoxLoginView
from .models import Registration, BlogPost, Category, TodoList
from .serializers import RegSerializers, LogSerializers, BlogSerializer, CatSerializer, TodoListSerializer


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


class BlogView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer



class CatView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer


class TodoView(generics.ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer




