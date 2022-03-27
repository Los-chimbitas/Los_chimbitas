from django.db import models

class Empleo(models.Model):
    nombre = models.CharField(max_length=30)
    oferente= models.CharField(max_length=30)
    def __str__(self):
        return 'Ofrecido por: {}\n Propuesta:{}'.format(self.oferente, self.nombre)
