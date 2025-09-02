from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import EstudianteForm

def formulario_estudiante(request):
    form = EstudianteForm()
    return render(request, 'formulario_estudiante.html', {'form': form})
