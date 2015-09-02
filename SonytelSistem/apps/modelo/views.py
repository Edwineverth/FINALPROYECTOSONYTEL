from django.shortcuts import render
from apps.sistema.models import Modelo
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	


# Create your views here.
class crearModelo(CreateView):
	template_name='modelos/crear.html'
	model=Modelo
	success_url=reverse_lazy('sistema')

#LISTAR ARTICULOS
class listarModelo(ListView):
	template_name='modelos/filtrar.html'
	context_object_name='modelos'
	model=Modelo

#ACTUALIZAR ARTICULOS
class editarModelo(UpdateView):
	model = Modelo
	template_name= 'modelos/editar.html'
	success_url=reverse_lazy('sistema')

#ELIMINAR ARTICULOSs
class eliminarModelo(DeleteView):
	model = Modelo
	context_object_name="modelos"
	template_name = 'modelos/eliminar.html'
	success_url = reverse_lazy('sistema')

class filtrarAjaxModelo(TemplateView):
	def get(self,request,*args,**kwargs):
		nombreModelo = request.GET.get('nombre')
		modelador = Modelo.objects.filter(mod_nombre__icontains =nombreModelo)
		data = serializers.serialize('json',modelador,fields=('mod_nombre','mod_descripcion'))
		return HttpResponse(data,content_type='application/json')