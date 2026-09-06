from django.urls import path

from . import views

urlpatterns = [
    path("", views.vacinacao_list, name="vacinacao_list"),
    path("novo/", views.vacinacao_create, name="vacinacao_create"),
    path("<int:vacinacao_id>/", views.vacinacao_detail, name="vacinacao_detail"),
    path("<int:vacinacao_id>/editar/", views.vacinacao_update, name="vacinacao_update"),
    path("<int:vacinacao_id>/excluir/", views.vacinacao_delete, name="vacinacao_delete"),
]
