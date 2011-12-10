from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

@login_required
def produccion_main(request):
    return render_to_response('produccion/produccion_main.html', {"usuario" : request.user}, context_instance=RequestContext(request))
