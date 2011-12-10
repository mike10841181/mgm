from django.db import models
from mgm.detalle.models import Detalle

# Create your models here.

class DetalleDeInventario(Detalle):
	
	def __unicode__(self):
		return super.__unicode__()
		
	class Meta:
		verbose_name_plural = "detalles de inventario"
