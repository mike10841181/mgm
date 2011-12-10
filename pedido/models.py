from django.db import models
from mgm.cliente.models import Cliente
from mgm.detalle.models import Detalle
from mgm.empleado.models import Empleado

# Create your models here.

class EstadoDePedido(models.Model):
	idEstadoDePedido = models.AutoField(primary_key = True)
	nombre = models.CharField("nombre de estado", max_length = 30, null = False, blank = False)
	descripcion = models.CharField("descripcion de estado", max_length = 50, null = False, blank = False)
	eliminada = models.BooleanField("eliminado", null = False, blank = False)	
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)
	
	def __unicode__(self):
		return self.nombre
	
	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "estados de pedido"
		
class Pedido(models.Model):
	idPedido = models.AutoField(primary_key = True)
	estado = models.ForeignKey(EstadoDePedido, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "estado de pedido")
	cliente = models.ForeignKey(Cliente, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "cliente")
	vendedor = models.ForeignKey(Empleado, limit_choices_to = {"eliminada" : False}, null = True, blank = True, default = None, verbose_name = "vendedor")
	subTotal = models.DecimalField("sub-total", max_digits = 8, decimal_places = 2, null = False, blank = False, default = 0)
	descuento = models.DecimalField("descuento", max_digits = 8, decimal_places = 2, null = False, blank = False, default = 0)
	isv = models.DecimalField("impuesto", max_digits = 8, decimal_places = 2, null = False, blank = False, default = 0)
	total = models.DecimalField("total", max_digits = 8, decimal_places = 2, null = False, blank = False, default = 0)
	eliminada = models.BooleanField("eliminado", null = False, blank = False, default = 0)
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)
	
	def __unicode__(self):
		return u"PED_%s" % (self.idPedido)
		
	class Meta:
		ordering = ["fechaDeCreacion"]
		verbose_name_plural = "pedidos"
		
class Factura(models.Model):
	idFactura = models.AutoField(primary_key = True)
	pedido = models.ForeignKey(Pedido, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "pedido")
	subTotal = models.DecimalField("sub-total", max_digits = 8, decimal_places = 2, null = False, blank = False)
	isv = models.DecimalField("impuesto", max_digits = 8, decimal_places = 2, null = False, blank = False)
	total = models.DecimalField("total", max_digits = 8, decimal_places = 2, null = False, blank = False)
	porcentajeDevengado = models.DecimalField("porcentaje devengado", max_digits = 4, decimal_places = 2, null = False, blank = False)
	eliminada = models.BooleanField("eliminada", null = False, blank = False)
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)
	
	def __unicode__(self):
		return u"%s %s - %s" % (self.pedido.cliente.first_name, self.pedido.cliente.last_name, self.fechaDeCreacion)
		
	class Meta:
		ordering = ["fechaDeCreacion"]
		verbose_name_plural = "facturas"
		
class DetalleDePedido(Detalle):
	pedido = models.ForeignKey(Pedido, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "pedido")
	descripcion = models.CharField("descripcion", max_length = 100, null = True, blank = True, default = "N/A")
	precioUnitario = models.DecimalField("precio unitario", max_digits = 8, decimal_places = 2, null = False, blank = False)
	subTotal = models.DecimalField("sub-total", max_digits = 8, decimal_places = 2, null = False, blank = False)
	isv = models.DecimalField("impuesto", max_digits = 8, decimal_places = 2, null = False, blank = False)
	total = models.DecimalField("total", max_digits = 8, decimal_places = 2, null = False, blank = False)
	
	def __unicode__(self):
		return super.__unicode__()
		
	class Meta:
		verbose_name_plural = "detalles de pedido"
