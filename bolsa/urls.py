from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
urlpatterns= [
    path('empleos/',views.empleos_view,name='empleos_view'),
    path('empleos/<int:pk>', views.empleo_view, name='empleo_view'),
    path('empleocreate/',csrf_exempt(views.empleos_view), name='empleoCreate')
]