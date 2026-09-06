from django.urls import path

from . import views

urlpatterns = [
    path("", views.cirurgia_list, name="cirurgia_list"),
    path("novo/", views.cirurgia_create, name="cirurgia_create"),
    path("<int:cirurgia_id>/", views.cirurgia_detail, name="cirurgia_detail"),
    path("<int:cirurgia_id>/editar/", views.cirurgia_update, name="cirurgia_update"),
    path("<int:cirurgia_id>/excluir/", views.cirurgia_delete, name="cirurgia_delete"),
]
