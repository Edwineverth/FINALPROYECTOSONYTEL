from django.conf.urls import patterns, include, url
from .views import crearCategoria,editarCategoria,eliminarCategoria,filtrarCategoria,filtrarAjaxCategoria,listarCategoria
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),
    #********************CLIENTE*********************************************
  
    url(r'^registrar/$', crearCategoria.as_view(),name='crearCategoria'),
    url(r'^editar/(?P<pk>[\d]+)$', editarCategoria.as_view(),name='editarCategoria'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarCategoria.as_view(),name='eliminarCategoria'),
    url(r'^filtrar/$', listarCategoria.as_view(),name='buscar_Categoria'),
    url(r'^filtrador/$', filtrarAjaxCategoria.as_view(),name='filtrador_Categoria'),
  
)
