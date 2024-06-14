from django.shortcuts import render,HttpResponse
import requests
import datetime

# Create your views here.

def home(request):
    
    city= request.GET.get('city',"jaipur")
    url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=20395329f0681f546fe6d8a91a8efec4'
    data = requests.get(url).json()
    payload= {'city':data['name'], 
              'weather':data['weather'][0]['main'],
              'icon':data['weather'][0]['icon'],
              'kelvin_temperature':data['main']['temp'],
              'celcuis_temperature':int(data['main']['temp'] - 273),
              'pressure': data['main']['pressure'],
              'humidity':data['main']['humidity'],
              'description':data['weather'][0]['description'],
              }
    
    context={
        'data':payload
    }
    
    print(context)
    
    
    return render( request,'home.html',context)