from django import forms
from .models import LibroFisico, LibroDigital

class LibroFisicoForm(forms.ModelForm):
    class Meta:
        model = LibroFisico
        fields = ['titulo', 'autor', 'anio_publicacion', 'num_paginas']  # Usar los nombres de campo correctos
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
        fields = ['titulo', 'autor', 'anio_publicacion', 'formato', 'tamanio_mb']  # Usar los nombres de campo correctos
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