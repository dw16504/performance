# A very frustrating aspect of this tutprial is the paths to views. I added this file because
# for some reason I can not access it from inside the App directories.



from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'investments/home.html')

def base(request):
    #return HttpResponse ("does this work?")
    return render(request, 'base.html')

def secondPage(request):
    return render(request, 'secondPage.html');
