from django.urls import path

from . import views

urlpatterns = [
    path("", views.listar_vacina, name="vacina_list"),
    path("novo/", views.criar_vacina, name="vacina_create"),
    path("<int:vacina_id>/", views.detalhe_vacina, name="vacina_detail"),
    path("<int:vacina_id>/editar/", views.editar_vacina, name="vacina_update"),
    path("<int:vacina_id>/excluir/", views.deletar_vacina, name="vacina_delete"),
]
