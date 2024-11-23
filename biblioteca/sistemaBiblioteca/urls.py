from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("editar/<int:libro_id>/<str:tipo>/", views.editar_libro, name="editar_libro"),
    path("eliminar/<int:libro_id>/<str:tipo>/", views.eliminar_libro, name="eliminar_libro"),
    path("buscar/", views.buscar_libros, name="buscar_libros"),
    path('guardar_libro_fisico/', views.guardar_libro_fisico, name='guardar_libro_fisico'),
    path('guardar_libro_digital/', views.guardar_libro_digital, name='guardar_libro_digital'),
]
# 