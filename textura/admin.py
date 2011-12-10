from django.contrib import admin
from mgm.textura.models import Color, Cuero


class ColorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'eliminada', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')
    list_filter = ('eliminada', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')

class CueroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'eliminada', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')
    list_filter = ('eliminada', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')

admin.site.register(Color, ColorAdmin)
admin.site.register(Cuero, CueroAdmin)