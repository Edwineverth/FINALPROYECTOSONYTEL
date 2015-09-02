from django.shortcuts import render
from apps.sistema.models import Categoria
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	


# Create your views here.
class crearCategoria(CreateView):
	template_name='categoria/crear.html'
	model=Categoria
	success_url=reverse_lazy('sistema')

#LISTAR ARTICULOS
class listarCategoria(ListView):
	template_name='categoria/filtrar.html'
	context_object_name='categorias'
	model=Categoria
#ACTUALIZAR ARTICULOS
class editarCategoria(UpdateView):
	model = Categoria
	template_name= 'categoria/editar.html'
	success_url=reverse_lazy('sistema')
#ELIMINAR ARTICULOS
class eliminarCategoria(DeleteView):
	model = Categoria
	context_object_name="categorias"
	template_name = 'categoria/eliminar.html'
	success_url = reverse_lazy('sistema')

#FILTRADO DE Categoria *****
class filtrarCategoria(TemplateView):
	template_name='categoria/filtrar.html'


#RETORNO AJAX FILTRADO *****
class filtrarAjaxCategoria(TemplateView):
	def get(self,request,*args,**kwargs):
		nombreCategoria = request.GET.get('nombre')
		categoria = Categoria.objects.filter(mar_nombre__contains =nombreCategoria)
		data = serializers.serialize('json',categoria,fields=('mar_nombre','mar_descripcion'))
		return HttpResponse(data,content_type='application/json')