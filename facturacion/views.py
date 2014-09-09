# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, ListView, UpdateView
from facturacion.forms import ClienteForm, ProductoForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
import datetime

from facturacion.models import Factura, DetalleFactura, Cliente, Producto, Serie

def completarSerie(s):
	serie = str(s)
	while(len(serie)<6):
		serie="0"+serie
	return serie

def factura(request):
	serie = Serie.objects.get(pk="0001")
	serie.numerador = completarSerie(serie.numerador+1)
	clientes = Cliente.objects.order_by('razon_social')
	productos = Producto.objects.order_by('descripcion')
	context = {'serie':serie,'clientes':clientes,'productos':productos}
	return render(request, 'facturacion/factura.html', context)

def guardarFactura(request):
	try:
		serie = Serie.objects.get(pk=request.POST['serie'])
		numero = request.POST['numero']
		id_cliente = request.POST['clientes']
		cliente = Cliente.objects.get(pk=id_cliente)
		f = request.POST['fecha']
		fecha = datetime.date(int(f[6:]), int(f[3:5]), int(f[0:2]))
		subtotal = request.POST['subtotal']
		igv = request.POST['igv']
		total = request.POST['total']
		p1 = request.POST['productos1']
		producto1 = Producto.objects.get(pk=p1)
		cantidad1 = request.POST['cantidad1']
		p2 = request.POST['productos2']
		producto2 = Producto.objects.get(pk=p2)
		cantidad2 = request.POST['cantidad2']

	except Exception, e:
		raise
	else:
		factura = Factura(serie=serie,numero=numero,fecha=fecha,subtotal=subtotal,igv=igv,total=total,cliente=cliente)
		factura.save()
		serie.numerador = int(numero)
		serie.save() 
		detalle_factura1 = DetalleFactura(factura=factura, producto=producto1,cantidad=cantidad1)
		detalle_factura1.save()
		detalle_factura2 = DetalleFactura(factura=factura, producto=producto2,cantidad=cantidad2)
		detalle_factura2.save()

		return HttpResponseRedirect(reverse('facturacion:factura'))

class BusquedaCliente(TemplateView):

	def get(self, request, *args, **kwargs):
		ruc = request.GET['ruc']
		cliente = Cliente.objects.get(pk=ruc)
		data = serializers.serialize('json', [cliente])
		c = data.strip("[]")
		return HttpResponse(c, mimetype="application/json")

class BusquedaProducto(TemplateView):

	def get(self, request, *args, **kwargs):
		id_producto = request.GET['id']
		producto = Producto.objects.get(pk=id_producto)
		data = serializers.serialize('json', [producto])
		c = data.strip("[]")
		return HttpResponse(c, mimetype="application/json")

class DetalleCliente(DetailView):
    model = Cliente
    template_name = "facturacion/detalle_cliente.html"
    context_object_name = "cliente"

class DetalleProducto(DetailView):
    model = Producto
    template_name = "facturacion/detalle_producto.html"
    context_object_name = "producto"

class Clientes(ListView):
    model = Cliente
    template_name = "facturacion/clientes.html"
    context_object_name = "clientes"

class Productos(ListView):
    model = Producto
    template_name = "facturacion/productos.html"
    context_object_name = "productos"

class NuevoCliente(CreateView):
    model = Cliente
    template_name = "facturacion/nuevo_cliente.html"
    success_url = reverse_lazy("facturacion:factura")

class ActualizarProducto(UpdateView):
    model =	Producto
    template_name = "noticias/form_producto.html"
    form_class = ProductoForm
    success_url = reverse_lazy("facturacion:productos")