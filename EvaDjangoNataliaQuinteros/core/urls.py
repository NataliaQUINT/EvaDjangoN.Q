from django.urls import path
from .views import *

urlpatterns = [
     path('', login, name="login"),
     path('index/', index, name="index"),
     path('home', home, name="home"),
     path('contacto', contacto, name="contacto"),
     path('register', register, name="register"),
]
