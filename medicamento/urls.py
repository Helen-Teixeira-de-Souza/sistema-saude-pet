from django.urls import path

from . import views

urlpatterns = [
    path("", views.medicamento_list, name="medicamento_list"),
    path("novo/", views.medicamento_create, name="medicamento_create"),
    path("<int:medicamento_id>/", views.medicamento_detail, name="medicamento_detail"),
    path("<int:medicamento_id>/editar/", views.medicamento_update, name="medicamento_update"),
    path("<int:medicamento_id>/excluir/", views.medicamento_delete, name="medicamento_delete"),
]
