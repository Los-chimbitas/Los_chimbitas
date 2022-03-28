import json

from django.http import HttpResponse
from .logic import logic_variable as vl
from django.core import serializers
from .forms import EmpleoForm
from django.contrib import messages
def empleos_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            empleo_dto= vl.get_empleo(id)
            empleo= serializers.serialize('json',[empleo_dto,])
            return HttpResponse(empleo,'application/json')
        else:
            empleos_dto = vl.get_empleos()
            empleos =serializers.serialize('json',empleos_dto)
            return HttpResponse(empleos,'application/json')
    if request.method =='POST':
        empleo_dto=vl.empleo_create(json.loads(request.body))
        empleo= serializers.serialize('json',[empleo_dto,])
        return HttpResponse(empleo,'application/json')

def empleo_view(request, pk):
    if request.method == 'GET':
        empleo=vl.get_empleo(pk)
        empleo_dto=serializers.serialize('json',empleo)
        return HttpResponse(empleo_dto, 'application/json')
    if request.method == 'PUT':
        empleo_dto =vl.update_empleo(pk,json.loads(request.body))
        empleo = serializers.serialize('json',[empleo_dto,])
        return HttpResponse(empleo, 'application/json')
