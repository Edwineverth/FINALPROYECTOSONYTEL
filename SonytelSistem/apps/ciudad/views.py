from django.shortcuts import render
from apps.sistema.models import Ciudad
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	


# Create your views here.
class crearCuidad(CreateView):
	template_name='ciudad/crear.html'
	model=Ciudad
	success_url=reverse_lazy('home')

#LISTAR ARTICULOS
class listarCiudad(ListView):
	template_name='ciudad/editar.html'
	context_object_name='ciudades'
	model=Ciudad
#ACTUALIZAR ARTICULOS
class editarCiudad(UpdateView):
	model = Ciudad
	template_name= 'ciudad/editar.html'
	success_url=reverse_lazy('home')
#ELIMINAR ARTICULOS
class eliminarCiudad(DeleteView):
	model = Ciudad
	context_object_name="ciudades"
	template_name = 'ciudad/eliminar.html'
	success_url = reverse_lazy('home')

#FILTRADO DE CIUDAD *****
class filtrarCiudad(TemplateView):
	template_name='ciudad/filtrar.html'


#RETORNO AJAX FILTRADO *****
class filtrarAjaxciudad(TemplateView):
	def get(self,request,*args,**kwargs):
		nombreciudad = request.GET.get('nombre')
		ciudad = Ciudad.objects.filter(ciu_nombre__contains =nombreciudad)
		data = serializers.serialize('json',ciudad,fields=('ciu_nombre','ciu_descripcion'))
		return HttpResponse(data,content_type='application/json')
