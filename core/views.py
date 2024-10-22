from django.shortcuts import render,redirect
from .models import rooms

from django.contrib import messages
# Create your views here.
def home(request):
    room = rooms.objects.all()
    return render(request, "core/home.html", {
        "rooms" : room
    })

def createRoom(request):
    
    if request.method == "POST":
        room_name = request.POST.get("roomname")
        if rooms.objects.filter(name = room_name).exists():
            messages.error(request, "room name already exists")
            return redirect("create_room")
        user = request.user
        if rooms.objects.filter(creator = user).exists():
            messages.error(request, "users are only allowed to create one room per user")
            return redirect("create_room")
        room = rooms(name = room_name, creator = user)
        room.save()
       
        
        return redirect("home")
    return render(request, "core/createroom.html")

def joinRoom(request, id):
    
    room = rooms.objects.get(id = id)
    return render(request, "core/chat.html", {
        "room" : room, 
    })

def deleteroom(request, id):
    room = rooms.objects.get(id = id)
    room.delete()
    return redirect("home")

