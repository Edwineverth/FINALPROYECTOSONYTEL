from django.conf.urls import patterns, include, url
from .views import crearMensajeria,editarMensajeria,eliminarMensajeria,filtrarMensajeria,filtrarAjaxMensajeria
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),

    url(r'^registrar/$', crearMensajeria.as_view(),name='crearMensajeria'),
    url(r'^editar/(?P<pk>[\d]+)$', editarMensajeria.as_view(),name='editarMensajeria'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarMensajeria.as_view(),name='eliminarMensajeria'),
    url(r'^filtrar/$', filtrarMensajeria.as_view(),name='buscar_Mensajeria'),
    url(r'^filtrador/$', filtrarAjaxMensajeria.as_view(),name='filtrador_Mensajeria'),
  
)
