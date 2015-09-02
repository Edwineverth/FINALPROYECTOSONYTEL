from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),

    url(r'^generar/$', generarRegistroMantenimiento,name='crearMantenimiento'),
    url(r'^guardar/$', guardar,name='guardarmantenimiento'),
    url(r'^listado/$', MantenimientoListView.as_view(),name='listarMantenimientos'),
    url(r'^editar/(?P<pk>[\d]+)$', MantenimientoUpdate.as_view(),name='editarMantenimientoM'),
    url(r'^detalle/(?P<pk>[\d]+)$', MatenimientoDetalle.as_view(),name='mantenimientoDetalle'),
    url(r'^eliminar/(?P<pk>[\d]+)$', MantenimientoDelete.as_view(),name='eliminarMantenimientoM'),
    #url(r'^listar/$', listarSolicitudmantenimiento.as_view(),name='listarMantenimiento'),
    #url(r'^espera/$', listarSolicitudmantenimientoespera.as_view(),name='listarMantenimientoespera'),
    #url(r'^crear/$', crearMantenimiento,name='registrarMantenimiento'),
    #url(r'^guardar/$', guardarMantenimiento,name='guardarMantenimiento'),


  
)
