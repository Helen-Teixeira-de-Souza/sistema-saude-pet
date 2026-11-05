from django.urls import path
from . import views

app_name = 'pet'

urlpatterns = [
    path('', views.pet_list, name='listar'),
    path('<int:pk>/', views.pet_detail, name='detalhar'),
    path('novo/', views.pet_create, name='criar'),
    path('<int:pk>/editar/', views.pet_update, name='editar'),
    path('<int:pk>/excluir/', views.pet_delete, name='excluir'),
]
