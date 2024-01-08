# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 14:44:26 2024

@author: ASUS
"""

from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('sample/', views.sample, name='sample'),
    path('allmembers/', views.allmembers, name='allmembers'),
    path('details/<int:id>', views.details, name='details'),
    path('saveMember/', views.saveMember, name='saveMember'),

]