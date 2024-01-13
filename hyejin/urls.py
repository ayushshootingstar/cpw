from django.contrib import admin
from django.urls import path
from hyejin import views

urlpatterns = [
   path('', views.main, name='main'),
   path('index/', views.index, name='index'),
   ]