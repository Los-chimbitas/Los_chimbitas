from ..models import Empleo


def get_empleos():
    empleos=Empleo.objects.all()
    return empleos
def get_empleo(var_pk):
    empleo = Empleo.objects.get(pk=var_pk)
    return empleo
def empleo_create(form):
    empleo = form.save()
    empleo.save()
    return ()
def update_empleo(emp_pk,new_emp):
    empleo = get_empleo(emp_pk)
    empleo.nombre=new_emp["nombre"]
    empleo.save()
    return empleo
