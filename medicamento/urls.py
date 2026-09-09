from django.urls import path
from . import views

app_name = 'medicamento'

urlpatterns = [
    path('', views.listar_medicamentos, name='listar'),
    path('novo/', views.criar_medicamento, name='criar'),
    path('<int:pk>/', views.detalhe_medicamento, name='detalhe'),
    path('<int:pk>/editar/', views.editar_medicamento, name='editar'),
    path('<int:pk>/deletar/', views.deletar_medicamento, name='deletar'),
]