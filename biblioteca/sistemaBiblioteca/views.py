from django.shortcuts import render, redirect
from .forms import LibroFisicoForm, LibroDigitalForm
from .models import LibroFisico, LibroDigital

# Vista para manejar la carga de libros y formularios
def index(request):
    libros_fisicos = LibroFisico.objects.all()
    libros_digitales = LibroDigital.objects.all()
    
    form = None
    # Si la solicitud es un POST, manejar la creación del libro
    if request.method == 'POST':
        tipo_libro = request.POST.get('type')  # Obtener el tipo de libro de la selección
        if tipo_libro == 'fisico':
            form = LibroFisicoForm(request.POST)
        elif tipo_libro == 'digital':
            form = LibroDigitalForm(request.POST)
        
        if form and form.is_valid():
            form.save()
            return redirect('/')  # Redirigir a la página principal después de guardar el libro
    
    else:
        # Si la solicitud no es un POST, simplemente cargar los formularios vacíos según el tipo
        tipo_libro = request.GET.get('type')  # Obtener el tipo de libro desde los parámetros GET
        if tipo_libro == 'fisico':
            form = LibroFisicoForm()
        elif tipo_libro == 'digital':
            form = LibroDigitalForm()

        # Verificar si es una solicitud AJAX
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # Solo renderizar el formulario sin la página completa
            tipo_libro = request.GET.get('type')  # Obtener el tipo de libro desde los parámetros GET
            if tipo_libro == 'fisico':
                return render(request, 'formulario-fisico.html', {'form': form})
            elif tipo_libro == 'digital':
                return render(request, 'formulario-digital.html', {'form': form})

    # Renderizar la página principal con la lista de libros
    return render(request, 'base.html', {
        'libros_fisicos': libros_fisicos,
        'libros_digitales': libros_digitales,
        'form': form
    })
