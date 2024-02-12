from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "chat/index.html")

def room(request):
    pass

def messages(request):
    pass
