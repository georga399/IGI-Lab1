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
from django.views.static import serve
import accounts.views
import hotelinfo.views
import hotelsystem.views

handler404 = 'hotelinfo.views.handler404'
handler403 = 'hotelinfo.views.handler403'

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    re_path(r'.+policy/?$', hotelinfo.views.policy, name='policy'),
    re_path(r".+about/?$", hotelinfo.views.about, name='about'),
    re_path(r'^$', hotelinfo.views.general, name='general'),
    re_path(r'^news/$', hotelinfo.views.news, name='news'),
    re_path(r'^article/(?P<id>\d+)$', hotelinfo.views.article, name='article'),
    re_path(r'^faq/$', hotelinfo.views.faq, name='faq'),
    re_path(r'^contacts/$', hotelinfo.views.contacts, name='contacts'),
    re_path(r'^vacancy/$', hotelinfo.views.vacancy, name='vacancy'),
    re_path(r'^reviews/$', hotelinfo.views.reviews, name='reviews'),
    re_path(r'^add_review/$', hotelinfo.views.add_review, name='add_review'),
    re_path(r'^promo/$', hotelinfo.views.promos, name='promo'),
    re_path(r'^joker/$', hotelinfo.views.joker, name='joker'),

    re_path(r'^register/$', accounts.views.register, name='register'),
    re_path(r'^login/$', accounts.views.login, name='login'),
    re_path(r'^logout/$', accounts.views.logout, name='logout'),

    re_path(r'^rooms/$', hotelsystem.views.rooms, name='rooms'),
    re_path(r'^room/(?P<id>\d+)$', hotelsystem.views.room, name='room'),
    re_path(r'^book_room/(?P<room_id>\d+)$', hotelsystem.views.book_room, name='book_room'),

    re_path(r'^personal_cabinet/$', hotelsystem.views.personal_cabinet, name='personal_cabinet'),
    re_path(r'^staff_cabinet/$', hotelsystem.views.staff_cabinet, name='staff_cabinet'),

    re_path(r'^edit_reservation/(?P<reservation_id>\d+)$', hotelsystem.views.edit_reservation, name='edit_reservation'),
    re_path(r'^delete_reservation/(?P<reservation_id>\d+)$', hotelsystem.views.delete_reservation, name='delete_reservation'),
    re_path(r'.+policy/?$', hotelinfo.views.policy, name='policy'),
    re_path(r".+about/?$", hotelinfo.views.about, name='about'),
    re_path(r".+cart_payment/", hotelsystem.views.cart_payment, name='cart_payment'),
    path("carES6/", hotelinfo.views.carES6, name='carES6' ),
    path("carProto/", hotelinfo.views.carES6, name='carProto' ),
    path("taylor/", hotelinfo.views.taylor, name='taylor')

] 
# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


