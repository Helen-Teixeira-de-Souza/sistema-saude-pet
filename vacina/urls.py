from django.urls import path

from . import views

urlpatterns = [
    path("", views.vacina_list, name="vacina_list"),
    path("novo/", views.vacina_create, name="vacina_create"),
    path("<int:vacina_id>/", views.vacina_detail, name="vacina_detail"),
    path("<int:vacina_id>/editar/", views.vacina_update, name="vacina_update"),
    path("<int:vacina_id>/excluir/", views.vacina_delete, name="vacina_delete"),
]
