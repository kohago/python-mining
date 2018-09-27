from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
#view
def home(request):
    return HttpResponse("Hello! Django World!")
