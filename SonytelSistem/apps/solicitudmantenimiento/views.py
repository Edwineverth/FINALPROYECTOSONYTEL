from django.shortcuts import render,render_to_response,RequestContext
from apps.sistema.models import Solicitudmantenimiento, Clientes,Articulossegunda
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	
from django.db.models import Q

# Create your views here.
class crearSolicitudMantenimiento(CreateView):
	template_name='mantenimiento/crear.html'
	model=Solicitudmantenimiento
	success_url=reverse_lazy('home')

#LISTAR ARTICULOS
class listarSolicitudmantenimiento(ListView):
	template_name='mantenimiento/listar.html'
	context_object_name='Solicitudmantenimiento'
	model=Solicitudmantenimiento
	def get_context_data(self, **kwargs):
		ctx = super(listarSolicitudmantenimiento, self).get_context_data(**kwargs)
		ctx['clientes'] = Clientes.objects.all()
		ctx['articulos'] = Articulossegunda.objects.all()

		return ctx
class listarSolicitudmantenimientoespera(ListView):
	template_name='mantenimiento/crearregistro.html'
	context_object_name='Solicitudmantenimiento'
	model=Solicitudmantenimiento
	def get_context_data(self, **kwargs):
		ctx = super(listarSolicitudmantenimientoespera, self).get_context_data(**kwargs)
		ctx['clientes'] = Clientes.objects.all()
		ctx['articulos'] = Articulossegunda.objects.all()
		return ctx

class listadoatendido(ListView):
	template_name='mantenimiento/atentida.html'
	context_object_name='Solicitudmantenimiento'
	model=Solicitudmantenimiento
	def get_context_data(self, **kwargs):
		ctx = super(listadoatendido, self).get_context_data(**kwargs)
		ctx['clientes'] = Clientes.objects.all()
		ctx['articulos'] = Articulossegunda.objects.all()
		return ctx


#ACTUALIZAR ARTICULOS
class editarSolicitudmantenimiento(UpdateView):
	model = Solicitudmantenimiento
	template_name= 'mantenimiento/editar.html'
	success_url=reverse_lazy('home')
#ELIMINAR ARTICULOS
class eliminarSolicitudmantenimiento(DeleteView):
	model = Solicitudmantenimiento
	context_object_name="Solicitudmantenimiento"
	template_name = 'mantenimiento/eliminar.html'
	def get_context_data(self, **kwargs):
		ctx = super(eliminarSolicitudmantenimiento, self).get_context_data(**kwargs)
		ctx['clientes'] = Clientes.objects.all()
		return ctx
	success_url = reverse_lazy('home')

#FILTRADO DE Solicitudmantenimiento *****
class filtrarSolicitudmantenimiento(TemplateView):
	template_name='mantenimiento/filtrar.html'

def crearMantenimiento(request):

	contexto = {'clientes':Clientes.objects.all(),'articulos':Articulossegunda.objects.filter(art_estado="D"),'solicitudes':1+Solicitudmantenimiento.objects.count()}
	return render_to_response('mantenimiento/crear.html',contexto,context_instance=RequestContext(request))

def guardarMantenimiento(request):
	print "ENTRAAA"
	fecha=request.GET['fecha']
	cliente=request.GET['cliente']
	articulo=request.GET['articulo']
	falla=request.GET['falla']
	observacion=request.GET['observacion']
	abono=request.GET['abono']
	saldo=request.GET['saldo']
	total=request.GET['total']
	print "ENTRA222"



	mant = Solicitudmantenimiento(
		solm_fecha= fecha,
		solm_falla=falla,
		solm_observaciones=observacion,
		solm_abono=abono,
		solm_saldo=saldo,
		solm_total =total,
		solm_estado ="E",
		art_id = (Articulossegunda.objects.get(art_nombre=articulo)).id,
		cli_id = (Clientes.objects.get(cli_nombre=cliente)).id
   		)
	mant.save()
	arti = (Articulossegunda.objects.get(art_nombre=articulo))
	articulos = Articulossegunda(id=arti.id,art_nombre=arti.art_nombre,art_precio=arti.art_precio,art_cantidad=arti.art_cantidad,art_serie=arti.art_serie,art_estado="M",mar_id=arti.mar_id,mod_id=arti.mod_id)
	articulos.save()

	return render_to_response('mantenimiento/crear.html',RequestContext(request))