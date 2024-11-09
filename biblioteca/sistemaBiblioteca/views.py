from django.shortcuts import render, redirect
from .forms import LibroFisicoForm, LibroDigitalForm
from .models import LibroFisico, LibroDigital

# Create your views here.
def index(request):
    libros_fisicos = LibroFisico.objects.all()
    libros_digitales = LibroDigital.objects.all()
    
    # Pasar los libros al contexto
    return render(request, 'base.html', {
        'libros_fisicos': libros_fisicos,
        'libros_digitales': libros_digitales,
    })



def crear_libro_fisico(request):
    if request.method == 'POST':
        form = LibroFisicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = LibroFisicoForm()
    return render(request, 'crear_fisico.html', {'form': form})


def crear_libro_digital(request):
    if request.method == 'POST':
        form = LibroDigitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirige a una vista que liste los libros
    else:
        form = LibroDigitalForm()
    return render(request, 'crear_digital.html', {'form': form})