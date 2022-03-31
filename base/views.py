from django.shortcuts import render
from django.http import HttpResponse

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
