
from django.contrib import admin
from django.conf.urls import url
from django.urls import path

from . import views
from django.conf.urls import include

urlpatterns = [
    # /music/
    path('sentiment/', views.index, name='index'),
    path('analysis/', views.analysis, name='analysis'),
    path('home/',views.home , name='home'),
    path('', views.indexpage, name='index'),
    path('sentiment/hist/', views.hist, name='hist'),

]