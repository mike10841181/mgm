from django.db import models
from mgm.persona.models import Persona

# Create your models here.

class Antiguedad(models.Model):
	idAntiguedad = models.AutoField(primary_key = True)
	nombre = models.CharField("nombre de antiguedad", max_length = 30, null = False, blank = False, unique = True)
	descripcion = models.CharField("descripcion de antiguedad", max_length = 50, null = False, blank = False)
	porcentajeDescuento = models.PositiveIntegerField("porcentage de descuento", null = False, blank = False)
	eliminada = models.BooleanField("eliminada", null = False, blank = False)
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)
	
	def __unicode__(self):
		return self.nombre
	
	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "tipos de antiguedad"

class TipoDeCliente(models.Model):
	idTipoDeCliente = models.AutoField(primary_key = True)
	nombre = models.CharField("nombre de tipo", max_length = 30, null = False, blank = False)
	descripcion = models.CharField("descripcion de tipo", max_length = 50, null = False, blank = False)
	porcentajeDescuento = models.PositiveIntegerField("porcentage de descuento", null = False, blank = False, unique = True)
	eliminada = models.BooleanField("eliminado", null = False, blank = False)
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)
	
	def __unicode__(self):
		return self.nombre
		
	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "tipos de cliente"

class Cliente(Persona):
	tipoDeCliente = models.ForeignKey(TipoDeCliente, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "tipo de cliente")
	antiguedad = models.ForeignKey(Antiguedad, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "antiguedad")
	
	class Meta:
		verbose_name_plural = "clientes"
