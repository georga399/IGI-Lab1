from django.test import TestCase, Client as TestClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.models import *
from hotelinfo.models import *
from datetime import datetime, timedelta
from hotelsystem.models import *
from django.utils import timezone
import json

class RoomViewsTestCase(TestCase):
    def setUp(self):
        self.client = TestClient()
        self.user = get_user_model().objects.create_user(username='testuser', password='password')
        self.staff_user = get_user_model().objects.create_user(username='staffuser', password='password', is_staff=True)
        self.category = RoomCategory.objects.create(name='Standard')
        self.room = Room.objects.create(number='101', category=self.category, description='A nice room', status='1', capacity=2, one_day_cost=100.0)
        self.client_user = Client.objects.create(user=self.user, phone_number='+1234567890', count_of_childs=0, date_of_birth='1990-01-01')
        self.promo = PromoInstance.objects.create(status='1', client=self.client_user, promo=Promo.objects.create(
            title='Promo1',
            description='Promo description',
            start_date=timezone.now(),
            expire_date=timezone.now() + timedelta(days=10),
            amount=10.0,
            status='1'
        ), amount=10.0)

    def test_rooms_view(self):
        response = self.client.get(reverse('rooms'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.room.description)

    def test_room_view(self):
        response = self.client.get(reverse('room', args=[self.room.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.room.description)

    def test_book_room_view_get(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('book_room', args=[self.room.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.room.description)

    def test_edit_reservation_view(self):
        self.client.login(username='testuser', password='password')
        reservation = Reservation.objects.create(user=self.user, room=self.room, start_date=timezone.now(), end_date=timezone.now() + timedelta(days=1), adults_count=1, price=100.0)
        response = self.client.post(reverse('edit_reservation', args=[reservation.id]), {'days': 2})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('personal_cabinet'))
        reservation.refresh_from_db()
        self.assertEqual((reservation.end_date - reservation.start_date).days, 2)

    def test_delete_reservation_view(self):
        self.client.login(username='testuser', password='password')
        reservation = Reservation.objects.create(user=self.user, room=self.room, start_date=timezone.now(), end_date=timezone.now() + timedelta(days=1), adults_count=1, price=100.0)
        response = self.client.post(reverse('delete_reservation', args=[reservation.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('personal_cabinet'))
        self.assertFalse(Reservation.objects.filter(id=reservation.id).exists())

    def test_staff_cabinet_redirect(self):
        self.client.login(username='staffuser', password='password')
        response = self.client.get(reverse('personal_cabinet'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('staff_cabinet'))