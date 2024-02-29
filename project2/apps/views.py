from django.shortcuts import render

# Create your views here.

def home(request):
    d={
        'name':'Benjamin',
        'age':21,
        'pay':2000
    }

    return render(request,'Home.html',d)

def login(request):
    return render(request,'Login.html')

def register(request):
    if request.method =='POST':
        return render(request,"login.html")
    return render(request,'Register.html')