from django.conf.urls.defaults import patterns, include, url
from django.views.static import *
from django.conf import settings

from mgm.zapato.views import modeloGuardado, modeloimg
from mgm.inicio.views import inicio, iniciarSesion, finalizarSesion
from mgm.catalogo.views import catalogo_main, catalogo_fancyDetalles
from mgm.cliente.views import cliente_main, cliente_activarDesactivar, cliente_modificar_main, cliente_modificar, cliente_inscripcion, cliente_nuevo, cliente_fancyPerfil, cliente_despuesDeAutoRegistro
from mgm.cotizacion.views import cotizacion_main
from mgm.empleado.views import empleado_main, empleado_activarDesactivar, empleado_modificar_main, empleado_modificar, empleado_nuevo, empleado_fancyPerfil
from mgm.pedido.views import pedido_main, pedido_ingresar, pedido_eliminar, pedido_solicitados#, pedido_modificar
from mgm.produccion.views import produccion_main


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mgm.views.home', name='home'),
    # url(r'^mgm/', include('mgm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', inicio),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^ajax/', include('ajax.urls')),
    url(r'^modeloguardado/', modeloGuardado),
    url(r'^modeloimg/', modeloimg),
    url(r'^catalogo/$', catalogo_main),
    url(r'^catalogo/catalogo_fancyDetalles/(\d+)/$', catalogo_fancyDetalles),
    url(r'^clientes/$', cliente_main),
    url(r'^clientes/activarDesactivar/$', cliente_activarDesactivar),
    url(r'^clientes/nuevo/$', cliente_nuevo),
    url(r'^clientes/modificar/$', cliente_modificar_main),
    url(r'^clientes/modificar/(.*)$', cliente_modificar),
    url(r'^clientes/cliente_fancyPerfil/(.*)$', cliente_fancyPerfil),
	url(r'^clientes/registroExitoso/$', cliente_despuesDeAutoRegistro),
    url(r'^empleados/$', empleado_main),
    url(r'^empleados/activarDesactivar/$', empleado_activarDesactivar),
    url(r'^empleados/empleado_fancyPerfil/(.*)$', empleado_fancyPerfil),
    url(r'^empleados/nuevo/$', empleado_nuevo),
    url(r'^empleados/modificar/$', empleado_modificar_main),
    url(r'^empleados/modificar/(.*)$', empleado_modificar),
    url(r'^inscripcion/', cliente_inscripcion),
    url(r'^cotizaciones/', cotizacion_main),
    url(r'^login/', iniciarSesion),
    url(r'^logout/', finalizarSesion),
    #url(r'^empleados/$', empleado_main),
    #url(r'^empleados/nuevoEmpleado/', empleado_nuevoEmpleado),
    url(r'^pedidos/$', pedido_main),
    url(r'^pedidos/ingresar/$', pedido_ingresar),
    #url(r'^pedidos/modificar/$', pedido_modificar),
    url(r'^pedidos/eliminar/$', pedido_eliminar),
    url(r'^pedidos/solicitados/$', pedido_solicitados),
    #url(r'^pedido/modelo/(\d)$', pedido_prueba),
    url(r'^produccion/', produccion_main),
    
    url(r'^medios/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
