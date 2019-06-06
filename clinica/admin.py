from django.contrib import admin
from .models import Paciente, Secretaria, Medico, Agenda, HoraMedica

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Secretaria)
admin.site.register(Medico)
admin.site.register(Agenda)
admin.site.register(HoraMedica)
