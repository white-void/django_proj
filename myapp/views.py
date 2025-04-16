from django.shortcuts import render
import requests
from .forms import *
# Create your views here.

def Index(request):
    response = requests.get('https://www.googleapis.com/books/v1/volumes?q=Philosophy')
    data = response.json()
    context = {
        'data':data,
        'maxResults':"1",
    }
    print(data["items"][0]["volumeInfo"]['title'])



    return render(request,'index.html',context)

def formdata(request):
    form = Dataform
    if request.method == "POST":
        form = Dataform(request.POST)
        form.save()

    
    context = {
        'form':form
    }

    return render(request,'formdata.html',context)