from django.db import models
from mgm.zapato.models import Zapato, Region
from mgm.textura.models import Textura

# Create your models here.

class Detalle(models.Model):
	idDetalle = models.AutoField(primary_key = True)
	zapato = models.ForeignKey(Zapato, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "zapato")
	texturas = models.ManyToManyField(Textura, through = "RegionDeTextura", null = False, blank = False, verbose_name = "texturas")
	cantidad = models.IntegerField("cantidad", null = False, blank = False)
	eliminada = models.BooleanField("eliminado", null = False, blank = False)	
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)
	
	def __unicode__(self):
		return u"%s %s suela %s talla %s" & (self.cantidad, self.zapato.modelo.unicode(), self.zapato.suela.unicode(), self.zapato.talla.unicode())

	class Meta:
		ordering = ["zapato"]
		verbose_name_plural = "detalles"

class RegionDeTextura(models.Model):
	detalle = models.ForeignKey(Detalle, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "detalle")
	textura = models.ForeignKey(Textura, limit_choices_to = {"eliminada" : False}, null = False, blank = False, verbose_name = "textura")
	region = models.ForeignKey(Region, limit_choices_to = {"eliminada" :False}, null = False, blank = False, verbose_name = "region")
	
	def __unicode__(self):
		return self.region.nombre