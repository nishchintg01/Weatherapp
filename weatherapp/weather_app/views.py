""" Weather App Views Module """
from django.shortcuts import render
import requests

OPEN_WEATHER_API_ENDPOINT = 'http://api.openweathermap.org/data/2.5/weather?q='
OW_API_KEY = 'APPID=09a589b23d3e65029f00268d33badda4'
IP_INFO_URI = 'https://ipinfo.io/'

def find_city_name_from_ip_addr(url):
    """
    Function to Fetch User's City name from IP Address
    """
    try:
        ip=requests.get(url)
        data=ip.json()
        city=data.get('city', "")
        return city
    except Exception as exc:
        print("City Details Not Found. Erro due to => %s", exc)
    return None

def get_weather_details_for_city(city_name):
    """
    Function to Fetch Weather Details from Open Weather API
    for the provided city
    """
    r=requests.get(OPEN_WEATHER_API_ENDPOINT+city_name+"&&units=metric&&"+OW_API_KEY)
    data=r.json()
    return data

def home_page(request):
    """
    Function to render weather details if city details
    are provided in POST request else show User city details.
    """
    if request.method == 'POST':
        city_name=request.POST['get_city']
    else:
        city_name=find_city_name_from_ip_addr(IP_INFO_URI)
    a=get_weather_details_for_city(city_name)
    weather_details = {"city": None, "description": None, "temperature": None, "icon": None}
    if int(a.get("cod", 400)) == 200:
        weather_details={
        'city':city_name,
        'description':a['weather'][0]['description'],
        'temperature':a['main']['temp'],
        'icon':a['weather'][0]['icon']
        }
    return render(request,"weatherapp/home.html",weather_details)
