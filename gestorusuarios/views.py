from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth.models import Permission

# Create your views here.
@login_required
def listarPersonal(request):
	personas = Usuarios.objects.all()
	return render(request, 'listar-empleados.html', {'personas':personas})

@login_required
def guardarPersona(request):
	form = PersonalForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(listarPersonal)
	return render(request, 'editar-empleado.html', {'form':form})

@login_required
def editarPersona(request, id):
	persona = get_object_or_404(Usuarios, pk=id)
	form = PersonalForm(request.POST or None, instance=persona)
	if form.is_valid():
		form.save()
		return redirect(listarPersonal)
	return render(request, 'editar-empleado.html', {'form':form})

@login_required
def eliminarPersona(request, id):
	persona = get_object_or_404(Usuarios, pk=id)
	if request.method == 'POST':
		persona.delete()
		return redirect(listarPersonal)
	return render(request, 'confirm-empleado.html', {'persona':persona})