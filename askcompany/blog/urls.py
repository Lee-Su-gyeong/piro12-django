from django.urls import path, register_converter
from . import views

app_name = 'blog'

urlpatterns = [
    path('archives/<yyyy:year>/', views.archives_year),
]