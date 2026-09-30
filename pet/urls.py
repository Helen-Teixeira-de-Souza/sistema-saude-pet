from django.urls import path
from . import views

app_name = 'pet'

urlpatterns = [
    path('', views.listar_pets, name='listar'),
    path('<int:pk>/', views.detalhar_pet, name='detalhar'),
    path('novo/', views.criar_pet, name='criar'),
    path('<int:pk>/editar/', views.editar_pet, name='editar'),
    path('<int:pk>/deletar/', views.excluir_pet, name='excluir'),
]