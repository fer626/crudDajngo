from django.urls import path
from gestorusuarios.views import listarPersonal, guardarPersona, editarPersona, eliminarPersona

urlpatterns = [
    path('', listarPersonal, name="listar"),
    path('nuevo/', guardarPersona, name="guardar"),
    path('editar/<int:id>', editarPersona, name="editar"),
    path('eliminar/<int:id>', eliminarPersona, name='eliminar'),
]