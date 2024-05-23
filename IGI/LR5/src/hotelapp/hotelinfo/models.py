from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=2000)
    last_modified_date = models.DateTimeField(auto_now=True) 

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

class Discount(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    expire_date = models.DateTimeField(auto_now=False, auto_now_add=False)

class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

class Review(models.Model):
    body = models.CharField(max_length=500)
    user = models.OneToOneField(get_user_model(), on_delete = models.CASCADE, primary_key = True)

class Company(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)