from django.urls import path
from . import views

app_name = 'vacina'

urlpatterns = [
    path("", views.listar_vacinas, name="listar"),
    path("novo/", views.criar_vacina, name="criar"),
    path("<int:pk>/", views.detalhar_vacina, name="detalhar"),
    path("<int:pk>/editar/", views.editar_vacina, name="editar"),
    path("<int:pk>/excluir/", views.excluir_vacina, name="excluir"),
]
