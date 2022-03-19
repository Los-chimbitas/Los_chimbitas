from ..models import Oferta

def get_ofertas():
    queryset = Oferta.objects.all()
    return (queryset)

def create_oferta(form):
    oferta = form.save()
    oferta.save()
    return ()