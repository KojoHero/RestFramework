from django.urls import path
from .views import SignIn
from knox import views as knox_views
from .views import LoginAPI

urlpatterns = [
    path('signup/', SignIn.as_view(), name='Signin'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]