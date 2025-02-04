from django.shortcuts import render
import random
import string
import secrets
from django.http import HttpResponse
import requests

# Create your views here.
def generate_password(request):
    

    password = ""
    for _ in range(9):
        password += secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    return HttpResponse(password)
def rand_number(request):
    num=random.randint(1,1001)
    text=requests.get(f"http://numberapi.com/{num}")
    return HttpResponse(text)
    
def weather(request):
    info= requests.get('https://wttr.in/kerman?format=j1')
    data = info.json()['current_condition'][0]  
    context = {  
        'temp_c': data['temp_C'],  
        'windspeed_kmph': data['windspeedKmph'],  
        'humidity': data['humidity'],  
    }  

    return render(request, 'info_weather/weather.html', context) 
