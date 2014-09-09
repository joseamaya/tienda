from django.db import models

# Create your models here.
class Cliente(models.Model):
    ruc = models.CharField(max_length=11,primary_key=True)
    razon_social = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    class Meta:
        verbose_name = ('cliente')
        verbose_name_plural = ('clientes')

    def __unicode__(self):
        return self.razon_social

class Producto(models.Model):
    descripcion = models.CharField(max_length=50)
    precio = models.FloatField()
    unidad = models.CharField(max_length=4)
    class Meta:
        verbose_name = ('Producto')
        verbose_name_plural = ('Productos')

    def __unicode__(self):
        return self.descripcion

class TipoDocumento(models.Model):
    descripcion = models.CharField(max_length=100)
    codigo_sunat = models.CharField(max_length=2)
    class Meta:
        verbose_name = ('TipoDocumento')
        verbose_name_plural = ('TipoDocumentos')

    def __unicode__(self):
        return self.descripcion
    

class Serie(models.Model):
    serie = models.CharField(max_length=4, primary_key=True)
    numerador = models.IntegerField()
    tipo_documento = models.ForeignKey(TipoDocumento)
    class Meta:
        verbose_name = ('Serie')
        verbose_name_plural = ('Series')

    def __unicode__(self):
        return self.serie
    

class Factura(models.Model):
    serie = models.ForeignKey(Serie)
    numero = models.CharField(max_length=6)
    fecha = models.DateField()
    subtotal = models.FloatField()
    igv = models.FloatField()
    total = models.FloatField()
    cliente = models.ForeignKey(Cliente)
    class Meta:
        verbose_name = ('Factura')
        verbose_name_plural = ('Facturas')

    def __unicode__(self):
    	return self.serie.serie+"-"+self.numero
    

class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura)
    producto = models.ForeignKey(Producto)
    cantidad = models.IntegerField()
    class Meta:
        verbose_name = ('DetalleFactura')
        verbose_name_plural = ('DetalleFacturas')

    def __unicode__(self):
        pass
    
    
    