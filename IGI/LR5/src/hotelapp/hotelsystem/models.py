from django.db import models
from django.contrib.auth import get_user_model
from utils.get_image_filename import get_image_filename

# Create your models here.
class RoomCategory(models.Model):
    name = models.CharField(max_length=20)

class Room(models.Model):
    ROOM_STATUS = ( 
    ("1", "available"), 
    ("2", "not available"),    
    )
    number = models.CharField(max_length=5)
    category = models.ForeignKey(RoomCategory, null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    status = models.CharField(choices =ROOM_STATUS,max_length = 15)
    capacity = models.SmallIntegerField()
    one_day_cost = models.FloatField()

class Image(models.Model):
    room = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to=get_image_filename('rooms'))
    
class Reservation(models.Model):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)
    adults_count = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.FloatField()
    room = models.ForeignKey(Room, null=True, on_delete=models.CASCADE)

class Payment(models.Model):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=200)
    reservation = models.ForeignKey(Reservation, null=True, on_delete=models.SET_NULL)
    amount = models.FloatField()
