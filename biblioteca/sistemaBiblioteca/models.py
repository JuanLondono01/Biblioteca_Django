from django.db import models

# Clase base abstracta para los libros
class Libro(models.Model):
    # Campos internos privados
    _titulo = models.CharField(max_length=200, db_column="titulo")
    _autor = models.CharField(max_length=100, db_column="autor")
    _anio_publicacion = models.DateField(db_column="anio_publicacion")

    # Getter y setter para 'titulo'
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    # Getter y setter para 'autor'
    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, value):
        self._autor = value

    # Getter y setter para 'anio_publicacion'
    @property
    def anio_publicacion(self):
        return self._anio_publicacion

    @anio_publicacion.setter
    def anio_publicacion(self, value):
        self._anio_publicacion = value

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
<<<<<<< HEAD
        abstract = True  # Clase abstracta para no crear una tabla 'Libro'

    def mostrar_info(self):
        return (
            f"Título: {self.titulo}, Autor: {self.autor}, Año de publicación: {self.anio_publicacion}"
        )

=======
        abstract = True  # Clase base abstracta para evitar que se cree una tabla "Libro"

    def mostrar_info(self):
        return f"Título: {self.get_titulo()}, Autor: {self.get_autor()}, Año de publicación: {self.get_fecha()}"
>>>>>>> f10f742f6d1454857d1835752cabbd66fd5bf947

# Modelo para libros físicos
class LibroFisico(Libro):
    _num_paginas = models.IntegerField()

    # Getter y setter para 'num_paginas'
    @property
    def num_paginas(self):
        return self._num_paginas

    @num_paginas.setter
    def num_paginas(self, paginas):
        self._num_paginas = paginas

    def set_paginas(self, paginas):
        self.num_paginas = paginas

    def get_paginas(self):
        return self.num_paginas

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Número de páginas: {self.get_paginas()}"

# Modelo para libros digitales
class LibroDigital(Libro):
    _formato = models.CharField(max_length=50)
    _tamanio_mb = models.FloatField()

    # Getter y setter para 'formato'
    @property
    def formato(self):
        return self._formato

    @formato.setter
    def formato(self, value):
        self._formato = value

    # Getter y setter para 'tamanio_mb'
    @property
    def tamanio_mb(self):
        return self._tamanio_mb

    @tamanio_mb.setter
    def tamanio_mb(self, value):
        self._tamanio_mb = value

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
