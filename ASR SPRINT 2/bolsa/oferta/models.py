from django.db import models

class Oferta(models.Model):
      ofertap = models.CharField(max_length=350)

      def __str__(self):
          return '{}'.format(self.ofertap)

# Create your models here.
