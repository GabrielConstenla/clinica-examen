from django import forms
from .models import Paciente, Secretaria, Medico, Agenda, HoraMedica
from django.core.exceptions import ValidationError
from django.utils import timezone, datetime

class PacienteForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = Paciente
        fields = ["rut", "dv", "nombreCompleto","telefono","tipoUsuario","email","password"]


    def clean_rut(self):
        rut = self.cleaned_data["rut"]
        if len(rut) <= 9:
            raise ValidationError("Debe ingresar su rut sin puntos, guión ni dígito verificador")
        return rut

    def clean_nombreCompleto(self):
            nombreCompleto = self.cleaned_data["nombre"]
            if len(nombreCompleto.split(" ")) < 4 :
                raise ValidationError("Por favor ingresa tu nombre completo")
            return nombreCompleto

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if telefono.isalpha():
            raise ValidationError('El telefono no puede contener letras')
        elif len(telefono) <= 8:
            raise ValidationError("Ingresa un telefono con un 9 digitos")
        return telefono

    def clean_email(self):
        email = self.cleaned_data['correo']

        correo_base, proveedor = email.split("@")
        dominio, extension = proveedor.split(".")
        if not dominio == "gmail":
            raise ValidationError("Aqui se tiene que registrar con gmail.com")
        elif not extension == "com":
            raise ValidationError("Aqui se tiene que registrar con gmail.com")
        return correo

class SecretariaForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = Secretaria
        fields = ["rut", "dv", "nombreCompleto","telefono","tipoUsuario","email","password"]


    def clean_rut(self):
        rut = self.cleaned_data["rut"]
        if len(rut) <= 9:
            raise ValidationError("Debe ingresar su rut sin puntos, guión ni dígito verificador")
        return rut

    def clean_nombreCompleto(self):
            nombreCompleto = self.cleaned_data["nombre"]
            if len(nombreCompleto.split(" ")) < 4 :
                raise ValidationError("Por favor ingresa tu nombre completo")
            return nombreCompleto

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if telefono.isalpha():
            raise ValidationError('El telefono no puede contener letras')
        elif len(telefono) <= 8:
            raise ValidationError("Ingresa un telefono con un 9 digitos")
        return telefono

    def clean_email(self):
        email = self.cleaned_data['correo']

        correo_base, proveedor = email.split("@")
        dominio, extension = proveedor.split(".")
        if not dominio == "gmail":
            raise ValidationError("Aqui se tiene que registrar con gmail.com")
        elif not extension == "com":
            raise ValidationError("Aqui se tiene que registrar con gmail.com")
        return correo

class MedicoForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = Medico
        fields = ["rut", "dv", "nombreCompleto","telefono","tipoUsuario","especialidad","email","password"]


    def clean_rut(self):
        rut = self.cleaned_data["rut"]
        if len(rut) <= 9:
            raise ValidationError("Debe ingresar su rut sin puntos, guión ni dígito verificador")
        return rut

    def clean_nombreCompleto(self):
            nombreCompleto = self.cleaned_data["nombre"]
            if len(nombreCompleto.split(" ")) < 4 :
                raise ValidationError("Por favor ingrese su nombre completo")
            return nombreCompleto

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if telefono.isalpha():
            raise ValidationError('El telefono no puede contener letras')
        elif len(telefono) <= 8:
            raise ValidationError("Ingrese un teléfono con un 9 digitos")
        return telefono

    def clean_email(self):
        email = self.cleaned_data["correo"]

        correo_base, proveedor = email.split("@")
        dominio, extension = proveedor.split(".")
        if not dominio == "gmail":
            raise ValidationError("Aqui se tiene que registrar con gmail.com")
        elif not extension == "com":
            raise ValidationError("Aqui se tiene que registrar con gmail.com")
        return correo

class HoraMedicaForm(forms.ModelForm):
    class Meta:
        model = HoraMedica
        fields = ["idHora","medico","fecha"]

    def clean_fecha(self):
        fecha = self.cleaned_data["fecha"]

        if fecha <= datetime.datetime.now()
            raise ValidationError("La hora para agendar no puede ser menor a la fecha actual")
        return fecha
