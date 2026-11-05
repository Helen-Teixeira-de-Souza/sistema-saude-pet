from django.urls import path
from . import views

app_name = 'profissional'

urlpatterns = [
    path('', views.listar_profissionais, name='listar'),
    path('criar/', views.criar_profissional, name='criar'),
    path('detalhar/<int:pk>/', views.detalhar_profissional, name='detalhar'),
    path('editar/<int:pk>/', views.editar_profissional, name='editar'),
    path('excluir/<int:pk>/', views.excluir_profissional, name='excluir'),
]