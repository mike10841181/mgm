from django.db import models
from mgm.detalle.models import Detalle

# Create your models here.
class OrdenDeProduccion(models.Model):
	eliminada = models.BooleanField("eliminada", null = False, blank = False)
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)
	
	class Meta:
		verbose_name_plural = "ordenes de produccion"

class DetalleDeProduccion(Detalle):
	ordeDeProduccion = models.ForeignKey(OrdenDeProduccion, null = False, blank = False, verbose_name = "Estado de pedido")

	def __unicode__(self):
		return super.__unicode__()
	
	class Meta:
		verbose_name_plural = "detalles de produccion"
