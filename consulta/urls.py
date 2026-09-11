from django.urls import path
from . import views

app_name = 'consulta'

urlpatterns = [
    path('', views.listar_consultas, name='listar'),
    path('nova/', views.criar_consulta, name='criar'),
    path('<int:pk>/', views.detalhar_consulta, name='detalhar'),
    path('<int:pk>/editar/', views.editar_consulta, name='editar'),
    path('<int:pk>/excluir/', views.excluir_consulta, name='excluir'),
]
