from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from mgm.cliente.models import Cliente
from mgm.persona.models import Persona

class EmpleadoModificaClienteForm(ModelForm):
	segundoNombre = forms.CharField(label="Segundo Nombre", max_length=30, initial = "N/A", help_text="fdsafdsafdafdsa")
	class Meta:
		model = Cliente
		exclude = ("usuario", "eliminada", "fechaDeCreacion", "fechaDeModificacin", "nombreDeUsuario")
		
class ClienteModificaPerfilForm(ModelForm):
	class Meta:
		model = Cliente
		exclude = ("tipoDeCliente", "antiguedad", "usuario", "eliminada", "fechaDeCreacion", "fechaDeModificacin", "nombreDeUsuario")
		
class NuevoClienteForm(forms.Form):
    #INVESTIGAR REGEX PARA PRIMER NOMBRE
    primerNombre = forms.CharField(label="Primer Nombre", max_length=30,validators=[RegexValidator("^[a-zA-Z]")])
    segundoNombre = forms.CharField(label="Segundo Nombre", max_length=30, initial = "N/A") 
    primerApellido = forms.CharField(label="Primer Apellido", max_length=30)
    segundoApellido = forms.CharField(label="Segundo Apellido",max_length = 30, initial = "N/A")
    numeroDeIdentidad = forms.CharField(label="Numero De Identidad", max_length = 15)
    direccion = forms.CharField(label="Direccion", max_length = 100)
    telefonoFijo = forms.CharField(label="Telefono Fijo", max_length = 8, initial = "N/A")
    telefonoMovil = forms.CharField(label="Telefono Movil", max_length = 8, initial = "N/A")
    
    imagen = forms.ImageField(label="Foto")
    
    email = forms.EmailField(label="Correo Electronico",max_length =75)
    nombreDeUsuario = forms.CharField(label = "Usuario:", max_length =30)
    
    contrasena = forms.CharField(label="contrasenia", widget=forms.PasswordInput())
    contrasena2 = forms.CharField(label="confirme contrasenia",widget=forms.PasswordInput())
    
    def clean(self):
        cleaned_data = self.cleaned_data
        
        if self._errors:
			return
			
        matchIdentidad = Persona.objects.filter(numeroDeIdentidad__exact=cleaned_data["numeroDeIdentidad"])
        matchUsername = User.objects.filter(username__exact=cleaned_data["nombreDeUsuario"])
        
        if matchIdentidad:
        	raise forms.ValidationError("Ya existe un cliente con este numero de identidad!")
        
        if matchUsername:
  	    	raise forms.ValidationError("El nombre de usuario no esta disponible!")
    	
    	return cleaned_data
