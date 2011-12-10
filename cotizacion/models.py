from django.db import models
from mgm.cliente.models import Cliente
from mgm.detalle.models import Detalle

# Create your models here.

class Cotizacion(models.Model):
	idCotizacion = models.AutoField(primary_key = True)
	cliente = models.ForeignKey(Cliente, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "cliente")
	subTotal = models.DecimalField("sub-total", max_digits = 8, decimal_places = 2, null = False, blank = False)
	isv = models.DecimalField("impuesto", max_digits = 8, decimal_places = 2, null = False, blank = False)
	total = models.DecimalField("total", max_digits = 8, decimal_places = 2, null = False, blank = False)
	eliminada = models.BooleanField("eliminada", null = False, blank = False)
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)
	
	def __unicode__(self):
		return u"%s %s - %s" % (self.cliente.first_name, self.cliente.last_name, self.fechaDeCreacion)
	
	class Meta:
		ordering = ["fechaDeCreacion"]
		verbose_name_plural = "cotizaciones"
		
class DetalleDeCotizacion(Detalle):
	cotizacion = models.ForeignKey(Cotizacion, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "cotizacion")
	precioUnitario = models.DecimalField("precio unitario", max_digits = 8, decimal_places = 2, null = False, blank = False)
	subTotal = models.DecimalField("sub-total", max_digits = 8, decimal_places = 2, null = False, blank = False)
	isv = models.DecimalField("impuesto", max_digits = 8, decimal_places = 2, null = False, blank = False)
	total = models.DecimalField("total", max_digits = 8, decimal_places = 2, null = False, blank = False)

	def __unicode__(self):
		return super.unicode()
		
	class Meta:
		verbose_name_plural = "detalles de cotizacion"
