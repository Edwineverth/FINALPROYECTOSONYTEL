from django.shortcuts import render
from apps.sistema.models import Mensajeria, Clientes
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	
from django.db.models import Q

# Create your views heres.
class crearMensajeria(CreateView):
	template_name='mensajeria/crear.html'
	model=Mensajeria
	success_url=reverse_lazy('sistema')
	def get_context_data(self, **kwargs):
		ctx = super(crearMensajeria, self).get_context_data(**kwargs)
		ctx['listarMensajes'] = Mensajeria.objects.all()
		return ctx

#LISTAR ARTICULOS
class listarMensajeria(ListView):
	template_name='mensajeria/editar.html'
	context_object_name='mensajeria'
	model=Mensajeria
#ACTUALIZAR ARTICULOS
class editarMensajeria(UpdateView):
	model = Mensajeria
	template_name= 'mensajeria/editar.html'
	success_url=reverse_lazy('sistema')
#ELIMINAR ARTICULOS
class eliminarMensajeria(DeleteView):
	model = Mensajeria
	context_object_name="mensajeria"
	template_name = 'mensajeria/eliminar.html'
	success_url = reverse_lazy('sistema')

#FILTRADO DE Mensajeria *****
class filtrarMensajeria(ListView):
	model = Mensajeria
	context_object_name = "mensajerias"
	template_name='mensajeria/filtrar.html'


#RETORNO AJAX FILTRADO *****
class filtrarAjaxMensajeria(TemplateView):
	def get(self,request,*args,**kwargs):
		nombreMensajeria = request.GET.get('nombre')
		mensajeria = Mensajeria.objects.filter(Q(men_asunto__contains=nombreMensajeria)| Q(men_descripcion__contains=nombreMensajeria))
		data = serializers.serialize('json',mensajeria,fields=('men_asunto','men_descripcion','cli'))
		return HttpResponse(data,content_type='application/json')