from django.urls import path

from . import views 
urlpatterns= [
path('',views.stat1,name='home'),
path('travel',views.Travel,name='travel'),
path('registration',views.Userregestration,name='registration'),
path('sample',views.sample,name='sample'),
path('login',views.loginpage,name='loginpage'),
path('logout',views.logout,name='logout'),
path('bus',views.bus,name='bus'),
path('seat',views.seat,name='seat'),
path('Ani',views.Ani,name='Ani'),



]  