from django.shortcuts import render
from apps.sistema.models import Proveedor,Ciudad
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here.
class crearProveedor(CreateView):
	template_name='proveedor/crear.html'
	model=Proveedor
	success_url=reverse_lazy('sistema')

#LISTAR ARTICULOS
class listarProveedor(ListView):
	template_name='proveedor/filtrar.html'
	context_object_name='Proveedores'
	model=Proveedor
	def get_context_data(self, **kwargs):
		ctx = super(listarProveedor, self).get_context_data(**kwargs)
		ctx['ciudades'] = Ciudad.objects.all()
		return ctx
#ACTUALIZAR ARTICULOS
class editarProveedor(UpdateView):
	model = Proveedor
	template_name= 'proveedor/editar.html'
	context_object_name = "proveedores"
	success_url=reverse_lazy('sistema')
#ELIMINAR ARTICULOS
class eliminarProveedor(DeleteView):
	model = Proveedor
	context_object_name="Proveedores"
	template_name = 'proveedor/eliminar.html'
	success_url = reverse_lazy('sistema')

class filtrarAjaxProveedor(TemplateView):
	def get(self,request,*args,**kwargs):
		nombreProveedor = request.GET.get('nombre')
		cliente = Proveedor.objects.filter(Q(prov_nombre__icontains =nombreProveedor)|Q(prov_cedula__icontains=nombreProveedor)).order_by("id")
		data = serializers.serialize('json',cliente,fields=('id','prov_ruc','prov_cedula','prov_nombre','prov_representante','prov_direccion','prov_telefono','prov_estado','ciu_id'))
		return HttpResponse(data,content_type='application/json')
