from django.db import models
from datetime import datetime

# Create your models here.
class Patient(models.Model):
    name = models.CharField(
        max_length=30, 
        verbose_name='Nombre'
    )
    last_name_p = models.CharField(
        max_length=30, 
        verbose_name='Apellido Paterno'
    )
    last_name_m = models.CharField(
        max_length=30, 
        verbose_name='Apellido Materno'
    )
    ci = models.CharField(
        max_length=30,
        verbose_name='Carnet de Identidad'
    )
    age = models.CharField(
        max_length=3,
        verbose_name='Edad'
    )
    gender = models.CharField(
        max_length=9,
        verbose_name='Sexo'
    )
    origin = models.CharField(
        max_length=100,
        verbose_name='Centro de Salud'
    )
    date_creation = models.DateTimeField(auto_now=True)
    date_updated = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        db_table = 'Patient'
        ordering = ['id']
    

