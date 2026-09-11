from django.urls import path
from . import views

app_name = 'vacinacao'

urlpatterns = [
    path("", views.listar_vacinacoes, name="listar"),
    path("novo/", views.criar_vacinacao, name="criar"),
    path("<int:vacinacao_id>/", views.detalhar_vacinacao, name="detalhar"),
    path("<int:vacinacao_id>/editar/", views.editar_vacinacao, name="editar"),
    path("<int:vacinacao_id>/excluir/", views.excluir_vacinacao, name="excluir"),
]
