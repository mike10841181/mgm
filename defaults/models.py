from django.db import models
from mgm.cliente.models import TipoDeCliente, Antiguedad
from mgm.pedido.models import EstadoDePedido

# Create your models here.

class ValoresPorDefecto(models.Model):
	tipoDeCliente = models.ForeignKey(TipoDeCliente, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "tipo de cliente")
	antiguedad = models.ForeignKey(Antiguedad, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "antiguedad")
	estadoDePedido = models.ForeignKey(EstadoDePedido, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "estado de pedido")
	
	def __unicode__(self):
		return "Valores por defecto"
		
	class Meta:
		verbose_name_plural = "valores por defecto"
