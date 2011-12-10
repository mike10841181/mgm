# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import simplejson
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from mgm.inicio.forms import LoginForm

def inicio(request):
	return render_to_response('inicio/inicio.html', {"usuario" : request.user}, context_instance=RequestContext(request))

def iniciarSesion(request):
	if request.method == 'POST': # If the form has been submitted...
		lf = LoginForm(request.POST)
		
		if lf.is_valid(): # All validation rules pass
			nombreDeUsuario = lf.cleaned_data["nombreDeUsuario"]
			contrasena = lf.cleaned_data["contrasena"]
			
			usuario = authenticate(username=nombreDeUsuario, password=contrasena)
			login(request, usuario)

			'''if request.GET.get('next'):
				return HttpRequest.build_absolute_uri(location)
			else:'''			
			return HttpResponseRedirect('/') # Redirect after POST
	else:	
		lf = LoginForm() # An unbound form
		
	return render_to_response('inicio/login.html', {"usuario" : request.user, "lf" : lf}, context_instance=RequestContext(request))

def finalizarSesion(request):
	logout(request)
	return HttpResponseRedirect('/login/')
