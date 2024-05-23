from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(unique=True, region="BY")
    count_of_childs = models.IntegerField()
    date_of_birth = models.DateField()

class Employee(models.Model):
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(unique=True, region="BY")
    salary = models.FloatField()
    date_of_birth = models.DateField()
    
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    employees = models.ManyToManyField(Employee)