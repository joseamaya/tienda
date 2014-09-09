from django.contrib import admin
from facturacion.models import Cliente, Producto, TipoDocumento, Serie, DetalleFactura, Factura

class DetalleEnLinea(admin.TabularInline):
	model = DetalleFactura
		
class FacturaAdmin(admin.ModelAdmin):

	inlines = [DetalleEnLinea]

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(TipoDocumento)
admin.site.register(Serie)
admin.site.register(Factura, FacturaAdmin)
