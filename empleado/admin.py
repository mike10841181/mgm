from django.contrib import admin
from mgm.empleado.models import AreaDepartamento, Empleado, TipoDeEmpleado

class AreaDepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'eliminada', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')
    list_filter = ('eliminada', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')

class TipoDeEmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion','areaDepartamento', 'eliminada', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')
    list_filter = ('eliminada', 'fechaDeCreacion', 'fechaDeModificacion', 'nombreDeUsuario')


admin.site.register(Empleado)
admin.site.register(AreaDepartamento,AreaDepartamentoAdmin)
admin.site.register(TipoDeEmpleado,TipoDeEmpleadoAdmin)
