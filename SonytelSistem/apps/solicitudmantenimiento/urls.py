from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),

    url(r'^registrar/$', crearSolicitudMantenimiento.as_view(),name='crearMantenimiento'),
    url(r'^editar/(?P<pk>[\d]+)$', editarSolicitudmantenimiento.as_view(),name='editarMantenimiento'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarSolicitudmantenimiento.as_view(),name='eliminarMantenimiento'),
    url(r'^listar/$', listarSolicitudmantenimiento.as_view(),name='listarMantenimiento'),
    url(r'^espera/$', listarSolicitudmantenimientoespera.as_view(),name='listarMantenimientoespera'),
    url(r'^atendida/$', listadoatendido.as_view(),name='dasdasdasd'),

    url(r'^crear/$', crearMantenimiento,name='registrarMantenimiento'),
    url(r'^guardar/$', guardarMantenimiento,name='guardarMantenimiento'),



  
)
