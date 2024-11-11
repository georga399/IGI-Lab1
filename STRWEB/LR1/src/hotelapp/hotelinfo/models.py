from django.db import models
from django.contrib.auth import get_user_model

from utils.get_image_filename import get_image_filename

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=1000)
    body = models.CharField(max_length=10000)
    image = models.ImageField(upload_to=get_image_filename('articles'), blank=True)
    last_modified_date = models.DateTimeField(auto_now=True) 

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

class Review(models.Model):
    body = models.CharField(max_length=500)
    user = models.OneToOneField(get_user_model(), on_delete = models.CASCADE, primary_key = True)

class Company(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

class Promo(models.Model):
    PROMO_STATUS =(
        ("1", "active"), 
        ("2", "expired")
    )
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    expire_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    amount = models.FloatField()
    status = models.CharField(max_length=1, choices=PROMO_STATUS)
    
class Partner(models.Model): 
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='static/partner_logos/')
    url = models.URLField()