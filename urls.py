from django.contrib import *
from . import views
from django.urls import path


urlpatterns = [

path("",views.index, name="index"), ]

