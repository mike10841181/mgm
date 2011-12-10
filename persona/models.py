#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

class Persona(models.Model):
	idPersona = models.AutoField(primary_key = True)
	primerNombre = models.CharField("primer nombre", max_length = 30, null = False, blank = False, validators=[RegexValidator("^[a-zA-ZÒ—·¡È…ÌÕÛ”˙⁄]+$")], help_text="Solo se aceptan Letras y texto sin espacios")
	segundoNombre = models.CharField("segundo nombre", max_length = 30, null = False, blank = True, default = "N/A", validators=[RegexValidator("^[a-zA-ZÒ—·¡È…ÌÕÛ”˙⁄/]+$")], help_text="Solo se aceptan Letras y texto sin espacios")
	primerApellido = models.CharField("primer apellido", max_length = 30, null = False, blank = False, validators=[RegexValidator("^[a-zA-ZÒ—·¡È…ÌÕÛ”˙⁄]+$")], help_text="Solo se aceptan Letras y texto sin espacios")
	segundoApellido = models.CharField("segundo apellido",max_length = 30, null = False, blank = True, default = "N/A", validators=[RegexValidator("^[a-zA-ZÒ—·¡È…ÌÕÛ”˙⁄/]+$")], help_text="Solo se aceptan Letras y texto sin espacios")
	numeroDeIdentidad = models.CharField("numero de identidad", max_length = 15, null = False, blank = False, unique = True, validators=[RegexValidator("^[0-9]{4}-[0-9]{4}-[0-9]{5}$")], help_text="El formato de Identidad de ser: 0801-1988-15617")
	direccion = models.CharField("direccion", max_length = 100, null = False, blank = False, default = "N/A", help_text="Se aceptan todo tipo de caracteres")
	telefonoFijo = models.CharField("telefono fijo", max_length = 8, null = False, blank = False, default = "0", validators=[RegexValidator("^[0-9]{8}$")], help_text="El formato de numero Telefonico debe ser: 22454242")
	telefonoMovil = models.CharField("telefono movil", max_length = 8, null = False, blank = False, default = "0", validators=[RegexValidator("^[0-9]{8}$")], help_text="El formato de numero Movil debe ser: 97788215")
	correoElectronico = models.EmailField("correo electronico", max_length = 75, null = False, blank = False, help_text="El formato de correo electronico es alguien@compania.ext")
	imagen = models.ImageField(upload_to = "imagenes/personas")
	usuario = models.OneToOneField(User, null = False, blank = False, verbose_name = "usuario")
	eliminada = models.BooleanField("eliminada", null = False, blank = False)
	fechaDeCreacion = models.DateTimeField("fecha de creacion", auto_now_add = True)
	fechaDeModificacion = models.DateTimeField("fecha de modificacion", auto_now = True)
	nombreDeUsuario = models.CharField("usuario", max_length = 30, null = False, blank = False, editable = False)
	
	def __unicode__(self):
		return u"%s %s (%s)" % (self.primerNombre, self.primerApellido, self.usuario.username)
		
	class Meta:
		ordering = ['primerNombre', 'primerApellido']
		verbose_name_plural = "personas"
