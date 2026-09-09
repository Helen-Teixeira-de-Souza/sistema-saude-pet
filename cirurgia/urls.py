from django.urls import path

from . import views

urlpatterns = [
    path("", views.listar_cirurgia, name="cirurgia_list"),
    path("novo/", views.criar_cirurgia, name="cirurgia_create"),
    path("<int:cirurgia_id>/", views.detalhe_cirurgia, name="cirurgia_detail"),
    path("<int:cirurgia_id>/editar/", views.editar_cirurgia, name="cirurgia_update"),
    path("<int:cirurgia_id>/excluir/", views.deletar_cirurgia, name="cirurgia_delete"),
]
