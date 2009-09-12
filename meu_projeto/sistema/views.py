from django.http import HttpResponse
from django.utils import simplejson

from models import Empresa

def filtrar_empresas(request):
    lista = Empresa.objects.values('pk','nome')

    if 'filtro' in request.GET:
        lista = lista.filter(nome__icontains=request.GET['filtro'])

    lista = list(lista)

    json = simplejson.dumps(lista)
    return HttpResponse(json, mimetype="text/javascript")

