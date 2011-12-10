from django.db import models

# Create your models here.
	
class Color(models.Model):
	idColor = models.AutoField(primary_key = True)
	nombre = models.CharField("nombre de color", max_length = 20, null = False, blank = False, unique = True)
	descripcion = models.CharField("descripcion de color", max_length = 50, null = False, blank = False)
	eliminada = models.BooleanField("eliminado", null = False, blank = False)
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)
	
	def __unicode__(self):
		return self.nombre
		
	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "colores"

class Cuero(models.Model):
	idCuero = models.AutoField(primary_key = True)
	nombre = models.CharField("nombre de cuero", max_length = 20, null = False, blank = False, unique = True)
	descripcion = models.CharField("descripcion de cuero", max_length = 50, null = False, blank = False)
	eliminada = models.BooleanField("eliminado", null = False, blank = False)
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)
	
	def __unicode__(self):
		return self.nombre
		
	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "cueros"

class Textura(models.Model):
	idTextura = models.AutoField(primary_key = True)
	color = models.ForeignKey(Color, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "color")
	cuero = models.ForeignKey(Cuero, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "cuero")
	eliminada = models.BooleanField("eliminada", null = False, blank = False)
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)
	
	def __unicode__(self):
		return u"%s %s" % (self.color.__unicode__(), self.cuero.__unicode__())
		
	class Meta:
		ordering = ["color", "cuero"]
		verbose_name_plural = "texturas"
