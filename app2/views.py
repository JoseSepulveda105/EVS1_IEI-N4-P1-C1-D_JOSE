from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def tiempo(request):
    dt=datetime.datetime.now()
    s="<h1>fecha y hora actual : </h1>"+str(dt)
    return HttpResponse

