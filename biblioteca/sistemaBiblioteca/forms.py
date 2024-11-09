from django import forms
from .models import LibroFisico, LibroDigital


class LibroFisicoForm(forms.ModelForm):
    class Meta:
        model = LibroFisico
        fields = ["titulo", "autor", "anio_publicacion", "num_paginas"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "input-field"}),
            "autor": forms.TextInput(attrs={"class": "input-field"}),
            "anio_publicacion": forms.DateInput(
                attrs={"class": "input-field", "type": "date"}
            ),
            "num_paginas": forms.NumberInput(attrs={"class": "input-field"}),
        }


class LibroDigitalForm(forms.ModelForm):
    formatos_libros = [
        ("pdf", "PDF"),
        ("epub", "EPUB"),
        ("mobi", "MOBI"),
        ("txt", "TXT"),
    ]

    class Meta:
        model = LibroDigital
        fields = ["titulo", "autor", "anio_publicacion", "formato", "tamanio_mb"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "input-field"}),
            "autor": forms.TextInput(attrs={"class": "input-field"}),
            "anio_publicacion": forms.DateInput(
                attrs={"class": "input-field", "type": "date"}
            ),
            "formato": forms.Select(attrs={"class": "input-field"}),
            "tamanio_mb": forms.NumberInput(attrs={"class": "input-field"}),
        }

    formato = forms.ChoiceField(choices=formatos_libros)
