# -*- coding: utf-8 -*e
from __future__ import unicode_literals

from django.db import models


class Articulossegunda(models.Model):
    art_nombre = models.CharField(max_length=30,verbose_name=u"Nombre:")
    art_precio = models.FloatField(verbose_name=u"Precio:")
    art_cantidad = models.IntegerField(verbose_name=u"Cantidad")
    art_serie = models.CharField(max_length=50,verbose_name=u"Serie")
    mar = models.ForeignKey('Categoria', blank=True, null=True,verbose_name=u"Marca",db_index=True,editable=True)
    mod = models.ForeignKey('Modelo', blank=True, null=True,verbose_name=u"Modelo")
    art_estado = models.CharField(default='D',editable=False,max_length=1,verbose_name=u"Estado")
    class Meta:
        ordering = ["id"]

    def __unicode__(self):
        return self.art_nombre




class Categoria(models.Model):
    mar_nombre = models.CharField(max_length=30,verbose_name=u"Nombre:")
    mar_descripcion = models.CharField(max_length=75,verbose_name=u"Descripción:")
    class Meta:
        ordering = ["id"]
    def __unicode__(self):
        return self.mar_nombre



class Ciudad(models.Model):
   
    ciu_nombre = models.CharField(max_length=30,verbose_name=u"Nombre:")
    ciu_descripcion = models.CharField(max_length=70,verbose_name=u"Descripción:")
    class Meta:
        ordering = ["id"]
    def __unicode__(self):
		return self.ciu_nombre


class Clientes(models.Model):
    cli_cedula = models.CharField(max_length=10,verbose_name=u"Cedula:")
    cli_nombre = models.CharField(max_length=30,verbose_name=u"Nombre:")
    cli_apellido = models.CharField(max_length=30,verbose_name=u"Apellido:")
    cli_telefono = models.CharField(max_length=10, blank=True,verbose_name=u"Telefono:")
    cli_direccion = models.CharField(max_length=75,verbose_name=u"Dirección:")
    cli_email = models.CharField(max_length=75,verbose_name=u"Email:")
    cli_estado = models.CharField(default='A',editable=False,max_length=1,verbose_name=u"Estado:")
    ciu = models.ForeignKey(Ciudad, blank=True, null=True)
    class Meta:
        ordering = ["id"]
    def __unicode__(self):
		return self.cli_nombre
  

class Detalleproveedor(models.Model):
    pro = models.ForeignKey('Productos', primary_key=True)
    kar_precio_proveedor = models.FloatField(db_column='kar_Precio_proveedor')  # Field name made lowercase.
    kar_entra = models.IntegerField()
    kar_sald = models.IntegerField()
    kar_fecha = models.DateTimeField()
    ord = models.ForeignKey('OrdenDeCompra', blank=True, null=True)

   
class Factura(models.Model):
    id_fac = models.AutoField(primary_key=True)
    fac_subtotal = models.FloatField()
    fac_iva = models.FloatField()
    fac_descuento = models.FloatField(verbose_name=u"Ingrese descuento")
    fac_total = models.FloatField()
    fac_fecha = models.DateField()
    fac_estado = models.CharField(max_length=1)
    cli = models.ForeignKey(Clientes, blank=True, null=True)
    serializador =  models.IntegerField()
    class Meta:
        ordering = ["id_fac"]

 

class Facturadetalle(models.Model):
    fac = models.ForeignKey(Factura, blank=True, null=True)
    pro = models.ForeignKey('Productos', blank=True, null=True)
    det_cantiadd = models.IntegerField()
    det_preciou = models.FloatField()
    det_preciot = models.FloatField()
    class Meta:
        ordering = ["id"]


class Facturadetallemantenimiento(models.Model):
    fac = models.ForeignKey(Factura)
    solm = models.ForeignKey('Solicitudmantenimiento')
    fad_preciou = models.FloatField()
    fad_preciot = models.FloatField()
    class Meta:
        ordering = ["id"]


