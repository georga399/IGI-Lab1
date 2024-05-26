import logging
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, get_user
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test

from hotelsystem.forms import BookingForm
from .models import Image, Reservation, Payment, Room, RoomCategory
from accounts.models import Client, PromoInstance

logger = logging.getLogger(__name__)

def rooms(request):
    logger.info("GET rooms list")
    rooms = Room.objects.all()
    categories = RoomCategory.objects.all()
    category_id = request.GET.get('category')
    capacity = request.GET.get('capacity')

    if category_id:
        rooms = rooms.filter(category_id=category_id)
    if capacity:
        rooms = rooms.filter(capacity=int(capacity))

    context = {
        'rooms': rooms,
        'categories': categories
    }
    return render(request, 'rooms.html', context)

def room(request, id):
    room = get_object_or_404(Room, id=id)
    images = Image.objects.filter(room=room)
    context = {
        'room': room,
        'images': images
    }
    return render(request, 'room.html', context)

@login_required
def book_room(request, room_id):
    if(request.user.is_staff):
        return redirect('staff_cabinet')

    room = get_object_or_404(Room, id=room_id)
    form = BookingForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        #TODO: validate date of booking
        reservation = form.save(commit=False)
        reservation.user = request.user
        reservation.save()

        payment = Payment.objects.create(
            user=request.user,
            description='Room Booking Payment',
            reservation=reservation,
            amount=reservation.price
        )

        room.status = '2'
        room.save()

        return render(request, 'booking_success.html', {'reservation': reservation})

    return render(request, 'book_room.html', {'room': room, 'form': form})

@login_required 
def personal_cabinet(request):
    if(request.user.is_staff):
        return redirect('staff_cabinet')

    client = Client.objects.get(user=request.user)
    reservations = Reservation.objects.filter(user=request.user)
    payments = Payment.objects.filter(user=request.user)
    active_promos = PromoInstance.objects.filter(client=client, status='1')
    archived_promos = PromoInstance.objects.filter(client=client, status='2')

    return render(request, 'personal_cabinet.html', {'reservations': reservations, 
                                                     'payments': payments, 
                                                     'active_promos': active_promos, 
                                                     'archived_promos': archived_promos,
                                                     })

@login_required
def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.user != reservation.user and not request.user.is_staff:
        return redirect('access_denied')
    
    if request.method == 'POST':
        # Update reservation data based on submitted form

        #TODO: Delete this attributes
        # reservation.adults_count = request.POST.get('adults_count')

        #TODO: Validate start date and end date
        reservation.start_date = request.POST.get('start_date')
        reservation.end_date = request.POST.get('end_date')
        reservation.price = request.POST.get('price')
        reservation.save()

        return redirect('personal_cabinet')

    return render(request, 'edit_reservation.html', {'reservation': reservation})

@login_required
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.user != reservation.user and not request.user.is_staff:
        return redirect('access_denied')

    if request.method == 'POST':
        reservation.delete()
        return redirect('personal_cabinet')

    return render(request, 'delete_reservation.html', {'reservation': reservation})

@user_passes_test(lambda u: u.is_staff)
def staff_cabinet(request):
    reservations = Reservation.objects.all()
    users = get_user_model().objects.all()
    return render(request, 'staff_cabinet.html', {'reservations': reservations, 'users': users})