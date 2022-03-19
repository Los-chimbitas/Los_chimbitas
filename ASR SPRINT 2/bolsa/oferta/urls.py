from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('ofertas/', views.ofertas_list, name='ofertasList'),
    path('ofertacreate/', csrf_exempt(views.oferta_create), name='ofertaCreate'),
]