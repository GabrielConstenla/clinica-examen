from django.db import models

# Create your models here.

TIPOUSUARIO = (
    ('PACIENTE', 'PACIENTE'),
    ('SECRETARIA', 'SECRETARIA'),
    ('MEDICO', 'MEDICO'),
)

ESPECIALIDAD = (
    ('MEDICINA INTERNA', 'MEDICINA INTERNA'),
    ('CIRUGIA GENERAL', 'CIRUGIA GENERAL'),
    ('PEDIATRIA', 'PEDIATRIA'),
)

class Paciente(models.Model):
    rut = models.CharField(max_length=8, primary_key=True)
    dv = models.CharField(max_length=1)
    nombreCompleto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    tipoUsuario = models.CharField(max_length=20, choices=TIPOUSUARIO)
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 50)
    def __str__(self):
        return self.nombreCompleto

class Secretaria(models.Model):
    rut = models.CharField(max_length=8, primary_key=True)
    dv = models.CharField(max_length=1)
    nombreCompleto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    tipoUsuario = models.CharField(max_length=20, choices=TIPOUSUARIO)
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 50)
    def __str__(self):
        return self.nombreCompleto

class Medico(models.Model):
    rut = models.CharField(max_length=8, primary_key=True)
    dv = models.CharField(max_length=1)
    nombreCompleto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    tipoUsuario = models.CharField(max_length=20, choices=TIPOUSUARIO)
    especialidad = models.CharField(max_length=50, choices=ESPECIALIDAD)
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 50)
    def __str__(self):
        return self.nombreCompleto

class HoraMedica(models.Model):
    idHora = models.AutoField(primary_key=True)
    medico = models.ManyToManyField( Medico )
    fecha = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.fecha

class Agenda(models.Model):
    idAgenda = models.AutoField(primary_key=True)
    medico = models.ManyToManyField( Medico )
    horas = models.ManyToManyField( HoraMedica )
    def __str__(self):
        return str(self.idAgenda)
