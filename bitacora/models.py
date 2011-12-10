from django.db import models

# Create your models here.
	
class Bitacora(models.Model):
	tabla = models.CharField("tabla", max_length = 50, null = False, blank = False)
	idFila = models.IntegerField("id fila", null = False, blank = False)
	columna = models.CharField("columna", max_length = 50, null = False, blank = False)
	accion = models.CharField("accion", max_length = 6, null = False, blank = False)
	valorAnterior = models.CharField("valor anterior", max_length = 50, null = True, blank = True)
	valorNuevo = models.CharField("valor nuevo", max_length = 50, null = True, blank = True)
	fecha = models.DateTimeField("fecha", auto_now_add = True)
	usuario = models.CharField("usuario", max_length = 30, null = False, blank = False)

