
from django.urls import path
from django.views.generic import TemplateView

from .views import (
    index,
    primer_template,
    template_raw,
    kiko,
    db_interact,
    form_test,
    conversor_monedas,
    ConversorCBV, ConversorNew, PrimerTemplateCBV, ConversorCBVTWO, lista_deudores, create_deudor, detail_deudor,
    update_deudor, delete_deudor
)


urlpatterns = [
    path('question/', db_interact, name='questions'),
    path('', kiko, name='kiko'),
    path('', index, name='index'),
    path('template/', primer_template, name='primer_template'),
    # signature de path(ruta: str, view: funcion, name: str)
    # ruta: puede ser cualquiera que tu quieras, eso lo defines tu
    path('diego/', template_raw, name='template_raw'),
    path('google/', form_test, name='google_form'),
    # 2. Registrar la ruta
    path('conversor/', conversor_monedas, name='conversor'),
    # 2. register view
    path('conversor_refactor/', ConversorCBV.as_view(), name='conversor_cbv'),
    # 2.
    path('conversor_new/', ConversorNew.as_view(), name='conversor_new'),
    # 2.
    path('index_new/', PrimerTemplateCBV.as_view(), name='index_new'),

    path('index_new_two/', TemplateView.as_view(template_name='polls/index.html'), name='index_pass'),

    # 2l
    path('conversor_cbv/', ConversorCBVTWO.as_view(), name='conversor_cbv_two'),

    path('deudores/', lista_deudores, name='lista_deudores'),
    path('deudores/new/', create_deudor, name='create_deudor'),
    path('deudores/<int:id>/', detail_deudor, name='detail_deudor'),
    path('deudores/<int:id>/update/', update_deudor, name='update_deudor'),
    path('deudores/<int:id>/delete/', delete_deudor, name='delete_deudor'),
]
