from django.urls import path

from . import views

urlpatterns = [
    path("", views.listar_vacinacao, name="vacinacao_list"),
    path("novo/", views.criar_vacinacao, name="vacinacao_create"),
    path("<int:vacinacao_id>/", views.detalhe_vacinacao, name="vacinacao_detail"),
    path("<int:vacinacao_id>/editar/", views.editar_vacinacao, name="vacinacao_update"),
    path("<int:vacinacao_id>/excluir/", views.deletar_vacinacao, name="vacinacao_delete"),
]
