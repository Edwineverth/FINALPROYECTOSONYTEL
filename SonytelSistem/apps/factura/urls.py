from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^crear/$', generarVentaFactura,name='crearFactura'),
    url(r'^crearr/$', guardarFactura,name='crearFacturad'),
    url(r'^imprimir/$', imprimir.as_view(),name='imprimirfac'),
    url(r'^eliminador/$', eliminarultimo,name='eliminar'),
    url(r'^listado/$', listarFacturas.as_view(),name='listarFacturas'),
    url(r'^filtrador/$', filtrarAjaxFactura.as_view(),name='filtradorajax'),
    url(r'^detalle/(?P<pk>[\d]+)$', detalleFactura.as_view(),name='detallefactura'),


   
    
)
