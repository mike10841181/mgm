from django.contrib import admin
from mgm.cliente.models import Antiguedad, TipoDeCliente, Cliente

class AntiguedadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'eliminada', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')
    list_filter = ('eliminada', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')
    
class TipoDeClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'eliminada', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')
    list_filter = ('eliminada', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')

admin.site.register(Cliente)
admin.site.register(Antiguedad, AntiguedadAdmin)
admin.site.register(TipoDeCliente, TipoDeClienteAdmin)
