from django.db import models
from mgm.persona.models import Persona

# Create your models here.

class AreaDepartamento(models.Model):
	idAreaDepartamento = models.AutoField(primary_key = True)
	nombre = models.CharField("nombre de departamento", max_length = 30, null = False, blank = False)
	descripcion = models.CharField("descripcion de departamento", max_length = 50, null = False, blank = False)
	eliminada = models.BooleanField("eliminado", null = False, blank = False)
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)
	
	def __unicode__(self):
		return self.nombre
		
	class Meta:
		ordering = ['nombre']
		verbose_name_plural = "departamentos"

class TipoDeEmpleado(models.Model):
	idTipoDeEmpleado = models.AutoField(primary_key = True)
	nombre = models.CharField("nombre de tipo", max_length = 30, null = False, blank = False)
	descripcion = models.CharField("descripcion de tipo", max_length = 50, null = False, blank = False)
	areaDepartamento = models.ForeignKey(AreaDepartamento, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "departamento")
	eliminada = models.BooleanField("eliminado", null = False, blank = False)	
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)
	
	def __unicode__(self):
		return self.nombre
		
	class Meta:
		ordering = ['nombre']
		verbose_name_plural = "tipos de empleado"

class Empleado(Persona):
	tipoDeEmpleado = models.ForeignKey(TipoDeEmpleado, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "tipo de empleado")
		
	class Meta:
		verbose_name_plural = "empleados"
