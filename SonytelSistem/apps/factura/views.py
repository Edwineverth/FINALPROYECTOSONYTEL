# -*- coding: utf-8 -*-
from django.shortcuts import render
from apps.sistema.models import Factura,Clientes,Facturadetalle,Productos
from apps.sistema.views import registrarCliente
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView,DetailView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.core import serializers	
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import Q
"************************************************"



class listarFacturas(ListView):
	template_name='factura/filtrar.html'
	context_object_name='listarFacturas'
	model=Factura
	def get_context_data(self, **kwargs):
		ctx = super(listarFacturas, self).get_context_data(**kwargs)
		ctx['clientes'] = Clientes.objects.all()
		return ctx


class detalleFactura(DetailView):
	template_name='detalleFactura/prueba.html'
	context_object_name='listarFacturas'
	model=Factura
	def get_context_data(self, **kwargs):
		ctx = super(detalleFactura, self).get_context_data(**kwargs)
		ctx['detalles'] = Facturadetalle.objects.all()
		ctx['productos'] = Productos.objects.all()
		return ctx

class filtrarAjaxFactura(TemplateView):
	def get(self,request,*args,**kwargs):
		nombrefact = request.GET.get('nombre')
		print nombrefact
		cliente = Clientes.objects.get(cli_nombre__icontains=nombrefact)
		print cliente
		modelador = Factura.objects.filter(cli_id =cliente.id)
		ident  = ''
		data = serializers.serialize('json',modelador,fields=('id_fac','fac_subtotal','fac_iva','fac_descuento','fac_total','fac_fecha','fac_estado','cli','serializador'))
		return HttpResponse(data,content_type='application/json')

				
def generarVentaFactura(request):

	objetosplantilla = {"listarclientes":Clientes.objects.filter(cli_estado="A"),"listarProductos":Productos.objects.all(),'nFactura': 1+Factura.objects.count()}
	return render_to_response('factura/crear.html', objetosplantilla, context_instance=RequestContext(request))

def eliminarultimo(request):
	voto_id = Factura.objects.latest('id_fac')
	voto_id.delete()
	return render_to_response('factura/crear.html',context_instance=RequestContext(request))


def guardarFactura(request):
	print "ASTA1 "
	codigoProducto= request.GET['codigo']
	cantidad = request.GET['cantidad']
	precio = (request.GET['precio'])
	cedula = request.GET['cedula']
	total =request.GET['total']
	num = request.GET['numero']

	pronombre= request.GET['nombrep']
	clinombre= request.GET['nombrec']


	listarProductos = Productos.objects.get(id=codigoProducto)
	unCliente= Clientes.objects.get(cli_cedula=cedula)
	print unCliente

	if (((int)(num)) == 1):
		print "ENTRA IF"
		fact = Factura(fac_subtotal=request.GET['subtotal'],fac_iva=request.GET['iva'],fac_descuento=request.GET['descuento'],fac_total =request.GET['total'],fac_fecha=request.GET['fechaa'],fac_estado="F",cli_id= unCliente.id,serializador = 1+Factura.objects.count())
		print "guardar"
		fact.save()
		print fact.id_fac
		pass

	idFactura = Factura.objects.get(id_fac =request.GET['nFactura'] )
	detalle = Facturadetalle(
		det_cantiadd=cantidad,
		det_preciou= precio,
		det_preciot= total,
		fac = idFactura,
		pro_id= listarProductos.id
		)
	detalle.save()
	refrescarStock = listarProductos.pro_cantidad - int(cantidad)
	#PROCESO PARA ACTUALIZAR EL STOCK DEL PRODUCTO ES NECESARIO INGRESAR TODAS LAS CANTIDADES  DEL PRODUCTO
	producto = Productos(
		id=listarProductos.id,
		pro_nombre= listarProductos.pro_nombre,
		pro_cantidad= refrescarStock ,
		pro_precio= listarProductos.pro_precio ,
		pro_ecg = "ESQ",
		pro_tarifa_iva = listarProductos.pro_tarifa_iva,
		pro_ex = listarProductos.pro_ex,
		pro_pvp = listarProductos.pro_pvp,
		mar_id = listarProductos.mar_id,
		)
	producto.save()


	print "******************FIN****************"

	return render_to_response('factura/crear.html',context_instance=RequestContext(request))

def envio(request):
	enviar_email_factura("edwineverth94@gmail.com","oracleedwineverth","esto es una prueba del servidor")






"*************************************ENVIO DE CORREO ELECTRONICO**************************************"
def enviar_email_factura(user, password, asunto, destinatario):
	#rutapdf
	print("asassssssssssssssss")
	parser = OptionParser()
	parser.add_option("-f", "--from", dest="sender", help="sender email address", default=user)
	parser.add_option("-t", "--to", dest="recipient", help="recipient email address", default=destinatario)
	parser.add_option("-s", "--subject", dest="subject", help="email subject", default=asunto)
	parser.add_option("-i", "--image", dest="image", help="image attachment", default=False)
	parser.add_option("-p", "--pdf", dest="pdf", help="pdf attachment", default=False)

	print("asassssssssssssssss------------")
	(options, args) = parser.parse_args()

	# Create message container.
	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = options.subject
	msgRoot['From'] = options.sender
	msgRoot['To'] = options.recipient
	print(options.recipient)

	# Create the body of the message.
	html = """\
	    <p>This is an inline image<br/>
	        <img src="cid:image1">
	    </p>
	"""

	# Record the MIME types.
	msgHtml = MIMEText(html, 'html')

	msgImg=""
	if options.image is not False:
	    img = open(options.image, 'rb').read()
	    msgImg = MIMEImage(img, 'png')
	    msgImg.add_header('Content-ID', '<image1>')
	    msgImg.add_header('Content-Disposition', 'inline', filename=options.image)

	msgPdf=""
	print("asas")
	if options.pdf is not False:
	    print("sds" + options.pdf)
	    #cd ..
	    pdf = open(options.pdf, 'rb').read()
	    msgPdf = MIMEApplication(pdf, 'pdf') # pdf for exemple
	    msgPdf.add_header('Content-ID', '<pdf1>') # if no cid, client like MAil.app (only one?) don't show the attachment
	    msgPdf.add_header('Content-Disposition', 'attachment', filename=options.pdf)
	    msgPdf.add_header('Content-Disposition', 'inline', filename=options.pdf)

	#msgRoot.attach(msgHtml)
	#msgRoot.attach(msgImg)
	msgRoot.attach(msgPdf)

	# Send the message via local SMTP server.
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login(user, password)
	s.set_debuglevel(1)
	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	#s.sendmail(options.sender, options.recipient, msgRoot.as_string())
	s.sendmail("akirevacacela@gmail.com", "estefaniavacacela@gmail.com", msgRoot.as_string())
	s.quit()

"***********************************************************************************+"
class imprimir(TemplateView):
    template_name='factura/reporte.html'
    def get_context_data(self, **kwargs):
		ctx = super(imprimir, self).get_context_data(**kwargs)
		idcliente = (Factura.objects.latest('id_fac')).cli_id
		ctx['listarClientes'] = Clientes.objects.get(id= idcliente)
		ctx['nFactura'] = (Factura.objects.latest('id_fac')).id_fac
		numero=(Factura.objects.latest('id_fac')).id_fac
		ctx['listarFacturas'] = Factura.objects.get(id_fac=numero)
		ctx['detalles'] = Facturadetalle.objects.filter(fac_id=numero)
		return ctx