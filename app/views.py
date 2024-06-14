from django.shortcuts import render
from app.models import*


# Create your views here.

def home(request):
    data = mobile.objects.all()
    context ={
        'data':data,
    }
    return render(request,"home.html",context)