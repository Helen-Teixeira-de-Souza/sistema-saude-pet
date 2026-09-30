from django.urls import path
from . import views

app_name = 'tutor'

urlpatterns = [
    path('', views.listar_tutores, name='listar'),
    path('<int:pk>/', views.detalhar_tutor, name='detalhar'),
    path('novo/', views.criar_tutor, name='criar'),
    path('<int:pk>/editar/', views.editar_tutor, name='editar'),
    path('<int:pk>/deletar/', views.excluir_tutor, name='excluir'),
]