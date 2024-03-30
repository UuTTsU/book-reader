from django.urls import path
from . import views

urlpatterns = [
    path('about_book/', views.about_book, name = 'about_book')
]