from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class RoomCategory(models.Model):
    name = models.CharField(max_length=20)

class RoomDescription(models.Model):
    description = models.CharField(max_length=1000)

class Room(models.Model):
    number = models.CharField(max_length=5)
    category = models.ForeignKey(RoomCategory, null=True, on_delete=models.SET_NULL)
    description = models.ForeignKey(RoomDescription, null=True, on_delete=models.SET_NULL)

#TODO: set default name of file
class Image(models.Model):
    room_description = models.ForeignKey(RoomDescription, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='media/')
    
class Reservation(models.Model):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)
    adults_count = models.IntegerField()
    register_datetime = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.DecimalField(max_digits = 5, decimal_places=2)

class Payment(models.Model):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=200)
    reservation = models.ForeignKey(Reservation, null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits = 5, decimal_places=2)
