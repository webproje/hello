from django.shortcuts import render
import json
import requests
from django.views.generic import TemplateView
from weather.forms import HomeForm
#from django.http import JsonResponse

# Create your views here.
def index(request):
    if request.method == "POST":
        form = HomeForm(request.POST)
        text = request.POST['post']

    #template_name ='weather/index.html'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={london}&units=imperial&appid=20d57468479aa1520a310c761005c159'
    city = 'Las Vegas'
#    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
#    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
    city_weather = requests.get(url).json() #request the API data and convert the JSON to Python data types
    weather = {
        'city' : city,
        'message' : city_weather['message'],
#        'description' : city_weather['weather'][0]['description'],
#        'icon' : city_weather['weather'][0]['icon']
        'sonuncu' : 'virgul icin'
    }
    context = {'weather' : weather, 'text':text}
    return render(request, 'weather/index.html', context) #returns the index.html template


def get(self, request):
    form = HomeForm()
    return render(request, 'weather/index.html', {'form': form})

def post(self, request):
    form = HomeForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['post']

    args ={'form': form, 'text':text}
    return render(request, 'weather/index.html', args)        
