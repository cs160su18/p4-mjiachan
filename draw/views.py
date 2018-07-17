from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.utils.safestring import mark_safe
from .models import Event
import json

def index(request):
    return render(request, 'draw/index.html', {})

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

def display(request):
    
    event_list = Event.objects.all()
    length = len(event_list)
    events = [False] * 4
    i = 0
    for i in range(length): 
        events[i] = event_list[i]
        
    context = {
        'event1': events[0],
        'event2': events[1],
        'event3': events[2],
        'event4': events[3],
    }
    return render(request, 'draw/prototype/display.html', context)

def customer(request):
    if request.method == 'POST':
        name = request.POST['name'].strip()
        time = request.POST['time'].strip()
        Event.objects.create(name=name, time=time)
    else:
        pass
    event_list = Event.objects.all()
    context = {
        'event_list': event_list,
    }
    return render(request, 'draw/prototype/customer.html', context)














# END