class Mantenimiento(models.Model):
 
    man_fecha = models.DateField()
    man_garantia = models.IntegerField()
    man_informe = models.TextField(max_length=300)

    man_fechaentrega = models.DateField()
    man_estado = models.CharField(max_length=1, blank=True)
    solm = models.ForeignKey('Solicitudmantenimiento')
    class Meta:
        ordering = ["id"]

    def __unicode__(self):
        return "%s %s" %(self.man_informe,self.man_informe)




class Mensajeria(models.Model):
 
    men_asunto = models.CharField(max_length=30,verbose_name=u"Nombre:")
    men_descripcion = models.CharField(max_length=500,verbose_name=u"Descripción:")
    cli = models.ForeignKey(Clientes)
    class Meta:
        ordering = ["id"]
    def __unicode__(self):
        return self.men_asunto




class Modelo(models.Model):
   
    mod_nombre = models.CharField(max_length=30,verbose_name=u"Nombre:")
    mod_descripcion = models.CharField(max_length=75,verbose_name=u"Descripción:")
    class Meta:
        ordering = ["id"]
    def __unicode__(self):
        return self.mod_nombre

 


class OrdenDeCompra(models.Model):
  
    ord_subtotal = models.FloatField()
    ord_iva = models.FloatField()
    ord_descuento = models.FloatField()
    ord_total = models.FloatField()
    ord_fecha = models.DateField()
    prov = models.ForeignKey('Proveedor')
    ord_estado = models.CharField(max_length=1)
    class Meta:
        ordering = ["id"]

   

class Productos(models.Model):
   
    pro_nombre = models.CharField(max_length=30,verbose_name=u"Nombre:")
    pro_cantidad = models.IntegerField(verbose_name=u"Cantidad:")
    pro_precio = models.FloatField(verbose_name=u"Precio:")
    pro_ecg = models.CharField(max_length=75, blank=True,verbose_name=u"ECG:")
    pro_tarifa_iva = models.FloatField(verbose_name=u"IVA:")
    pro_ex = models.IntegerField(verbose_name=u"Cant Min:")
    pro_pvp = models.FloatField(verbose_name=u"Precio Venta Publico:")
    mar = models.ForeignKey(Categoria, blank=True, null=True,verbose_name=u"TIPO:")
    class Meta:
        ordering = ["id"]
    def __unicode__(self):
        return self.pro_nombre    

   

class Proveedor(models.Model):
   
    prov_ruc = models.CharField(max_length=13,verbose_name=u"RUC")
    prov_cedula = models.CharField(max_length=10,verbose_name=u"CEDULA")
    prov_nombre = models.CharField(max_length=30,verbose_name=u"NOMBRE")
    prov_representante = models.CharField(max_length=50,verbose_name=u"REPRESENTANTE")
    prov_direccion = models.CharField(max_length=80,verbose_name=u"DIRECCIÓN")
    prov_telefono = models.CharField(max_length=10, blank=True,verbose_name=u"TELEFONO")
    ciu = models.ForeignKey(Ciudad, blank=True, null=True,verbose_name=u"CIUDAD")
    prov_estado = models.CharField(max_length=1, blank=True,verbose_name=u"ESTADO")
    class Meta:
        ordering = ["id"]
    def __unicode__(self):
        return self.prov_nombre




class Repuestos(models.Model):
    man = models.ForeignKey(Mantenimiento)
    pro = models.ForeignKey(Productos)
    rep_cantidad = models.IntegerField()
    class Meta:
        ordering = ["id"]


class Solicitudmantenimiento(models.Model):
 
    solm_fecha = models.DateField(verbose_name=u"Fecha")
    solm_falla = models.CharField(max_length=100,verbose_name=u"Falla")
    solm_observaciones = models.CharField(max_length=100, blank=True,verbose_name=u"Observacion")
    solm_abono = models.FloatField(verbose_name=u"Abono")
    solm_saldo = models.FloatField(verbose_name=u"Saldo")
    solm_total = models.FloatField(verbose_name=u"Total")
    solm_estado = models.CharField(max_length=1, blank=True,verbose_name=u"Estado")
    art = models.ForeignKey(Articulossegunda)
    cli = models.ForeignKey(Clientes, blank=True, null=True)
    class Meta:
        ordering = ["id"]
    

   
