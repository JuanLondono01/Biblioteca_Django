from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("crear_fisico/", views.crear_libro_fisico, name="crear_fisico"),
    path("crear_digital/", views.crear_libro_digital, name="crear_digital"),
]