from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.db.models import Q
from mgm.empleado.models import Empleado, TipoDeEmpleado
from mgm.empleado.forms import DatosDeEmpleadoForm
from mgm.persona.forms import DatosDeUsuarioForm

@login_required
def empleado_main(request):
	if request.user.is_staff:
		empleados = Empleado.objects.filter(eliminada__exact="0")
		tipos = TipoDeEmpleado.objects.filter(eliminada__exact="0")
	
		return render_to_response('empleado/empleado_main.html', {"usuario" : request.user, "empleados" : empleados, "tipos" : tipos}, context_instance=RequestContext(request))
	else:
		return render_to_response('accesoDenegado.html', {"usuario" : request.user}, context_instance=RequestContext(request))
		
@login_required
def empleado_activarDesactivar(request):
	if request.user.is_staff:
		if request.user.has_perm('empleado.delete_empleado'):
			empleados = Empleado.objects.all()
			tipos = TipoDeEmpleado.objects.filter(eliminada__exact="0")
			
			if request.method == 'POST':
				var = request.POST.getlist("listadoIdDeEmpleados")
				empleadosSeleccionados = Empleado.objects.filter(pk__in=var)
				
				for e in empleadosSeleccionados:
					e.eliminada = not e.eliminada
					e.save()
				
			return render_to_response('empleado/empleado_activarDesactivar.html', {"usuario" : request.user, "empleados" : empleados, "tipos" : tipos}, context_instance=RequestContext(request))
	return render_to_response('accesoDenegado.html', {"usuario" : request.user}, context_instance=RequestContext(request))

@login_required
def empleado_modificar_main(request):
	if request.user.is_staff:
		if request.user.has_perm('empleado.change_empleado'):	
			empleados = Empleado.objects.filter(eliminada__exact="0")
			tipos = TipoDeEmpleado.objects.filter(eliminada__exact="0")
			
			return render_to_response('empleado/empleado_modificar_main.html', {"usuario" : request.user, "empleados" : empleados, "tipos" : tipos}, context_instance=RequestContext(request))
	return render_to_response('accesoDenegado.html', {"usuario" : request.user}, context_instance=RequestContext(request))

@login_required
def empleado_modificar(request, nombreDeUsuario):
	if request.user.is_staff:
		if request.user.has_perm('empleado.change_empleado'):
			e = Empleado.objects.get(usuario__username__exact=nombreDeUsuario)
			
			if request.method == 'POST':
				f = DatosDeEmpleadoForm(request.POST, request.FILES, instance = e)
				
				if f.is_valid():
					e = f.save(commit = False)
					e.save()
					return HttpResponseRedirect("/empleados/")
			else:				
				f = DatosDeEmpleadoForm(instance = e)
				
			return render_to_response('empleado/empleado_modificar.html', {"usuario" : request.user, "f" : f}, context_instance=RequestContext(request))
	return render_to_response('accesoDenegado.html', {"usuario" : request.user}, context_instance=RequestContext(request))

	
def empleado_fancyPerfil(request, nombreDeUsuario):
		empleado = Empleado.objects.get(usuario__username__exact=nombreDeUsuario)
		return render_to_response('empleado/empleado_fancyPerfil.html', {"usuario" : request.user, "empleado" : empleado}, context_instance=RequestContext(request))

@login_required
def empleado_nuevo(request):
	if request.user.is_staff:
		if request.user.has_perm('empleado.add_empleado'):
			if request.method == 'POST':
				e = DatosDeEmpleadoForm(request.POST, request.FILES)
				u = DatosDeUsuarioForm(request.POST)
				
				if e.is_valid() and u.is_valid():
					nombreDeUsuario = u.cleaned_data["nombreDeUsuario"]
					contrasena = u.cleaned_data["contrasena"]
					
					usuarioNuevo = User.objects.create_user(nombreDeUsuario, "", contrasena)
					usuarioNuevo.is_staff = True
					usuarioNuevo.save()
					
					empleadoNuevo = Empleado()
					empleadoNuevo.primerNombre = e.cleaned_data['primerNombre']
					empleadoNuevo.segundoNombre = e.cleaned_data['segundoNombre']
					empleadoNuevo.primerApellido = e.cleaned_data['primerApellido']
					empleadoNuevo.segundoApellido = e.cleaned_data['segundoApellido']
					empleadoNuevo.numeroDeIdentidad = e.cleaned_data['numeroDeIdentidad']
					empleadoNuevo.direccion = e.cleaned_data['direccion']
					empleadoNuevo.telefonoFijo= e.cleaned_data['telefonoFijo']
					empleadoNuevo.telefonoMovil= e.cleaned_data['telefonoMovil']
					empleadoNuevo.correoElectronico = e.cleaned_data["correoElectronico"]
					empleadoNuevo.imagen = e.cleaned_data['imagen']
					empleadoNuevo.usuario = usuarioNuevo
					empleadoNuevo.tipoDeEmpleado = e.cleaned_data['tipoDeEmpleado']
					empleadoNuevo.save()
					
					return HttpResponseRedirect('/empleados/')
			else:
				e = DatosDeEmpleadoForm()
				u = DatosDeUsuarioForm()
					
			return render_to_response('empleado/empleado_nuevo.html', {"usuario" : request.user, "e" : e, "u" : u}, context_instance=RequestContext(request))
	return render_to_response('accesoDenegado.html', {"usuario" : request.user}, context_instance=RequestContext(request))

def empleado_nuevoEmpleado(request):
    if request.method== 'POST':
        nef=NuevoEmpleadoForm(request.POST, request.FILES)
        if nef.is_valid():
            nombreDeUsuario= nef.cleaned_data["nombreDeUsuario"]
            email= nef.cleaned_data["email"]
            contrasena=nef.cleaned_data["contrasena"]
            
            usuarioNuevo= User.objects.create_user(nombreDeUsuario, email, contrasena)
            usuarioNuevo.is_staff = True
            usuarioNuevo.save()
            
            empleadoNuevo= Empleado()
            empleadoNuevo.primerNombre = nef.cleaned_data['primerNombre']
            empleadoNuevo.segundoNombre = nef.cleaned_data['segundoNombre']
            empleadoNuevo.primerApellido = nef.cleaned_data['primerApellido']
            empleadoNuevo.segundoApellido = nef.cleaned_data['segundoApellido']
            empleadoNuevo.numeroDeIdentidad= nef.cleaned_data['numeroDeIdentidad']
            empleadoNuevo.direccion = nef.cleaned_data['direccion']
            empleadoNuevo.telefonoFijo= nef.cleaned_data['telefonoFijo']
            empleadoNuevo.telefonoMovil= nef.cleaned_data['telefonoMovil']
            empleadoNuevo.imagen =nef.cleaned_data['imagen']
            empleadoNuevo.usuario = usuarioNuevo
            empleadoNuevo.tipoDeEmpleado = TipoDeEmpleado.objects.get(pk=1)
            empleadoNuevo.save()
            
            
            return HttpResponseRedirect('/')
    else:
        nef=NuevoEmpleadoForm()
        
    return render_to_response('empleado/empleado_nuevoEmpleado.html', {"usuario" : request.user,"nef":nef}, context_instance=RequestContext(request) )
