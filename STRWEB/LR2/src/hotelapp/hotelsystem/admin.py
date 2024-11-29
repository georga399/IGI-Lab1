from django.contrib import admin
from .models import RoomCategory, Room, Payment, Reservation, Image

# Register your models here.
admin.site.register(RoomCategory)
admin.site.register(Room)
admin.site.register(Payment)
admin.site.register(Reservation)
admin.site.register(Image)
