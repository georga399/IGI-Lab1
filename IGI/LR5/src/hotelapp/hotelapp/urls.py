"""
URL configuration for hotelapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
import accounts.views
import hotelinfo.views
import hotelsystem.views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    path('policy/', hotelinfo.views.policy, name='policy'),
    path("about/", hotelinfo.views.about, name='about'),
    path('', hotelinfo.views.general),
    path('news/', hotelinfo.views.news, name='news'),
    path('article/<int:id>', hotelinfo.views.article),
    # path('faqs/', hotelinfo.views.faqs, name='faqs'),
    # path('contacts/', hotelinfo.views.contacts, name='contacts'),
    # path('jobs/', hotelinfo.views.jobs, name='jobs'),
    # path('reviews/', hotelinfo.views.reviews, name='reviews'),
    # path('create_review/', hotelinfo.views.create_review, name='create_review'),
    # path('promo/', hotelinfo.view.promo, name='promo'),

    path('register/', accounts.views.register, name='register'),
    path('login/', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name='logout'),
    
    path("client_home/", hotelsystem.views.client_home, name='client_home'), # list of user bookings, list of user payments
    # path("staff_home/", hotelsystem.views.staff_home, name='staff_home'), # list of all bookings, # list of all users
    # path('rooms/', hotelsystem.views.rooms, name='rooms'),
    # re_path('roominfo-<>', hotelsystem.views.roominfo, )
    # re_path('booking/<id>')
    # re_path("book_room/<int>"),
    # path('make-payment/<booking-id>')
    # path('payments/<userid>',)

    
]
