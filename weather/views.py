from django.shortcuts import render
import requests
from .models import City
from django.http import HttpResponse

# Create your views here.


def view(request):
    req = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=0f57ba0243ae78a736aa8ad8372551fb'
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        city_weather = requests.get(req.format(city)).json()
        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)

    return render(request, 'weather/index.html', {'weather_data': weather_data})

