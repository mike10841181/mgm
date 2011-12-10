from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from mgm.zapato.models import Modelo

# Create your views here.


def modeloGuardado(request):
	return render_to_response('modeloGuardado.html')

def modeloimg(request):
	modelos = Modelo.objects.all()
	return render_to_response('zapato/zapato_modeloimg.html', {'modelos': modelos}, context_instance=RequestContext(request))
