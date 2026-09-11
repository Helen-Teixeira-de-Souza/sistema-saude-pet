from django.urls import path
from . import views

app_name = 'exame'

urlpatterns = [
    path('', views.listar_exames, name='listar'),
    path('novo/', views.criar_exame, name='criar'),
    path('<int:pk>/', views.detalhar_exame, name='detalhar'),
    path('<int:pk>/editar/', views.editar_exame, name='editar'),
    path('<int:pk>/excluir/', views.excluir_exame, name='excluir'),
]