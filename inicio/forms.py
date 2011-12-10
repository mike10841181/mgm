from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
	nombreDeUsuario = forms.CharField(label="nombre de usuario", validators=[RegexValidator("^[a-z+A-Z+0-9+\+\-\@\_\.]")], max_length=30)
	contrasena = forms.CharField(label="contrasena", widget=forms.PasswordInput())
	
	def clean(self):
		data = self.cleaned_data
		
		if self._errors:
			return
			
		nombreDeUsuario = data["nombreDeUsuario"]
		contrasena = data["contrasena"]

		usuario = authenticate(username=nombreDeUsuario, password=contrasena)
		
		if usuario is None:
			raise forms.ValidationError("Nombre de usuario y/o contrasena incorrectos")
		else:
			if not usuario.is_active:
				raise forms.ValidationError("Su cuenta ha sido desactivada")

		return data
