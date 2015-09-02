from django.conf.urls import patterns, include, url
from .views import crearArticulo,editarArticulo,eliminarArticulo,listarArticulos,filtrarAjaxArticuloSegunda
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),
    #********************CLIENTE*********************************************
    url(r'^registrar/$', crearArticulo.as_view(),name='crearArticulo'),
    url(r'^listar/$', listarArticulos.as_view(),name='listarArticulos'),
    url(r'^filtrador/$', filtrarAjaxArticuloSegunda.as_view(),name='filtradorArticulos'),
    url(r'^editar/(?P<pk>[\d]+)$', editarArticulo.as_view(),name='editarArticulo'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarArticulo.as_view(),name='eliminarArticulo'),

    #*********************PROVEEDOR***************************************
    
    
)
