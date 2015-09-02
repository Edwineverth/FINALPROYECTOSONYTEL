from django.shortcuts import render
from apps.sistema.models import Facturadetalle,Factura,Productos,Categoria,Clientes,Articulossegunda
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet
from extra_views.generic import GenericInlineFormSet
from django.http import HttpResponse
from django.core import serializers	
from django.db.models import Q
from django.template import Context, Template
from .forms import detalleFacturaForm
# Create your views here.

class crearFacturadetalle(CreateView):
	template_name='detalleFactura/crear.html'
	model=Facturadetalle
	success_url=reverse_lazy('home')

#LISTAR ARTICULOS
class listarFacturadetalle(ListView):
	template_name='detalleFactura/editar.html'
	context_object_name='facturadetalle'
	model=Facturadetalle
#ACTUALIZAR ARTICULOS
class editarFacturadetalle(UpdateView):
	model = Facturadetalle
	template_name= 'detalleFactura/editar.html'
	success_url=reverse_lazy('home')
#ELIMINAR ARTICULOS
class eliminarFacturadetalle(DeleteView):
	model = Facturadetalle
	context_object_name="facturadetalle"
	template_name = 'detalleFactura/eliminar.html'
	success_url = reverse_lazy('home')

#FILTRADO DE Facturadetalle *****
class filtrarFacturadetalle(TemplateView):
	template_name='detalleFactura/filtrar.html'

class facturacion(TemplateView):
	factura = Factura
	facturadet = Facturadetalle
	template_name = 'detalleFactura/prueba.html'

"""class facturacion(FormView):
	template_name= 'detalleFactura/prueba.html'
	form_class = detalleFacturaForm
	success_url=reverse_lazy('/')
	def form_valid(self,form):
		user= form.save()
		perfil=Perfiles()
		perfil.usuario=user
		perfil.telefono=form.cleaned_data['telefono']
		perfil.save()
		return super(Registrarse,self).form_valid(form)
"""

class ItemInline(InlineFormSet):
    model = Facturadetalle
    raw_id_fields=('pro',)
    extra=1


class TagInline(GenericInlineFormSet):
    model = Productos


class CreateOrderView(CreateWithInlinesView):
    model = Factura
    inlines = [ItemInline]
    template_name = "detalleFactura/prueba.html"


def cliente(request):
	clientes = Clientes.objects.all()
	articulos = Articulossegunda.objects.all()
	template = "detalleFactura/prueba.html"
	return render(request,template,locals())
#RETORNO AJAX FILTRADO *****
class filtrarAjaxFacturadetalle(TemplateView):
	def get(self,request,*args,**kwargs):
		nombreFacturadetalle = request.GET.get('nombre')
		Facturadetalle = Facturadetalle.objects.filter(Q(men_asunto__contains=nombreMensajeria)| Q(men_descripcion__contains=nombreMensajeria))
		data = serializers.serialize('json',mensajeria,fields=('men_asunto','men_descripcion','cli'))
		return HttpResponse(data,content_type='application/json')