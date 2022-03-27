from django.http import HttpResponse
from .logic import logic_variable as vl
from django.core import serializers
def empleos_view(request):
    if request.method == 'GET':
        empleos=vl.get_empleos()
        empleos_dto = serializers.serialize('json', empleos)
    return HttpResponse(empleos_dto,'application/json')