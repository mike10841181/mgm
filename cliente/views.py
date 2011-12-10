from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.db.models import Q
from mgm.cliente.models import Cliente, TipoDeCliente, Antiguedad
from mgm.defaults.models import ValoresPorDefecto
from mgm.cliente.forms import EmpleadoModificaClienteForm
from mgm.persona.forms import DatosPersonalesForm, DatosDeUsuarioForm

def cliente_main(request):
	if request.user.is_staff:
		clientes = Cliente.objects.filter(eliminada__exact="0")
		tipos = TipoDeCliente.objects.filter(eliminada__exact="0")
		
		print clientes
		
		return render_to_response('cliente/cliente_main.html', {"usuario" : request.user, "clientes" : clientes, "tipos" : tipos}, context_instance=RequestContext(request))
	else:
		return render_to_response('accesoDenegado.html', {"usuario" : request.user}, context_instance=RequestContext(request))

def cliente_activarDesactivar(request):
	if request.user.is_staff:
		if request.user.has_perm('cliente.delete_cliente'):
			clientes = Cliente.objects.all()
			tipos = TipoDeCliente.objects.filter(eliminada__exact="0")
			
			if request.method == 'POST':
				var = request.POST.getlist("listadoIdDeClientes")
				clientesSeleccionados = Cliente.objects.filter(pk__in=var)
				
				for c in clientesSeleccionados:
					c.eliminada = not c.eliminada
					c.save()
					
			return render_to_response('cliente/cliente_activarDesactivar.html', {"usuario" : request.user, "clientes" : clientes, "tipos" : tipos}, context_instance=RequestContext(request))
	return render_to_response('accesoDenegado.html', {"usuario" : request.user}, context_instance=RequestContext(request))
			
def cliente_modificar_main(request):
	if request.user.is_staff:
		if request.user.has_perm('cliente.change_cliente'):
			clientes = Cliente.objects.filter(eliminada__exact="0")
			tipos = TipoDeCliente.objects.filter(eliminada__exact="0")
			
			return render_to_response('cliente/cliente_modificar_main.html', {"usuario" : request.user, "clientes" : clientes, "tipos" : tipos}, context_instance=RequestContext(request))
	
	return render_to_response('accesoDenegado.html', {"usuario" : request.user}, context_instance=RequestContext(request))
	
def cliente_modificar(request, nombreDeUsuario):
	if request.user.is_staff:
		if request.user.has_perm('cliente.change_cliente'):		
			c = Cliente.objects.get(usuario__username__exact=nombreDeUsuario)
			
			if request.method == 'POST':
				f = EmpleadoModificaClienteForm(request.POST, request.FILES, instance = c)
				
				if f.is_valid():
					c = f.save(commit = False)
					c.save()
					return HttpResponseRedirect("/clientes/")
			else:				
				f = EmpleadoModificaClienteForm(instance=c)
				
			return render_to_response('cliente/cliente_modificar.html', {"usuario" : request.user, "f" : f}, context_instance=RequestContext(request))
			
	return render_to_response('accesoDenegado.html', {"usuario" : request.user}, context_instance=RequestContext(request))
	
def cliente_fancyPerfil(request, nombreDeUsuario):
		cliente = Cliente.objects.get(usuario__username__exact=nombreDeUsuario)
		return render_to_response('cliente/cliente_fancyPerfil.html', {"usuario" : request.user, "cliente" : cliente}, context_instance=RequestContext(request))
	
