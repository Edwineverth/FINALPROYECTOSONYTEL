from django.contrib import admin
from models import * 

class formatoFacturadetalle(admin.ModelAdmin):
	list_display = ('pro','det_cantiadd','det_preciou','det_preciot',)

class detallefacturaInline(admin.StackedInline):
	model=Facturadetalle
	raw_id_fields=('pro',)
	extra=1

	#list_display = ('fac','pro','det_cantiadd','det_preciou','det_preciot',)
class FacturaAdmin(admin.ModelAdmin):
	search_fields=('cli',)
	list_filter=('cli','fac_fecha',)
	raw_id_fields=('cli',)
	inlines = (detallefacturaInline,)


# Register your models here.
admin.site.register(Articulossegunda)
admin.site.register(Categoria)
admin.site.register(Ciudad)
admin.site.register(Clientes)
admin.site.register(Detalleproveedor)
admin.site.register(Factura,FacturaAdmin)
admin.site.register(Facturadetalle,formatoFacturadetalle)
admin.site.register(Facturadetallemantenimiento)
admin.site.register(Mantenimiento)
admin.site.register(Mensajeria)
admin.site.register(Modelo)
admin.site.register(OrdenDeCompra)
admin.site.register(Productos)
admin.site.register(Proveedor)
admin.site.register(Repuestos)
admin.site.register(Solicitudmantenimiento)
#admin.site.register(Perfil)
