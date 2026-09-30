from django.urls import path
from . import views

app_name = 'cirurgia'

urlpatterns = [
    path("", views.listar_cirurgias, name="listar"),
    path("novo/", views.criar_cirurgia, name="criar"),
    path("<int:pk>/", views.detalhar_cirurgia, name="detalhar"),
    path("<int:pk>/editar/", views.editar_cirurgia, name="editar"),
    path("<int:pk>/excluir/", views.excluir_cirurgia, name="excluir"),
]