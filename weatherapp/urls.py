from django.urls import path
from . import views

urlpatterns = [
    path('', views.weatherApplication, name='weatherApplication'),  #the path for our index view
]