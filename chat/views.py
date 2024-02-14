from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Message
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
    return render(request, "chat/index.html", {
    })

@login_required
def room(request):
    if request.method == "POST":
        name = request.POST['name']
        user = request.user
        if Room.objects.filter(name=name):
            return redirect('/messages/'+ name)
        else:
            rm = Room.objects.create(name=name, created_by=user.username)
            rm.save()
            return redirect('/messages/'+ name)

    return render(request, "chat/index.html", {
    
    })

@login_required
def messages(request, name):
    if request.method == "POST":
        room = request.POST['room']
        msg = request.POST['msg']
        sent_to = request.POST['sent_to']
        sender = request.POST['sender']
        m = Message.objects.create(sender=sender, room=room, msg=msg, sent_to=sent_to)
        m.save()

    msgs = Message.objects.filter(room=name)
    user = request.user
    return render(request, "chat/index.html", {
        "msgs": msgs,
        "room": name,
        "username": user.username
    })

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('login')
        return render(request, "chat/login.html")
    return render(request, "chat/login.html")

def logout(request):
    auth.logout(request)
    return redirect('login')
