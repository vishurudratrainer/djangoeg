# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 14:44:26 2024

@author: ASUS
"""

from django.urls import path
from . import views

urlpatterns = [
    path('variable/', views.variables, name='templateeg'),
    path('varintemplate/', views.varintemplate, name='varintemplate'),
    path('listtest/', views.listtest, name='listtest'),
    path('ifelseeg/', views.ifelseeg, name='ifelseeg'),
    path('fornested/', views.fornested, name='fornested'),

]