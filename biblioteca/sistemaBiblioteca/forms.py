from django import forms
from .models import LibroFisico, LibroDigital

class LibroFisicoForm(forms.ModelForm):
    titulo = forms.CharField(max_length=200, label="Titulo")
    autor = forms.CharField(max_length=100, label="Autor")
    anio_publicacion = forms.DateField(
        label="Fecha de publicacion", widget=forms.DateInput(attrs={"type": "date"})
    )
    num_paginas = forms.IntegerField(label="Numero de Paginas")

    class Meta:
        model = LibroFisico
<<<<<<< HEAD
        fields = ["titulo", "autor", "anio_publicacion", "num_paginas"]

    def __init__(self, *args, **kwargs):
        # Usa las propiedades para inicializar los valores del formulario
        instance = kwargs.get("instance")
        if instance:
            initial = kwargs.setdefault("initial", {})
            initial["titulo"] = instance._titulo
            initial["autor"] = instance._autor
            initial["anio_publicacion"] = instance._anio_publicacion
            initial["num_paginas"] = instance._num_paginas
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Usa las propiedades para guardar los valores
        instance.titulo = self.cleaned_data["titulo"]
        instance.autor = self.cleaned_data["autor"]
        instance.anio_publicacion = self.cleaned_data["anio_publicacion"]
        instance.num_paginas = self.cleaned_data["num_paginas"]
        if commit:
            instance.save()
        return instance
=======
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
>>>>>>> f10f742f6d1454857d1835752cabbd66fd5bf947



class LibroDigitalForm(forms.ModelForm):
    FORMATO_OPCIONES = [
        ("", "--Selecciona--"),
        ("PDF", "PDF"),
        ("EPUB", "EPUB"),
        ("MOBI", "MOBI"),
        ("AZW", "AZW (Kindle)"),
        ("OTRO", "Otro"),
    ]

    titulo = forms.CharField(max_length=200, label="Titulo")
    autor = forms.CharField(max_length=100, label="Autor")
    anio_publicacion = forms.DateField(
        label="Fecha de publicacion", widget=forms.DateInput(attrs={"type": "date"})
    )
    formato = forms.ChoiceField(
        choices=FORMATO_OPCIONES, label="Formato del Libro", widget=forms.Select()
    )
    tamanio_mb = forms.FloatField(label="Peso Del Libro (MB)")

    def __init__(self, *args, **kwargs):
        # Usa las propiedades para inicializar los valores del formulario
        instance = kwargs.get("instance")
        if instance:
            initial = kwargs.setdefault("initial", {})
            initial["titulo"] = instance._titulo
            initial["autor"] = instance._autor
            initial["anio_publicacion"] = instance._anio_publicacion
            initial["formato"] = instance._formato
            initial["tamanio_mb"] = instance._tamanio_mb
        super().__init__(*args, **kwargs)

    class Meta:
        model = LibroDigital
<<<<<<< HEAD
        fields = ["titulo", "autor", "anio_publicacion", "formato", "tamanio_mb"]

    def save(self, commit=True):
        # Sobrescribir save para usar propiedades
        instance = super().save(commit=False)
        instance.titulo = self.cleaned_data["titulo"]
        instance.autor = self.cleaned_data["autor"]
        instance.anio_publicacion = self.cleaned_data["anio_publicacion"]
        instance.formato = self.cleaned_data["formato"]
        instance.tamanio_mb = self.cleaned_data["tamanio_mb"]

        if commit:
            instance.save()
        return instance
=======
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
>>>>>>> f10f742f6d1454857d1835752cabbd66fd5bf947
