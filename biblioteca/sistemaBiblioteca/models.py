from django.db import models

# Clase base abstracta para los libros
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    anio_publicacion = models.DateField()

    # Métodos de acceso (getters y setters)
    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_titulo(self):
        return self.titulo

    def set_autor(self, autor):
        self.autor = autor

    def get_autor(self):
        return self.autor

    def set_fecha(self, fecha):
        self.anio_publicacion = fecha

    def get_fecha(self):
        return self.anio_publicacion

    class Meta:
        abstract = True  # Clase base abstracta para evitar que se cree una tabla "Libro"

    def mostrar_info(self):
        return f"Título: {self.get_titulo()}, Autor: {self.get_autor()}, Año de publicación: {self.get_fecha()}"

# Modelo para libros físicos
class LibroFisico(Libro):
    num_paginas = models.IntegerField()

    def set_paginas(self, paginas):
        self.num_paginas = paginas

    def get_paginas(self):
        return self.num_paginas

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Número de páginas: {self.get_paginas()}"

# Modelo para libros digitales
class LibroDigital(Libro):
    formato = models.CharField(max_length=50)
    tamanio_mb = models.FloatField()

    def set_formato(self, formato):
        self.formato = formato

    def get_formato(self):
        return self.formato

    def set_size(self, size):
        self.tamanio_mb = size

    def get_size(self):
        return self.tamanio_mb

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Tamaño: {self.get_size()} MB, Formato: {self.get_formato()}"
