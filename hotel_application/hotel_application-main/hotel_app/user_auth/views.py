from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .forms import  NewUserForm , UpdateUserForm 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from main.models import *
# Create your views here.

def user_register(request):
    if request.method == "POST":
        register_form = NewUserForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect('main:index')
    register_form = NewUserForm()
    return render(request=request, template_name='user_auth/register.html', context={'register_form': register_form})

def user_login(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('main:index')       
        else:
            messages.error(request, 'Invalid username or password')
    else:
        login_form = AuthenticationForm()

    return render(request, 'user_auth/login.html', {'login_form': login_form})

@login_required
def user_cab(request):
    try:
        user_reservation = Reservation.objects.get(user=request.user)
        if user_reservation:
            # Calculate total price
            check_in = user_reservation.check_in
            check_out = user_reservation.check_out
            nights = (check_out - check_in).days
            total_price = nights * user_reservation.room.price
        else:
            total_price = None
            
    except Reservation.DoesNotExist:
        user_reservation = None
        total_price = None

    if request.user.is_authenticated:
        username = request.user.username
        print(username)

    return render(request, 'user_auth/cab.html', {
        'user_reservation': user_reservation,
        'total_price': total_price,
    }) 
    
# def user_cab(request):
#     try:
#         user_reservation = Reservation.objects.get(user=request.user)
#     except Reservation.DoesNotExist:
#         user_reservation = None

#     if request.user.is_authenticated:
#         username = request.user.username
#         print(username)

#     return render(request, 'user_auth/cab.html', {'user_reservation': user_reservation})

def user_logout(request):
    logout(request)
    return redirect('main:index')


def user_change(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('main:index')
    else:
        user_form = UpdateUserForm(instance=request.user)
    return render(request, 'user_auth/change_profile.html',{'user_form': user_form})

