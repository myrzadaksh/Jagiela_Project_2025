from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q

def index(request):
    rooms = Room.objects.all()
    return render(request,'main/index.html',{'rooms': rooms,})

def about_us(request):
    hotel = HotelInfo.objects.get(id=1)
    return render(request,'main/about_us.html',{'hotel': hotel,})

def detail(request, room_id):
    try:
        room = Room.objects.get(id=room_id)
    except:
        return redirect('/')
    return render (request, 'main/detail.html', {'room': room})

# @login_required(login_url='/')
def make_reservation(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if not request.user.is_authenticated:
        messages.error(request, 'You need to sign in to make a reservation.')
        return redirect('/')
    if not room.is_available:
        messages.error(request, 'This room is not available for reservation.')
        return redirect('/')
    if request.method == "POST":
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        number_of_guests = request.POST['number_of_guests']
        
        reservation = Reservation(
            user=request.user,
            room=room,
            check_in=check_in,
            check_out=check_out,
            number_of_guests=number_of_guests
        )
        reservation.save()
        room.is_available = False
        room.save()
        return redirect('/')
    
    return render(request, 'main/make_reservation.html', {'rooms': room, })

def search(request):
    rooms = []
    if request.method == 'GET':
        query = request.GET.get('q')
        print(query,"HEREREE")
        rooms = Room.objects.filter(Q(room_name__icontains=query))
    return render(request, 'main/index.html', {'query': query, 'rooms': rooms})

@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'main/reservation_list.html', {'reservations': reservations})