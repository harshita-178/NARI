from contextlib import nullcontext
from django.shortcuts import render,HttpResponse
from .models import Contact

# Create your views here.
def index(request):
    if request.method=="POST":
        contact=Contact()
        email=request.POST.get('email')
        password=request.POST.get('password')
        contact.email=email
        contact.password=password
        contact.save()
        return render(request,'Home.html')
    return render(request,'index.html')

def Awareness(request):
    return render(request,'Awareness.html')

def Services(request):
    return render(request,'Services.html')  

def Healthcare(request):
    return render(request,'Healthcare.html')    