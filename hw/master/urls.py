# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 14:44:26 2024

@author: ASUS
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('testing/', views.testing, name='testing'),    

    path('master/', views.members, name='master'),
    path('sample1/', views.sample, name='sample'),
    path('allmembers1/', views.allmembers, name='allmembers'),
    path('master/details/<int:id>', views.details, name='details'),

]