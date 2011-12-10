from django import forms
from mgm.zapato.models import Modelo
from mgm.textura.models import Color, Cuero

class ZapatoForm(forms.Form):
	def __init__(self, idModelo, *args, **kwargs):
		super(ZapatoForm, self).__init__(*args, **kwargs)

		modelo = Modelo.objects.get(pk=idModelo)
		
		tallas = modelo.categoria.tallas.all()
		TALLAS = []
		for t in tallas:
			TALLAS.append((t.idTalla, t.valor))
		
		suelas = modelo.familia.suelas.all()
		SUELAS = []
		for s in suelas:
			SUELAS.append((s.idSuela, s.nombre))
			
		COLORES = []
		for color in Color.objects.filter(eliminada__exact="0"):
			COLORES.append((color.idColor, color.nombre))
		
		CUEROS = []
		for cuero in Cuero.objects.filter(eliminada__exact="0"):
			CUEROS.append((cuero.idCuero, cuero.nombre))
			
		regiones = modelo.regiones.all()
		
		for r in regiones:
			self.fields['color_%s' % (r.idRegion)] = forms.ChoiceField(label="color de region %s" % (r.nombre), choices=COLORES)
			self.fields['cuero_%s' % (r.idRegion)] = forms.ChoiceField(label="cuero de region %s" % (r.nombre), choices=CUEROS)
		
		self.fields['suela'] = forms.ChoiceField(label="suela", choices=SUELAS)
		self.fields['talla'] = forms.ChoiceField(label="talla", choices=TALLAS)
		self.fields['pares'] = forms.IntegerField(label="pares", min_value=1, initial="1")
