from django.db import models

# Create your models here.
		
class Talla(models.Model):
	idTalla = models.AutoField(primary_key = True)
	valor = models.IntegerField("valor", null = False, blank = False, unique = True)
	eliminada = models.BooleanField("eliminada", null = False, blank = False)
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)
	
	def __unicode__(self):
		return u"%s" % self.valor
	
	class Meta:
		ordering = ["valor"]
		verbose_name_plural = "tallas"
		
class Categoria(models.Model):
	idCategoria = models.AutoField(primary_key = True)
	nombre = models.CharField("nombre de categoria", max_length = 30, null = False, blank = False, unique = True)
	descripcion = models.CharField("descripcion de categoria", max_length = 50, null = False, blank = False)
	tallas = models.ManyToManyField(Talla, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "tallas disponibles")
	eliminada = models.BooleanField("eliminada", null = False, blank = False)
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)
	
	def __unicode__(self):
		return self.nombre
		
	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "categorias"

class Suela(models.Model):
	idSuela = models.AutoField(primary_key = True)
	nombre = models.CharField("nombre de suela", max_length = 30, null = False, blank = False, unique = True)
	descripcion = models.CharField("descripcion de suela", max_length = 50, null = False, blank = False)
	eliminada = models.BooleanField("eliminada", null = False, blank = False)
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)
	
	def __unicode__(self):
		return self.nombre
		
	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "suelas"

class Region(models.Model):
	idRegion = models.AutoField(primary_key = True)
	nombre = models.CharField("nombre de region", max_length = 1, null = False, blank = False, unique = True)
	eliminada = models.BooleanField("eliminada", null = False, blank = False)
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)
	
	def __unicode__(self):
		return self.nombre
	
	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "regiones"

class FamiliaDeModelo(models.Model):
	idFamiliaDeModelo = models.AutoField(primary_key = True)
	nombre = models.CharField("nombre de familia", max_length = 30, null = False, blank = False, unique = True)
	prefijo = models.CharField("prefijo", max_length = 4, null = False, blank = False, unique = True)
	suelas = models.ManyToManyField(Suela, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "suelas disponibles")
	eliminada = models.BooleanField("eliminada", null = False, blank = False)
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)
	
	def __unicode__(self):
		return self.nombre
					
	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "familias de modelos"
		
class Modelo(models.Model):
	idModelo = models.AutoField(primary_key = True)
	categoria = models.ForeignKey(Categoria, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "categoria")
	familia = models.ForeignKey(FamiliaDeModelo, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "familia")
	precioBase = models.DecimalField("precio base", max_digits = 8, decimal_places = 2, null = False, blank = False)
	#precioBasePorMayor = models.DecimalField("precio base (por mayor)", max_digits = 8, decimal_places = 2, null = False, blank = False)
	regiones = models.ManyToManyField(Region, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "regiones del modelo")
	imagen = models.ImageField(upload_to = "imagenes/modelos")
	eliminada = models.BooleanField("eliminado", null = False, blank = False)
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)
	
	def __unicode__(self):
		return (u"MOD_%s_%s" % (self.familia.prefijo, self.idModelo))
	
	class Meta:
		ordering = ["categoria"]
		verbose_name_plural = "modelos"
		
class Zapato(models.Model):
	idZapato = models.AutoField(primary_key = True)
	modelo = models.ForeignKey(Modelo, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "modelo")
	suela = models.ForeignKey(Suela, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "suela")
	talla = models.ForeignKey(Talla, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "talla")
	eliminada = models.BooleanField("eliminado", null = False, blank = False)
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)

	def __unicode__(self):
		return u"Modelo %s con suela %s, talla %s" % (self.modelo.__unicode__(), self.suela.__unicode__(), self.talla.__unicode__())
		
	class Meta:
		ordering = ["modelo", "suela", "talla"]
		verbose_name_plural = "zapatos"
