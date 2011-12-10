from django.contrib import admin
from mgm.pedido.models import EstadoDePedido

class EstadoDePedidoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'eliminada', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')
    list_filter = ('eliminada', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')

admin.site.register(EstadoDePedido, EstadoDePedidoAdmin)
