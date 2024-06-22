from django.shortcuts import render
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
     path('' ,views.LoginView.as_view() , name='Login'),
     path('Home' ,views.HomeView.as_view() , name='Home'),
     path('custumers' ,views.custumerView.as_view() , name='custumers'),
     path('Messages' ,views.MessagesView.as_view() , name='Messages'),
     path('add' ,views.addCostumerView.as_view() , name='add'),
     path('add_Doctor' ,views.addDoctorView.as_view() , name='add_Doctor'),
     path('logout' ,views.HomeView.as_view() , name='logout'),
     path('user-logout', views.user_logout, name="user-logout"),
     

]