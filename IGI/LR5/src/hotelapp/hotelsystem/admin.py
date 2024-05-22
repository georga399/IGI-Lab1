from django.contrib import admin
from .models import RoomCategory, RoomDescription, Room, Payment, Reservation

# Register your models here.
admin.site.register(RoomCategory)
admin.site.register(RoomDescription)
admin.site.register(Room)
admin.site.register(Payment)
admin.site.register(Reservation)
