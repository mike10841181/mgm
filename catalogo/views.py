
from django.shortcuts import render_to_response
from django.template import RequestContext
from mgm.zapato.models import Modelo

def catalogo_main(request):
    return render_to_response('catalogo/catalogo_main.html', {"usuario" : request.user}, context_instance=RequestContext(request))

def catalogo_fancyDetalles(request, idDeModelo):
	modelo = Modelo.objects.get(pk__exact=idDeModelo)
	return render_to_response('catalogo/catalogo_fancyDetalles.html', {"usuario" : request.user, "modelo" : modelo}, context_instance=RequestContext(request))
