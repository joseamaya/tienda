from django.conf.urls import url
from django.views.generic import TemplateView

from facturacion import views

urlpatterns = [
	url(r'^$',views.factura, name="factura"),
	url(r'^guardarFactura/$',views.guardarFactura, name="guardarFactura"),
	url(r'^busquedaCliente/$',views.BusquedaCliente.as_view(), name="busquedaCliente"),
	url(r'^busquedaProducto/$',views.BusquedaProducto.as_view(), name="busquedaProducto"),
	url(r'^nuevoCliente/$',views.NuevoCliente.as_view(), name="nuevoCliente"),
	url(r'^nueva_serie/$',views.NuevaSerie.as_view(), name="nueva_serie"),
	url(r'^nuevo_tipo_documento/$',views.NuevoTipoDocumento.as_view(), name="nuevo_tipo_documento"),
	url(r'^clientes/$',views.Clientes.as_view(), name="clientes"),
	url(r'^productos/$',views.Productos.as_view(), name="productos"),
	url(r'^cliente/(?P<pk>\d+)/$',views.DetalleCliente.as_view(), name="cliente"),
	url(r'^producto/(?P<pk>\d+)/$',views.DetalleProducto.as_view(), name="producto"),
	#url(r'^(?P<encuesta_id>\d+)/$',views.detalle, name='detalle'),
	#url(r'^(?P<encuesta_id>\d+)/resultados/$',views.resultados, name='resultados'),
	#url(r'^(?P<encuesta_id>\d+)/voto/$',views.voto, name='voto'),
]