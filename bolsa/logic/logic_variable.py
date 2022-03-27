from ..models import Empleo


def get_empleos():
    empleos=Empleo.objects.all()
    return empleos