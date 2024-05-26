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
from django.conf.urls.static import static
from django.conf import settings
import accounts.views
import hotelinfo.views
import hotelsystem.views

handler404 = 'hotelinfo.views.handler404'
handler403 = 'hotelinfo.views.handler403'

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    path('policy/', hotelinfo.views.policy, name='policy'),
    path("about/", hotelinfo.views.about, name='about'),
    path('', hotelinfo.views.general, name='general'),
    path('news/', hotelinfo.views.news, name='news'),
    path('article/<int:id>', hotelinfo.views.article, name='article'),
    path('faq/', hotelinfo.views.faq, name='faq'),
    path('contacts/', hotelinfo.views.contacts, name='contacts'),
    path('vacancy/', hotelinfo.views.vacancy, name='vacancy'),
    path('reviews/', hotelinfo.views.reviews, name='reviews'),
    path('add_review/', hotelinfo.views.add_review, name='add_review'),
    path('promo/', hotelinfo.views.promos, name='promo'),

    path('register/', accounts.views.register, name='register'),
    path('login/', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name='logout'),
    
    path('rooms/', hotelsystem.views.rooms, name='rooms'),
    path('room/<int:id>', hotelsystem.views.room, name='room'),

    path('book_room/<int:room_id>', hotelsystem.views.book_room, name='book_room'),
    path('personal_cabinet/', hotelsystem.views.personal_cabinet, name='personal_cabinet'),
    path('staff_cabinet/', hotelsystem.views.staff_cabinet, name='staff_cabinet'),
    path('edit_reservation/<int:reservation_id>', hotelsystem.views.edit_reservation, name='edit_reservation'),
    path('delete_reservation/<int:reservation_id>', hotelsystem.views.delete_reservation, name='delete_reservation'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
