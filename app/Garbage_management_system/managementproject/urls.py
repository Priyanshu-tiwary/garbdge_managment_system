from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
     path('', home, name='home'),
     path('login/', login, name='login'),
     path('register/', register, name='register'),
     path('dashboard/', dashboard, name='dashboard'),
     path('dashboardfordriver/', dashboard_for_driver, name='dashboard_for_driver'),
     path('complaintform/', complaint_form, name='complaint_form'),
     path('honor/', honor, name='honor'),

]