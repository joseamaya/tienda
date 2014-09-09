from django import forms 
from facturacion.models import Cliente, Producto

class ClienteForm(forms.ModelForm):
	class Meta():
		model = Cliente

class ProductoForm(forms.ModelForm):
	class Meta():
		model = Producto