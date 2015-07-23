from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ConsultarForm
from .models import *
# Create your views here.

def _queryset_filtrado(request):
	params = {}
	if request.session['sexo']:
		params['entrevistado__sexo'] = request.session['sexo']

	if request.session['organizacion']:
		params['org_responsable'] = request.session['organizacion']

	return Encuesta.objects.filter(**params)

def IndexView(request,template="index.html"):
	if request.method == 'POST':
		mensaje = None
		form = ConsultarForm(request.POST)
		if form.is_valid():
			request.session['sexo'] = form.cleaned_data['sexo']
			request.session['organizacion'] = form.cleaned_data['organizacion']
			mensaje = "Todas las variables estan correctamente :)"
			request.session['activo'] = True
			centinela = 1

			return redirect('/mapa/')

		else:
			centinela = 0   
		   
	else:
		form = ConsultarForm()
		mensaje = "Existen alguno errores"
		centinela = 0
		try:
			del request.session['sexo']
			del request.session['organizacion']
		except:
			pass

	return render(request, template, locals())

class MapaView(TemplateView):
    template_name = "mapa.html"

def principal_dashboard(request, template='dashboard.html', departamento_id=None):
	a = _queryset_filtrado(request)
	ahora = a.filter(entrevistado__departamento=departamento_id).distinct('entrevistado__id')
	depart = Departamento.objects.get(id=departamento_id)
	geolat = []
	geolong = []
	for obj in depart.municipio_set.all():
		geolat.append(obj.latitud)
		geolong.append(obj.longitud)
	
	latitud = geolat[-2]
	longitud = geolong[-2]

	return render(request,template,locals())

def detalle_finca(request, template='detalle_finca.html', entrevistado_id=None):
	detalle = Encuesta.objects.filter(entrevistado_id=entrevistado_id).order_by('year')

	return render(request, template, locals())