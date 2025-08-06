from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'hello/index.html')

def rafa(request):
    return HttpResponse('Rafa')

def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name.captalize() #variaveis que quero que meu template possa usar
    })

def greeting(request, name):
    return HttpResponse(f"Hello, {name}")

