from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
# import json
from django.http import HttpResponse


# Create your views here.


def view(request):
    req = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=0f57ba0243ae78a736aa8ad8372551fb'
    cities = City.objects.all()
    if request.method == "POST":
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    weather_data = []
    for city in cities:
        try:
            city_weather = requests.get(req.format(city)).json()
            weather = {
                'city': city,
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }
            weather_data.append(weather)
        except:
            return HttpResponse('Bad request')
    return render(request, 'weather/index.html', {'weather_data': weather_data, 'form': form})


'''
def view_from_form(request):
    weather_data = []
    if request.method == "POST":
        city_name = str(request.POST.get('city'))
        jsonList = []
        req = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&appid=0f57ba0243ae78a736aa8ad8372551fb")
        jsonList.append(json.loads(req.content))
        userData = {}
        for data in jsonList:
            userData['city'] = city_name
            userData['temperature'] = data['main']['temp']
            userData['description'] = data['weather'][0]['description']
            userData['icon'] = data['weather'][0]['icon']
        weather_data.append(userData)
    return render(request, 'weather/index2.html', {'weather_data': weather_data})
'''
