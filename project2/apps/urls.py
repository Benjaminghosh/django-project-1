from django.urls import path
from apps.views import *

urlpatterns = [
    path('home',home,name='home'),
    path('login',login,name='home'),
    path('register',register,name='home')
]
