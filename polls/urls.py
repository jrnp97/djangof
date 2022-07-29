
from django.urls import path
from .views import index, primer_template, template_raw, kiko, db_interact

urlpatterns = [
    path('question/', db_interact, name='questions'),
    path('', kiko, name='kiko'),
    path('', index, name='index'),
    path('template/', primer_template, name='primer_template'),
    # signature de path(ruta: str, view: funcion, name: str)
    # ruta: puede ser cualquiera que tu quieras, eso lo defines tu
    path('diego/', template_raw, name='template_raw'),
]
