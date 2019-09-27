from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm
import json, requests
from .forms import getDetails
import csv

def homepage(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'registration/login.html')

def logout(request):
    return render(request, 'registration/logout.html')

def checkweather(request):
    return render(request, 'required_pages/check_weather.html')

def firemap(request):
    return render(request, 'required_pages/fire_map.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def index(request):
    return render(request, 'index.html')


def make_a_alert(request):
    dict = {}
    f = open('data1.csv','r+')
    while f.hasNext():
        x = f.readline().split(',');
        dict.append([x[0],x[1]])
    form = UserForm()
    return render(request, 'required_pages/make_a_alert.html', {form:'form','dict':dict})

def weatherCheckerFunction(request,method = ['GET','POST']):
    request.session.flush()
    if request.method == 'GET':
        tem = ''
        return render(request, 'weather/weather_checker.html',{'tem':tem})
    elif request.method == 'POST':
        api_key = "a1b53799bcd337535f33d864f5c2b4aa"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        print(request)
        city_name = request.POST.get('your_name', '')
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            print(" Temperature (in kelvin unit) = " +
                  str(current_temperature) +
                  "\n atmospheric pressure (in hPa unit) = " +
                  str(current_pressure) +
                  "\n humidity (in percentage) = " +
                  str(current_humidiy) +
                  "\n description = " +
                  str(weather_description))
            my_dict = {'temp':current_temperature,'pressure': current_pressure,'humidity': current_humidiy,'desc': weather_description}
            return render(request, 'weather/weather_checker.html', {'temp':current_temperature,'pressure': current_pressure,'humidity': current_humidiy,'desc': weather_description})
    else:
        return redirect('homepage')