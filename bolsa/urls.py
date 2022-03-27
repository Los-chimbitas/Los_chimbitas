from django.contrib import admin
from django.urls import path
from . import views
urlpatterns= [
    path('',views.empleos_view,name='empleos_view')
]