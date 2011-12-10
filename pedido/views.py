from decimal import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from mgm.zapato.models import Categoria, Modelo, Talla, Suela, Zapato
from mgm.textura.models import Color, Cuero, Textura
from mgm.detalle.models import RegionDeTextura
from mgm.pedido.models import Pedido, EstadoDePedido, DetalleDePedido
from mgm.defaults.models import ValoresPorDefecto
from mgm.cliente.models import Cliente
from mgm.empleado.models import Empleado

@login_required
def pedido_main(request):
	if not request.user.is_staff:
		cliente = Cliente.objects.get(pk = request.user.persona.pk)
		pedidos = Pedido.objects.filter(eliminada__exact = "0", cliente__exact = cliente)
	else:
		pedidos = Pedido.objects.filter(eliminada__exact = "0")
	
	return render_to_response('pedido/pedido_main.html', {"usuario" : request.user, "pedidos" : pedidos}, context_instance=RequestContext(request))

@login_required
def pedido_ingresar(request):
	if request.user.has_perm('pedido.add_pedido'):
		if request.method == 'GET':
			colores = Color.objects.filter(eliminada__exact="0")
			cueros = Cuero.objects.filter(eliminada__exact="0")
			categorias = Categoria.objects.filter(eliminada__exact="0")
			modelos = []
			
			for c in categorias:
				modelosDeC = Modelo.objects.filter(categoria__exact=c)
				modelos.append(modelosDeC)
			
			idCliente= -1
			if not request.user.is_staff:
				idCliente=request.user.persona.pk
				
			return render_to_response('pedido/pedido_ingresar.html', {"usuario" : request.user, "modelos" : modelos, "colores" : colores, "cueros" : cueros, "idCliente" : idCliente}, context_instance=RequestContext(request))
		elif request.method == 'POST':
			idCliente = int(request.POST.get("idCliente"))
			idModelos = request.POST.getlist("modelos")
			idTallas = request.POST.getlist("tallas")
			idSuelas = request.POST.getlist("suelas")
			cantidades = request.POST.getlist("cantidades")
			descripciones = request.POST.getlist("descripciones")
				
			i = 0
			
			cliente = Cliente.objects.get(pk=idCliente)
			estado = ValoresPorDefecto.objects.get(pk=1).estadoDePedido
			
			nuevoPedido = Pedido()
			nuevoPedido.estado = estado
			nuevoPedido.cliente = cliente
			
			if request.user.is_staff:
				nuevoPedido.vendedor = Empleado.objects.get(pk = request.user.persona.pk)
			nuevoPedido.save()
			
			for idM in idModelos:
				modelo = Modelo.objects.get(pk=idM)
				talla = Talla.objects.get(pk=idTallas[i])
				suela = Suela.objects.get(pk=idSuelas[i])
				cantidad = int(cantidades[i])
				descripcion = descripciones[i]
				
				zapato = Zapato.objects.filter(modelo__exact=modelo, talla__exact=talla, suela__exact=suela)
				
				if zapato:
					zapato = zapato[0]
				else:
					zapato = Zapato()
					zapato.modelo = modelo
					zapato.suela = suela
					zapato.talla = talla
					zapato.eliminada = 0
					zapato.save()
				
				detalleDePedido = DetalleDePedido()
				
				detalleDePedido.pedido = nuevoPedido
				detalleDePedido.zapato = zapato
				detalleDePedido.cantidad = cantidad
				detalleDePedido.descripcion = descripcion
				detalleDePedido.precioUnitario = modelo.precioBase
				detalleDePedido.subTotal = detalleDePedido.cantidad * detalleDePedido.precioUnitario
				print "subtot de detalle: %s" % (detalleDePedido.subTotal)
				detalleDePedido.isv = detalleDePedido.subTotal * Decimal(str(0.12))
				detalleDePedido.total = detalleDePedido.subTotal + detalleDePedido.isv
				detalleDePedido.save()
				
				texturas = []
				for r in modelo.regiones.all():
					texturas = [request.POST.getlist("textura_%s_%s" % (r.pk, i+1))]
					
					for t in texturas:
						color = Color.objects.get(pk=t[0])
						cuero = Cuero.objects.get(pk=t[1])
						
						textura = Textura.objects.filter(color__exact=color, cuero__exact=cuero)
						
						if textura:
							print u"textura %s" % ("ya existia")
							textura = textura[0]
						else:
							textura = Textura()
							textura.color = color
							textura.cuero = cuero
							textura.eliminada = 0
							textura.save()
							print u"textura %s" % ("no existia y fue creada")
						
						RegionDeTextura.objects.create(detalle=detalleDePedido, textura=textura, region=r)
				
					
				detalleDePedido.save()
					
				i += 1
			
			for d in nuevoPedido.detalledepedido_set.all():
				nuevoPedido.subTotal += d.subTotal
			
			print "subTot pedido: %s" % (nuevoPedido.subTotal)
			print "desc por tipo: %s" % (cliente.tipoDeCliente.porcentajeDescuento)
			nuevoPedido.descuento = nuevoPedido.subTotal * (cliente.tipoDeCliente.porcentajeDescuento/Decimal(str(100.0)) + cliente.antiguedad.porcentajeDescuento/Decimal(str(100.0)))
			print "subTot desc: %s" % (nuevoPedido.descuento)
			nuevoPedido.isv = (nuevoPedido.subTotal - nuevoPedido.descuento) * Decimal(str(0.12))
			print "subTot isv: %s" % (nuevoPedido.isv)
			nuevoPedido.total = nuevoPedido.subTotal - nuevoPedido.descuento + nuevoPedido.isv
			print "subTot tot: %s" % (nuevoPedido.total)
			
			nuevoPedido.save()
			
			return HttpResponseRedirect('/pedidos/ingresar')
	return render_to_response('accesoDenegado.html', {"usuario" : request.user}, context_instance=RequestContext(request))

@login_required
def pedido_solicitados(request):
	if request.user.is_staff:
		if request.user.has_perm('pedido.change_pedido'):
			defaultEstado = ValoresPorDefecto.objects.get(pk=1).estadoDePedido
			pedidos = Pedido.objects.filter(estado__exact=defaultEstado)

			if request.method == 'POST':
				estado = EstadoDePedido.objects.get(pk=int(request.POST.get("accion")))
				pedidos = Pedido.objects.filter(pk__in=(request.POST.getlist("listadoIdDePedidos")))
				
				for p in pedidos:
					p.estado = estado
					p.save()
				
				return HttpResponseRedirect('/pedidos/')
			else:
				estados = EstadoDePedido.objects.exclude(pk=(ValoresPorDefecto.objects.get(pk=1).estadoDePedido.pk))
				return render_to_response('pedido/pedido_solicitados.html', {"usuario" : request.user, "pedidos" : pedidos, "estados": estados}, context_instance=RequestContext(request))		
	
	return render_to_response('accesoDenegado.html', {"usuario" : request.user}, context_instance=RequestContext(request))
	
@login_required
def pedido_eliminar(request):
	if request.user.is_staff:
		if request.user.has_perm('pedido.delete_pedido'):
			pedidos = Pedido.objects.filter(eliminada__exact="0")
			
			return render_to_response('pedido/pedido_eliminar.html', {"usuario" : request.user, "pedidos" : pedidos}, context_instance=RequestContext(request))
	return render_to_response('accesoDenegado.html', {"usuario" : request.user}, context_instance=RequestContext(request))
