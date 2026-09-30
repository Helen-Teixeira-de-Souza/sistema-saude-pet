from django.urls import path
from . import views

app_name = 'vacinacao'

urlpatterns = [
    path("", views.listar_vacinacoes, name="listar"),
    path("novo/", views.criar_vacinacao, name="criar"),
    path("<int:pk>/", views.detalhar_vacinacao, name="detalhar"),
    path("<int:pk>/editar/", views.editar_vacinacao, name="editar"),
    path("<int:pk>/excluir/", views.excluir_vacinacao, name="excluir"),
]
