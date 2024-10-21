from django.shortcuts import render,redirect
from .models import rooms
# Create your views here.
def home(request):
    room = rooms.objects.all()
    return render(request, "core/home.html", {
        "rooms" : room
    })

def createRoom(request):
    if request.method == "POST":
        room_name = request.POST.get("roomname")
        room = rooms(name = room_name)
        room.save()
        return redirect("home")
    return render(request, "core/createroom.html")

def joinRoom(request, id):
    room = rooms.objects.get(id = id)
    return render(request, "core/room.html", {
        "room" : room
    })