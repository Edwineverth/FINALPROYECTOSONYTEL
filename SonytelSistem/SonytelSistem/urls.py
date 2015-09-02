from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^',include('apps.sistema.urls')),
    url(r'^$',TemplateView.as_view(template_name='SITIOWEB/nova/inicio.html'),name='homeinicio'),
    url(r'^cerrar/$','django.contrib.auth.views.logout_then_login',name='logout'),
    url(r'^acercade/',TemplateView.as_view(template_name='SITIOWEB/nova/about-us.html'),name='acercadee'),
    url(r'^servicios/',TemplateView.as_view(template_name='SITIOWEB/nova/services.html'),name='servicios'),
    url(r'^contactenos/',TemplateView.as_view(template_name='SITIOWEB/nova/contact-us.html'),name='contactenos'),
    url(r'^registro/','django.contrib.auth.views.login',{'template_name':'SITIOWEB/nova/iniciosistema.html'},name='login'),
    url(r'^registrate/',TemplateView.as_view(template_name='SITIOWEB/nova/registration.html'),name='registrodesistema'),
    url(r'^cliente/',include('apps.sistema.urls')),
    url(r'^articulos/',include('apps.articulos.urls')),
    url(r'^modelo/',include('apps.modelo.urls')),
    url(r'^ciudad/',include('apps.ciudad.urls')),
    url(r'^proveedor/',include('apps.proveedor.urls')),
    url(r'^categoria/',include('apps.categoria.urls')),
    url(r'^factura/',include('apps.factura.urls')),
    url(r'^mensajeria/',include('apps.mensajeria.urls')),
    url(r'^facturadetalle/',include('apps.facturadetallle.urls')),
    url(r'^solicitudmantenimiento/',include('apps.solicitudmantenimiento.urls')),
    url(r'^mantenimiento/',include('apps.mantenimiento.urls')),
    url(r'^productos/',include('apps.producto.urls')),
    



)
