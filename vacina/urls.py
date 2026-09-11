from django.urls import path
from . import views

app_name = 'vacina'

urlpatterns = [
    path("", views.listar_vacina, name="listar"),
    path("novo/", views.criar_vacina, name="criar"),
    path("<int:vacina_id>/", views.detalhar_vacina, name="detalhar"),
    path("<int:vacina_id>/editar/", views.editar_vacina, name="editar"),
    path("<int:vacina_id>/excluir/", views.excluir_vacina, name="excluir"),
]
