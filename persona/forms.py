from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from mgm.persona.models import Persona

class DatosPersonalesForm(ModelForm):
	class Meta:
		model = Persona
		exclude = ("usuario", "eliminada", "fechaDeCreacion", "fechaDeModificacion", "nombreDeUsuario")


class DatosDeUsuarioForm(forms.Form):
	nombreDeUsuario = forms.CharField(label= "Nombre de usuario", validators=[RegexValidator("^[(a-z)+(A-Z)+(0-9)+\+\-\@\_\.]")], help_text="Requerido 30 caracteres o menos. Letras, Digitos y @/./+/-/_ solamente.",max_length= 30, )
	contrasena = forms.CharField(label="Contrasena", widget=forms.PasswordInput())
	contrasena2 = forms.CharField(label="Vuelva a ingresar contrasena",widget=forms.PasswordInput())
	
	def clean(self):
		cleaned_data = self.cleaned_data
		
		if self._errors:
			return
		
		if cleaned_data["contrasena"] != cleaned_data["contrasena2"]:
			raise forms.ValidationError("Las contrasenas ingresadas son distintas")
		
		matchUsername = User.objects.filter(username__exact=cleaned_data["nombreDeUsuario"])
		
		if matchUsername:
			raise forms.ValidationError("Ya existe un cliente con este numero de identidad!")

		return cleaned_data
