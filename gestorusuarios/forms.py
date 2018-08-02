from django import forms
from .models import *

class PersonalForm(forms.ModelForm):
	class Meta:
		model = Usuarios
		fields = [
			'nombre',
			'apellidos',
			'direccion',
			'estatus',
			'rol',
			'usuario',
			'fecha_nacimiento',
			'curp',
			'fecha_contratacion',
			'correo',
			'telefono',
			'celular',
		]
