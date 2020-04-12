from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args,**kwargs):
    return render(request,"home.html")


def contact_view(*args,**kwargs):
    return HttpResponse("<h1> Contact Page  </h1>")


def about_view(request,*args,**kwargs):
    return render(request,"about.html")


def social_view(*args,**kwargs):
    return HttpResponse("<h1> Social Page  </h1>")

