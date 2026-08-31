from django.urls import path
from . import views

urlpatterns = [
    path('', views.pet_list, name='pet_list'),
    path('<int:pk>/', views.pet_detail, name='pet_detail'),
    path('novo/', views.pet_create, name='pet_create'),
    path('<int:pk>/editar/', views.pet_update, name='pet_update'),
    path('<int:pk>/deletar/', views.pet_delete, name='pet_delete'),
]