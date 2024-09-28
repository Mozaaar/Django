from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=70)
    telefono = models.CharField(max_length=60)
class Envio(models.Model):
    id_envio = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=70)
    telefono = models.CharField(max_length=60)
class Realiza(models.Model):
    id_realiza = models.CharField(max_length=10, primary_key=True)
    
class Factura(models.Model):
    id_factura = models.CharField(max_length=10, primary_key=True)
    fecha_emision = models.DateField()
    monto_t = models.FloatField()
class Paquete(models.Model):
    id_paquete = models.CharField(max_length=10, primary_key=True)
    peso =  models.FloatField(help_text="Peso en kilogramos")
    dimensiones = models.TextField(max_length=20,help_text="longitud, ancho, altiura") 
    contenido = models.CharField(max_length=10)
class Envio_paq(models.Model):
    id_enviopaq = models.CharField(max_length=10, primary_key=True)
 
class Transportista(models.Model):
    id_tra = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=20)
    telefono = models.CharField(max_length=10)
class Sucursal(models.Model):
    id_sucursal = models.CharField(max_length=10)
    direccion = models.CharField(max_length=70)
    telefono = models.CharField(max_length=60)
