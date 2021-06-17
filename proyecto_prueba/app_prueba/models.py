from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class Vehiculo(models.Model):

    vin = models.CharField(max_length=17, default='')
    patente = models.CharField(
        max_length=6, default='')
    año = models.CharField(max_length=4, default='', validators=[
        RegexValidator(r'^\d{1,10}$')])
    fecha = models.DateField(blank=True, null=True)
    marca = models.CharField(max_length=150, default='')
    modelo = models.CharField(max_length=150, default='')

    def __str__(self):

        return self.marca + ' ' + self.modelo + ' - ' + self.patente
