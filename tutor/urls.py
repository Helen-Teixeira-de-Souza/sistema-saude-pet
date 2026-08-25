from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.tutor_detail, name='tutor_detail'),
    path('novo/', views.tutor_create, name='tutor_create'),
    path('<int:pk>/editar/', views.tutor_update, name='tutor_update'),
    path('<int:pk>/deletar/', views.tutor_delete, name='tutor_delete'),
]