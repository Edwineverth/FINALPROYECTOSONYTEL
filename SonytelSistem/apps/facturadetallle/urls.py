from django.conf.urls import patterns, include, url
from .views import crearFacturadetalle,editarFacturadetalle,eliminarFacturadetalle,facturacion,CreateOrderView,ItemInline
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),

    url(r'^registrar/$', crearFacturadetalle.as_view(),name='crearFacturadetalle'),
    url(r'^editar/(?P<pk>[\d]+)$', editarFacturadetalle.as_view(),name='editarFacturadetalle'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarFacturadetalle.as_view(),name='eliminarFacturadetalle'),
    url(r'^prueba/', facturacion.as_view(),name='facturacion_asc'),
    #url(r'^prueba2/$', FacturaPrueba2.as_view(),name='prueba2'),
    url(r'^prueba2/','apps.facturadetallle.views.cliente',name='clentess'),
    #url(r'^filtrar/$', filtrarMensajeria.as_view(),name='buscar_Mensajeria'),
    #url(r'^filtrador/$', filtrarAjaxMensajeria.as_view(),name='filtrador_Mensajeria'),
  
)