from django.conf.urls import patterns, include, url
from .views import index,registrarCliente,listarCliente,editar,eliminar,filtrarCliente,filtrarAjaxcliente,presentacionsistema
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^sistema/$', presentacionsistema,name='sistema'),
    url(r'^registrar/$', registrarCliente.as_view(),name='registrar_cliente'),
    url(r'^listado/$', listarCliente.as_view(),name='listar_cliente'),
    url(r'^filtrar/$', filtrarCliente.as_view(),name='buscar_cliente'),
    url(r'^filtrador/$', filtrarAjaxcliente.as_view(),name='filtrador_cliente'),
    url(r'^editar/(?P<pk>[\d]+)$', editar.as_view(),name='editar'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminar.as_view(),name='eliminar'),
    
)
