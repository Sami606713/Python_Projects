from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(requet):
    return HttpResponse("<h1>index Page</h1>")