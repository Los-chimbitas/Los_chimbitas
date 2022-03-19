from django.shortcuts import render

from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import OfertaForm
from .logic.oferta_logic import get_ofertas, create_oferta
def ofertas_list(request):
    ofertas = get_ofertas()
    context = {
        'ofertas_list': ofertas
    }
    return render(request, 'Oferta/ofertas.html', context)

def oferta_create(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST)
        if form.is_valid():
            create_oferta(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created oferta')
            return HttpResponseRedirect(reverse('ofertaCreate'))
        else:
            print(form.errors)
    else:
        form = OfertaForm()

    context = {
        'form': form,
    }
    return render(request, 'Oferta/ofertaCreate.html', context)

# Create your views here.
