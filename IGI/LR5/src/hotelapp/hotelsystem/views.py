import datetime
from decimal import Decimal
import logging
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, get_user
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone

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

    logger.info(f'book_room: Room status {room.status}')
    if(room.status == "2"):
        return redirect('rooms')

    if request.method == 'POST':
        days = request.POST.get('days')    
        if days is None:
            days = 1
        else:
            days = int(days)
        promo_instance_id = request.POST.get('promo_instance')
        start_date = timezone.now()
        end_date = start_date + datetime.timedelta(days=days)

        # Calculate the payment amount
        one_day_cost = room.one_day_cost
        amount = float(one_day_cost * days)

        reservation = Reservation.objects.create(
                user=request.user,
                start_date=start_date,
                end_date=end_date,
                room=room,
                adults_count=room.capacity,
                price=Decimal(amount)
        )
        room.status = '2'
        room.save()

        # Retrieve selected promo instance from the form
        discount = 0
        if(promo_instance_id is not None):
            promo_instance = get_object_or_404(PromoInstance, id=promo_instance_id)
            discount = promo_instance.amount
                    # Disable the selected promo instance
            promo_instance.status = '2'
            promo_instance.save()


        # Create a payment object    
        payment = Payment.objects.create(
                user=request.user,
                description='Room Reservation',
                reservation=reservation,
                amount= max(0, amount - discount)  # Assuming price is calculated and set in the Reservation model
            )
        



        return render(request, 'booking_success.html', {'reservation': reservation})


    client = Client.objects.filter(user=request.user).first()
    promos = PromoInstance.objects.filter(client=client, status='1')

    return render(request, 'book_room.html', {'room': room, 'promos':promos })

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
        days = request.POST.get('days')
        if(days is None):
            return redirect('personal_cabinet')

        else:
            days = int(days)

        if(reservation.end_date < timezone.now()):
            reservation.delete()
            reservation.room.status = '1'
            return redirect('personal_cabinet')

        # reservation.start_date = request.POST.get('start_date')

        prev_end_date = reservation.end_date

        reservation.end_date = timezone.now() + datetime.timedelta(days=days)

        
        days_delta = -(prev_end_date - reservation.end_date).days

        if(prev_end_date < reservation.end_date):
            lamount = float(reservation.room.one_day_cost*days_delta)
            logger.info(f"type: {type(lamount)}")
            if(lamount > 0):
                reservation.price += float(lamount)
                payment = Payment.objects.create(
                    user=request.user,
                    description='Changing reservation',
                    # reservation=reservation,
                    amount = reservation.price 
                )
        

        reservation.save()

        return redirect('personal_cabinet')

    return render(request, 'edit_reservation.html', {'reservation': reservation})

@login_required
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.user != reservation.user and not request.user.is_staff:
        return redirect('access_denied')
    if request.method == 'POST':
        room = reservation.room
        room.status = '1'
        room.save()
        reservation.delete()
        return redirect('personal_cabinet')

    return render(request, 'delete_reservation.html', {'reservation': reservation})

@user_passes_test(lambda u: u.is_staff)
def staff_cabinet(request):
    reservations = Reservation.objects.all()
    clients = Client.objects.all()
    return render(request, 'staff_cabinet.html', {'reservations': reservations, 'clients': clients})