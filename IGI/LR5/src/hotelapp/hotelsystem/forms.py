from django import forms
from decimal import Decimal
from .models import Reservation

class BookingForm(forms.ModelForm):
    price = forms.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = Reservation
        fields = ['adults_count', 'start_date', 'end_date', 'price']