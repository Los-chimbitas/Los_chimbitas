import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .logic import logic_variable as vl
from django.core import serializers
from .forms import EmpleoForm
from django.contrib import messages

from .logic.logic_variable import empleo_create


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
    elif request.method == 'PUT':
        empleo_dto =vl.update_empleo(pk,json.loads(request.body))
        empleo = serializers.serialize('json',[empleo_dto,])
        return HttpResponse(empleo, 'application/json')

def empleo_createa(request):
    if request.method == 'POST':
        form = EmpleoForm(request.POST)
        if form.is_valid():
            empleo_create(form)
            messages.add_message(request, messages.SUCCESS, 'Measurement create successful')
            return HttpResponseRedirect(reverse('empleocreate'))
        else:
            print(form.errors)
    else:
        form = EmpleoForm()

    context = {
        'form': form,
    }

    return render(request, 'Bolsa/empleoCreate.html', context)
