from django.shortcuts import render, redirect, get_object_or_404
from .forms import LibroFisicoForm, LibroDigitalForm
from django.db.models import Q
from .models import LibroFisico, LibroDigital
from django.http import JsonResponse


def index(request):
    libros_fisicos = LibroFisico.objects.all()
    libros_digitales = LibroDigital.objects.all()

    form = None
    template = "base.html"

    if request.method == "POST":
        tipo_libro = request.POST.get("type")

        if tipo_libro == "fisico":
            form = LibroFisicoForm(request.POST)
            template = "formulario-fisico.html"
        elif tipo_libro == "digital":
            form = LibroDigitalForm(request.POST)
            template = "formulario-digital.html"
        else:
            form = None

        if form and form.is_valid():
            # Crear el objeto manualmente para garantizar compatibilidad con encapsulación
            form.save()
            return redirect("/")

<<<<<<< HEAD
    else:
        tipo_libro = request.GET.get("type")
=======
    else:from django import forms
from .models import LibroFisico, LibroDigital


class LibroFisicoForm(forms.ModelForm):
    class Meta:
        model = LibroFisico
        fields = [LibroFisico.get_titulo(), LibroFisico.get_autor(), LibroFisico.get_fecha(), LibroFisico.get_paginas()]
        widgets = {
            "titulo": forms.TextInput(
                attrs={"class": "input-field", "autocomplete": "off"}
            ),
            "autor": forms.TextInput(
                attrs={"class": "input-field", "autocomplete": "off"}
            ),
            "anio_publicacion": forms.DateInput(
                attrs={"class": "input-field", "type": "date", "autocomplete": "off"}
            ),
            "num_paginas": forms.NumberInput(
                attrs={"class": "input-field", "autocomplete": "off"}
            ),
        }


class LibroDigitalForm(forms.ModelForm):
    formatos_libros = [
        ('', '--Selecciona--'),
        ("pdf", "PDF"),
        ("epub", "EPUB"),
        ("mobi", "MOBI"),
        ("txt", "TXT"),
    ]

    class Meta:
        model = LibroDigital
        fields = [LibroDigital.get_titulo(), LibroDigital.get_autor(), LibroDigital.get_fecha(), LibroDigital.get_formato(), LibroDigital.get_size()]
        widgets = {
            "titulo": forms.TextInput(
                attrs={"class": "input-field", "autocomplete": "off"}
            ),
            "autor": forms.TextInput(
                attrs={"class": "input-field", "autocomplete": "off"}
            ),
            "anio_publicacion": forms.DateInput(
                attrs={"class": "input-field", "type": "date"}
            ),
            "formato": forms.Select(
                attrs={"class": "input-field", "autocomplete": "off"}
            ),
            "tamanio_mb": forms.NumberInput(
                attrs={"class": "input-field", "autocomplete": "off"}
            ),
        }

    formato = forms.ChoiceField(choices=formatos_libros)

        # Si la solicitud no es un POST, simplemente cargar los formularios vacíos según el tipo
        tipo_libro = request.GET.get(
            "type"
        )  # Obtener el tipo de libro desde los parámetros GET
>>>>>>> f10f742f6d1454857d1835752cabbd66fd5bf947
        if tipo_libro == "fisico":
            form = LibroFisicoForm()
            template = "formulario-fisico.html"
        elif tipo_libro == "digital":
            form = LibroDigitalForm()
            template = "formulario-digital.html"
        else:
            form = None

    return render(
        request,
        template,
        {
            "libros_fisicos": libros_fisicos,
            "libros_digitales": libros_digitales,
            "form": form,
        },
    )


def guardar_libro_fisico(request):
    if request.method == "POST":
        form = LibroFisicoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "redirect_url": "/"})  # Indicar la redirección
        else:
            return JsonResponse({"success": False, "errors": form.errors})
    return JsonResponse({"success": False, "message": "Método no permitido"})


def guardar_libro_digital(request):
    if request.method == "POST":
        form = LibroDigitalForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "redirect_url": "/"})  # Indicar la redirección
        else:
            return JsonResponse({"success": False, "errors": form.errors})
    return JsonResponse({"success": False, "message": "Método no permitido"})

def editar_libro(request, libro_id, tipo):
    if tipo == "fisico":
        libro = get_object_or_404(LibroFisico, id=libro_id)
        form_class = LibroFisicoForm
        template = "formulario-fisico.html"
    elif tipo == "digital":
        libro = get_object_or_404(LibroDigital, id=libro_id)
        form_class = LibroDigitalForm
        template = "formulario-digital.html"
    else:
        return redirect("/")

    if request.method == "POST":
        form = form_class(request.POST, instance=libro)
        if form and form.is_valid():
            form.save()  # Guardar el libro directamente
            return redirect("/")
        else:
            print(form.errors)
    else:
        form = form_class(instance=libro)

    return render(request, template, {"form": form, "libro": libro})


def eliminar_libro(request, libro_id, tipo):
    if tipo == "fisico":
        libro = get_object_or_404(LibroFisico, id=libro_id)
    elif tipo == "digital":
        libro = get_object_or_404(LibroDigital, id=libro_id)
    else:
        return redirect("/")

    if request.method == "POST":
        libro.delete()
        return redirect("/")

    return render(request, "confirmDelete.html", {"libro": libro})


def buscar_libros(request):
    query = request.GET.get("q", "")  # Obtener el término de búsqueda
    resultados_fisicos = []
    resultados_digitales = []

    if query:
        # Buscar en ambos modelos utilizando las propiedades
        resultados_fisicos = LibroFisico.objects.filter(
            Q(_titulo__icontains=query) | Q(_autor__icontains=query)
        )
        resultados_digitales = LibroDigital.objects.filter(
            Q(_titulo__icontains=query) | Q(_autor__icontains=query)
        )

    return render(
        request,
        "buscar_libros.html",
        {
            "query": query,
            "resultados_fisicos": resultados_fisicos,
            "resultados_digitales": resultados_digitales,
        },
    )
