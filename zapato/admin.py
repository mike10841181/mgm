from django.contrib import admin
from mgm.zapato.models import FamiliaDeModelo, Modelo, Suela, Talla, Categoria, Region

class FamiliaDeModeloAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'prefijo')
	
class ModeloAdmin(admin.ModelAdmin):
	list_display = ('categoria', 'precioBase', 'eliminada', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')
	list_filter = ('categoria', 'precioBase', 'eliminada', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')

class SuelaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion', 'eliminada', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')
	list_filter = ('fechaDeCreacion', 'fechaDeModificacion')
	
class TallaAdmin(admin.ModelAdmin):
	list_display = ('valor', 'eliminada', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')
	list_filter = ('valor','eliminada', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion', 'eliminada', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')
	list_filter = ('tallas','eliminada', 'fechaDeCreacion', 'fechaDeModificacion')
#eliminada,	
class RegionAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')
	list_filter = ('fechaDeCreacion', 'fechaDeModificacion')		

admin.site.register(FamiliaDeModelo, FamiliaDeModeloAdmin)
admin.site.register(Modelo)
admin.site.register(Suela, SuelaAdmin)
admin.site.register(Talla, TallaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Region, RegionAdmin)
