from django.shortcuts import render
from django.http import HttpResponse
import requests

openweatherapi='http://api.openweathermap.org/data/2.5/weather?q='
apikey='APPID=09a589b23d3e65029f00268d33badda4'
find_addr='https://ipinfo.io/'

def find_ip(url):
    ip=requests.get(url)
    data=ip.json()
    city=data['city']
    return city

def weather_forcast(city_name):
    r=requests.get(openweatherapi+city_name+"&&units=metric&&"+apikey)
    data=r.json()
    return data

def home(request):
    if request.method == 'POST':
        city_name=request.POST['get_city']
        a=weather_forcast(city_name)
        weather_details={
        'city':city_name,
        'description':a['weather'][0]['description'],
        'temperature':a['main']['temp'],
        'icon':a['weather'][0]['icon']
        }
        return render(request,"weatherapp/home.html",weather_details)
    else:
        city_name=find_ip(find_addr)
        a=weather_forcast(city_name)
        weather_details={
        'city':city_name,
        'description':a['weather'][0]['description'],
        'temperature':a['main']['temp'],
        'icon':a['weather'][0]['icon']
        }
        return render(request,"weatherapp/home.html",weather_details)
    return render(request,"weatherapp/home.html",weather_details)
