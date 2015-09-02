from django.shortcuts import render
from apps.sistema.models import Articulossegunda,Categoria,Modelo
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import Q

from django.contrib.auth.decorators import login_required
# Create your views here.



class crearArticulo(CreateView):
	template_name='articulos/reportar.html'
	model=Articulossegunda
	success_url=reverse_lazy('sistema')

#LISTAR ARTICULOSs
#@login_required
class listarArticulos(ListView):
	template_name='articulos/listar.html'
	context_object_name='articulos'
	model=Articulossegunda
	def get_context_data(self, **kwargs):
		ctx = super(listarArticulos, self).get_context_data(**kwargs)
		ctx['categorias'] = Categoria.objects.all()
		ctx['modelos'] = Modelo.objects.all()
		return ctx
#ACTUALIZAR ARTICULOS
#@login_required
class editarArticulo(UpdateView):
	model = Articulossegunda
	template_name= 'articulos/actualizar.html'
	success_url=reverse_lazy('sistema')
#ELIMINAR ARTICULOS
#@login_required
class eliminarArticulo(DeleteView):
	model = Articulossegunda
	context_object_name="articulos"
	template_name = 'articulos/eliminar.html'
	success_url = reverse_lazy('sistema')

class filtrarAjaxArticuloSegunda(TemplateView):
	def get(self,request,*args,**kwargs):
		nombreProveedor = request.GET.get('nombre')
		articulosSegunda = Articulossegunda.objects.filter(Q(art_nombre__contains =nombreProveedor)|Q(art_cantidad__contains=nombreProveedor)).order_by("id")
		data = serializers.serialize('json',articulosSegunda,fields=('id','art_nombre','art_precio','art_cantidad','art_serie','art_estado','mar','mod'))
		return HttpResponse(data,content_type='application/json')
