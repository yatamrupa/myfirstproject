from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rejection(request):
    return HttpResponse('no neeku akka chellelu lera')
