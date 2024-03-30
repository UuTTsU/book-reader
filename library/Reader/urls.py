from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_reader, name = 'about reader')
    ]