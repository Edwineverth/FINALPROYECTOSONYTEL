from django.conf.urls import patterns, include, url
from .views import crearProveedor,editarProveedor,eliminarProveedor,filtrarAjaxProveedor,listarProveedor
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),
    #********************CLIENTE*********************************************
    url(r'^registrar/$', crearProveedor.as_view(),name='crearProveedor'),
    url(r'^editar/(?P<pk>[\d]+)$', editarProveedor.as_view(),name='editarProveedor'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarProveedor.as_view(),name='eliminarProveedor'),
    url(r'^filtro/$', filtrarAjaxProveedor.as_view(),name='filtrarProveedor'),
    url(r'^listar/$', listarProveedor.as_view(),name='listarProveedor'),

    #*********************PROVEEDOR***************************************
    
    
)