def cliente_inscripcion(request):
	if request.method == 'POST':
		datosPersonalesForm = DatosPersonalesForm(request.POST, request.FILES)
		datosDeUsuarioForm = DatosDeUsuarioForm(request.POST)
		
		if datosPersonalesForm.is_valid() and datosDeUsuarioForm.is_valid():
			nombreDeUsuario = datosDeUsuarioForm.cleaned_data["nombreDeUsuario"]
			contrasena = datosDeUsuarioForm.cleaned_data["contrasena"]
			
			usuarioNuevo = User.objects.create_user(nombreDeUsuario, "", contrasena)
			usuarioNuevo.is_staff = False
			usuarioNuevo.is_active = False
			usuarioNuevo.save()
			
			clienteNuevo = Cliente()
			clienteNuevo.primerNombre = datosPersonalesForm.cleaned_data['primerNombre']
			clienteNuevo.segundoNombre = datosPersonalesForm.cleaned_data['segundoNombre']
			clienteNuevo.primerApellido = datosPersonalesForm.cleaned_data['primerApellido']
			clienteNuevo.segundoApellido = datosPersonalesForm.cleaned_data['segundoApellido']
			clienteNuevo.numeroDeIdentidad = datosPersonalesForm.cleaned_data['numeroDeIdentidad']
			clienteNuevo.direccion = datosPersonalesForm.cleaned_data['direccion']
			clienteNuevo.telefonoFijo= datosPersonalesForm.cleaned_data['telefonoFijo']
			clienteNuevo.telefonoMovil= datosPersonalesForm.cleaned_data['telefonoMovil']
			clienteNuevo.correoElectronico = datosPersonalesForm.cleaned_data["correoElectronico"]
			clienteNuevo.imagen = datosPersonalesForm.cleaned_data['imagen']
			clienteNuevo.usuario = usuarioNuevo
			clienteNuevo.tipoDeCliente = ValoresPorDefecto.objects.get(pk=1).tipoDeCliente
			clienteNuevo.antiguedad = ValoresPorDefecto.objects.get(pk=1).antiguedad
			clienteNuevo.eliminada = 1
			clienteNuevo.save()
			
			return HttpResponseRedirect('/clientes/registroExitoso/')
	else:
		datosPersonalesForm = DatosPersonalesForm()
		datosDeUsuarioForm = DatosDeUsuarioForm()
		
	return render_to_response('cliente/cliente_inscripcion.html', {"datosPersonalesForm" : datosPersonalesForm, "datosDeUsuarioForm" : datosDeUsuarioForm}, context_instance=RequestContext(request))

def cliente_nuevo(request):
	if request.user.is_staff:
		if request.user.has_perm('cliente.add_cliente'):
			if request.method == 'POST':
				c = EmpleadoModificaClienteForm(request.POST, request.FILES)
				u = DatosDeUsuarioForm(request.POST)
				
				if c.is_valid() and u.is_valid():
					nombreDeUsuario = u.cleaned_data["nombreDeUsuario"]
					contrasena = u.cleaned_data["contrasena"]
					
					usuarioNuevo = User.objects.create_user(nombreDeUsuario, "", contrasena)
					usuarioNuevo.is_staff = False
					usuarioNuevo.save()
					
					clienteNuevo = Cliente()
					clienteNuevo.primerNombre = c.cleaned_data['primerNombre']
					clienteNuevo.segundoNombre = c.cleaned_data['segundoNombre']
					clienteNuevo.primerApellido = c.cleaned_data['primerApellido']
					clienteNuevo.segundoApellido = c.cleaned_data['segundoApellido']
					clienteNuevo.numeroDeIdentidad = c.cleaned_data['numeroDeIdentidad']
					clienteNuevo.direccion = c.cleaned_data['direccion']
					clienteNuevo.telefonoFijo= c.cleaned_data['telefonoFijo']
					clienteNuevo.telefonoMovil= c.cleaned_data['telefonoMovil']
					clienteNuevo.correoElectronico = c.cleaned_data["correoElectronico"]
					clienteNuevo.imagen = c.cleaned_data['imagen']
					clienteNuevo.usuario = usuarioNuevo
					clienteNuevo.tipoDeCliente = c.cleaned_data['tipoDeCliente']
					clienteNuevo.antiguedad = c.cleaned_data['antiguedad']
					clienteNuevo.save()
					
					return HttpResponseRedirect('/clientes/')
			else:
				c = EmpleadoModificaClienteForm()
				u = DatosDeUsuarioForm()
			
			agregarTipos = request.user.has_perm("cliente.add_tipodecliente")
			agregarAntiguedades = request.user.has_perm("cliente.add_antiguedad")
			
			return render_to_response('cliente/cliente_nuevo.html', {"usuario" : request.user, "c" : c, "u" : u, "agregarTipos" : agregarTipos, "agregarAntiguedades" : agregarAntiguedades}, context_instance=RequestContext(request))
			
	return render_to_response('accesoDenegado.html', {"usuario" : request.user}, context_instance=RequestContext(request))
	
def cliente_despuesDeAutoRegistro(request):
		return render_to_response('cliente/mensajeAutoRegistro.html', context_instance=RequestContext(request))
