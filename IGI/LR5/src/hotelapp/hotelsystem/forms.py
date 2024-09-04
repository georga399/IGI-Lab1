from django import forms
from decimal import Decimal

from accounts.models import PromoInstance
from .models import Reservation

class BookingForm(forms.Form):
    days = forms.IntegerField(label="Number of days")
    promo_instance = forms.ModelChoiceField(queryset=PromoInstance.objects.filter(status='1'))