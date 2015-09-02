from django.shortcuts import render
from apps.sistema.models import Productos,Categoria,Modelo
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import Q


class Insertar_Producto(CreateView):
	template_name="productos/crear.html"
	model=Productos
	success_url=reverse_lazy('sistema')
class listarProducto(ListView):
	template_name= "productos/listar.html"
	model = Productos
	context_object_name='productos'
	def get_context_data(self, **kwargs):
		ctx = super(listarProducto, self).get_context_data(**kwargs)
		ctx['categorias'] = Categoria.objects.all()
		return ctx
class editarProducto(UpdateView):
	template_name = "productos/editar.html"
	context_object_name= "productos"
	model = Productos
	success_url=reverse_lazy('sistema')
class eliminarProducto(DeleteView):
	template_name = "productos/eliminar.html"
	context_object_name = "productos"
	model = Productos
	success_url=reverse_lazy('sistema')

class filtrarAjaxProducto(TemplateView):
	def get(self,request,*args,**kwargs):
		nombreProducto = request.GET.get('nombre')
		cliente = Productos.objects.filter(Q(pro_nombre__icontains =nombreProducto)|Q(pro_ecg__icontains=nombreProducto)).order_by("id")
		data = serializers.serialize('json',cliente,fields=('id','pro_nombre','pro_cantidad','pro_precio','pro_ecg','pro_tarifa_iva','pro_ex','pro_pvp','mar_id'))
		return HttpResponse(data,content_type='application/json')
