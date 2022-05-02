from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RoomForm

from .models import Room

# Create your views here.
#rooms = [
#    {'id': 1, 'name': 'lets learn something'},
#    {'id': 2, 'name': 'design with me'},
#    {'id': 3, 'name': 'lets learn something'},
#]

def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {
        'rooms': rooms
    })

def index(request, pk):
    room = Room.objects.get(id=pk)
    return render(request, 'base/rooms.html', {'room': room})

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'base/room_form.html', context) 

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj' : room})