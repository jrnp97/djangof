from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# VIEW
def index(request):

    return HttpResponse('Hola D & D')
