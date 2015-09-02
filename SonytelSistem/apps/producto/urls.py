from django.conf.urls import patterns, include, url
from .views import Insertar_Producto,listarProducto,listarProducto,filtrarAjaxProducto,editarProducto,eliminarProducto
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^registrarproducto/$', Insertar_Producto.as_view(),name='RegistrarProducto'),
    #url(r'^registrar/$', registrarCliente.as_view(),name='registrar_cliente'),
    url(r'^listar/$', listarProducto.as_view(),name='listar_Producto'),
    #url(r'^filtrar/$', filtrarCliente.as_view(),name='buscar_cliente'),
    url(r'^filtrador/$', filtrarAjaxProducto.as_view(),name='filtrador_producto'),
    url(r'^editar/(?P<pk>[\d]+)$', editarProducto.as_view(),name='editarproducto'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarProducto.as_view(),name='eliminarproducto'),
    #url(r'^test-form/$', TestFormView.as_view(), name="test-form"),
    
)