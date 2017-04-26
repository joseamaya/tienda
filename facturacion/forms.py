from django import forms 
from facturacion.models import Cliente, Producto, TipoDocumento, Serie

class ClienteForm(forms.ModelForm):

	class Meta():
		model = Cliente
		fields = ['ruc','razon_social','direccion']

class ProductoForm(forms.ModelForm):

	class Meta():
		model = Producto
		fields = ['descripcion', 'precio', 'unidad']

class TipoDocumentoForm(forms.ModelForm):

	class Meta():
		model = TipoDocumento
		fields = ['descripcion', 'codigo_sunat']

class SerieForm(forms.ModelForm):

	class Meta():
		model = Serie
		fields = ['serie', 'numerador','tipo_documento']