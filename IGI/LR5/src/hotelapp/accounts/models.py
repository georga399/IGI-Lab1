from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from utils.get_image_filename import get_image_filename
from hotelinfo.models import Promo

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(unique=True, region="BY")
    count_of_childs = models.IntegerField()
    date_of_birth = models.DateField()
    promos = models.ManyToManyField(Promo, through="PromoInstance")

class Employee(models.Model):
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(unique=True, region="BY")
    salary = models.FloatField()
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to=get_image_filename('employees'), blank=True)
    
class JobTitle(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    employees = models.ManyToManyField(Employee)

class PromoInstance(models.Model):
    PROMO_STATUS = (
        ("1", "active"),
        ("2", "archived")
    )
    status = models.CharField(max_length=1, choices=PROMO_STATUS)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    promo = models.ForeignKey(Promo, on_delete=models.CASCADE)
    amount = models.FloatField()


