# Create your views here.
from django.shortcuts						import render_to_response, redirect, get_object_or_404
from django.template.context				import RequestContext
from django.core.paginator					import Paginator, InvalidPage, EmptyPage
from django.http							import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers				import reverse
from django.core.exceptions					import ObjectDoesNotExist
from django.core							import serializers
from django.db								import transaction
from django.db.models						import Q, Count
from django.contrib.auth.models				import User, Group
from django.contrib.auth.decorators			import login_required
from django.utils							import simplejson
from django.template.defaultfilters			import date
import re, datetime, string, random, math

from mgm.zapato.models import Modelo, FamiliaDeModelo, Suela, Talla
from django.contrib.auth.models import User
from mgm.cliente.models import Cliente, TipoDeCliente, Antiguedad

def ajax_mgm(request):
	if request.is_ajax():
		pagina = request.GET['data']
		if pagina == 'catalogo_categoria':
			idCategoria = int(request.GET["id"])
			
			modelos = []
			
			if idCategoria == 1:
				modelos = Modelo.objects.filter(categoria__nombre__exact="Infantil")
			elif idCategoria == 2:
				modelos = Modelo.objects.filter(categoria__nombre__exact="Juvenil")
			else:
				modelos = Modelo.objects.filter(categoria__nombre__exact="Adulto")
			
			familias = FamiliaDeModelo.objects.all()
			
			return render_to_response('catalogo/catalogo_album.html', {"modelos" : modelos, "familias" : familias}, context_instance=RequestContext(request))
		elif pagina == "pedido_ingresar":
			idModelo = int(request.GET["id"])
			modelo = Modelo.objects.get(pk=idModelo)
			
			tallas = modelo.categoria.tallas.all()
			suelas = modelo.familia.suelas.all()
			regiones = modelo.regiones.all()
			
			data = []
			
			for t in tallas:
				data.append({"idTalla" : t.pk, "valor" : t.valor, "tipo" : "talla"})
			
			for s in suelas:
				data.append({"idSuela" : s.pk, "nombre" : s.nombre, "tipo" : "suela"})
				
			for r in regiones:
				data.append({"idRegion" : r.pk, "nombre" : r.nombre, "tipo" : "region"})
				
			return HttpResponse(simplejson.dumps(data), mimetype="application/json")
			
			'''codigo = ""
			
			for t in tallas:
				codigo += "<option value=%s>%s</option>" % (t.pk, t.valor)
			
			codigo += "::"
			
			for s in suelas:
				codigo += "<option value=%s>%s</option>" % (s.pk, s.nombre)
			
			
			codigo += "::"

			for r in regiones:
				codigo += r.nombre
			
			
			return HttpResponse(codigo)'''
		
