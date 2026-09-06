from django.urls import path
from . import views

app_name = 'consulta'

urlpatterns = [
    path('', views.listar_consultas, name='listar'),
    path('<int:pk>/', views.detalhe_consulta, name='detalhe'),
    path('nova/', views.criar_consulta, name='criar'),
    path('<int:pk>/editar/', views.editar_consulta, name='editar'),
    path('<int:pk>/deletar/', views.deletar_consulta, name='deletar'),
]