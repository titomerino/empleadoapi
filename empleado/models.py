from django.db import models


# Create your models here.
class Empleado(models.Model):

    TIPO_DOCUMENTO_OPCIONES = (
        (1, "Dui"),
        (2, "Nit"),
        (3, "Pasaporte"),
    )

    AREA = (
        (1, "Administracion"),
        (2, "Ventas"),
        (3, "Desarrollo"),
        (4, "Medicina"),
    )

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipo_documento = models.IntegerField(choices=TIPO_DOCUMENTO_OPCIONES, default=1)
    documento = models.CharField("Nº de documento", max_length=50)
    area = models.IntegerField(choices=AREA, default=1)

    def __str__(self):
        return self.nombre
