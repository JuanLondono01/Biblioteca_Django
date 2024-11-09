from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    anio_publicacion = models.IntegerField()

    class Meta:
        abstract = True  # Clase base abstracta para que no se cree una tabla "Libro"

    def mostrar_info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año de publicación: {self.anio_publicacion}"


# Modelo para libros físicos
class LibroFisico(Libro):
    num_paginas = models.IntegerField()

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Número de páginas: {self.num_paginas}"


# Modelo para libros digitales
class LibroDigital(Libro):
    formato = models.CharField(max_length=50)
    tamanio_mb = models.FloatField()

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Tamaño: {self.tamanio_mb} MB, Formato: {self.formato}"
