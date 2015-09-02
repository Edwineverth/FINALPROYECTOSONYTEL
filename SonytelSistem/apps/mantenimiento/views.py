from django.shortcuts import render,render_to_response,RequestContext
from apps.sistema.models import Solicitudmantenimiento, Clientes,Articulossegunda,Productos,Categoria,Modelo,Mantenimiento,Repuestos
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView,DetailView
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers	
from django.db.models import Q

class MantenimientoListView(ListView):
	model = Mantenimiento
	context_object_name='mantenimiento'
	template_name = "mantenimiento/listarmantenimiento.html"
	def get_context_data(self, **kwargs):
		ctx = super(MantenimientoListView, self).get_context_data(**kwargs)
		ctx['solicitudmantenimiento'] = Solicitudmantenimiento.objects.all()
		ctx['repuestos'] = Repuestos.objects.all()
		return ctx

class MantenimientoUpdate(UpdateView):
	model = Mantenimiento
	template_name= 'mantenimiento/editar.html'
	success_url=reverse_lazy('home')

class MantenimientoDelete(DeleteView):
	model = Mantenimiento
	context_object_name="mantenimiento"
	template_name = 'mantenimiento/eliminarM.html'
	def get_context_data(self, **kwargs):
		ctx = super(MantenimientoListView, self).get_context_data(**kwargs)
		ctx['solicitudmantenimiento'] = Solicitudmantenimiento.objects.all()
		ctx['repuestos'] = Repuestos.objects.all()
		return ctx
	
class MatenimientoDetalle(DetailView):
	model = Mantenimiento
	context_object_name = "mantenimiento"
	template_name = 'mantenimiento/detallemantenimiento.html'
	def get_context_data(self, **kwargs):
		ctx = super(MatenimientoDetalle, self).get_context_data(**kwargs)
		ctx['solicitudmantenimiento'] = Solicitudmantenimiento.objects.all()
		ctx['repuestos'] = Repuestos.objects.all()
		ctx['productos'] = Productos.objects.all()
		return ctx
		


def generarRegistroMantenimiento(request):
	#__gte mayor igual
	#__lte menor igual
	contexto ={'productos':Productos.objects.filter(pro_cantidad__gte=30),'clientes':Clientes.objects.all(),'solicitudes':Solicitudmantenimiento.objects.all(),'articulos':Articulossegunda.objects.all(),'modelos':Modelo.objects.all(),'categorias':Categoria.objects.all(),'nmantenimiento':1+Mantenimiento.objects.count()}
	return render_to_response('mantenimiento/apertura.html',contexto,context_instance=RequestContext(request))

def guardar(request):

	codigo= request.GET['codigo']
	nombre= request.GET['nombre']
	cantidad= request.GET['cantidad']
	garantia= request.GET['garantia']
	fechaentrega= request.GET['fechaentrega']
	informe= request.GET['informe']
	fechacompra= request.GET['fechacompra']
	num = request.GET['numero']
	print num
	m=Mantenimiento.objects.filter(id=request.GET['numeroM']).count()
	
	newf = fechacompra.split(' ')
	
	ffcompra=newf[0]
	valor1= ffcompra.split('/')
	
	newf2=fechaentrega.split(' ')
	ffentrega = newf2[0]
	valor2=ffentrega.split('/')
	if str(num)=='1':
		mante= Mantenimiento(
			man_fecha=  "%s-%s-%s" %( valor1[2],valor1[0],valor1[1]),
			man_garantia= garantia,
			man_informe= informe,
			man_fechaentrega="%s-%s-%s" %( valor2[2],valor2[0],valor2[1]),
			man_estado= "R",
			solm_id= request.GET['nmant']
			)
		mante.save()

	else:
		pass

	s = Solicitudmantenimiento.objects.get(id=request.GET['nmant'])
	solicitud = Solicitudmantenimiento(

		id=s.id ,
		solm_fecha=s.solm_fecha,
		solm_falla=s.solm_falla ,
		solm_observaciones=s.solm_observaciones ,
		solm_abono=s.solm_abono ,
		solm_saldo=s.solm_saldo ,
		solm_total=s.solm_total ,
		solm_estado="A" ,
		art_id=s.art_id ,
		cli_id=s.cli_id 

		)
	solicitud.save()
	
	repu = Repuestos(
		rep_cantidad=cantidad,
		man_id=request.GET['numeroM'],
		pro_id=codigo)
	repu.save()

	listarProductos = Productos.objects.get(id=codigo)

	refrescarstock =listarProductos.pro_cantidad - int(cantidad)
	producto = Productos(
		id=listarProductos.id,
		pro_nombre= listarProductos.pro_nombre,
		pro_cantidad= refrescarstock ,
		pro_precio= listarProductos.pro_precio ,
		pro_ecg = "ESQ",
		pro_tarifa_iva = listarProductos.pro_tarifa_iva,
		pro_ex = listarProductos.pro_ex,
		pro_pvp = listarProductos.pro_pvp,
		mar_id = listarProductos.mar_id,
		)
	producto.save()


	
	return render_to_response('mantenimiento/apertura.html',context_instance=RequestContext(request))
