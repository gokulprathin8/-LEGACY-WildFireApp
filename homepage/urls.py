from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('check-weather/', views.checkweather, name='checkweather'),
    path('fire-map/', views.firemap, name='firemap'),
    path('register/',views.register, name='register'),
    path('', views.index, name='index'),
    path('make-a-alert/',views.make_a_alert, name='make-a-alert'),
    path('weather_checker/', views.weatherCheckerFunction, name='weatherCheckerFunction')

]