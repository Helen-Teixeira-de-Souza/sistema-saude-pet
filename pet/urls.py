from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.PetListView.as_view(), name='pet_list'),
    path('<int:pk>/', views.PetDetailView.as_view(), name='pet_detail'),
    path('novo/', views.PetCreateView.as_view(), name='pet_create'),
    path('<int:pk>/editar/', views.PetUpdateView.as_view(), name='pet_update'),
    path('<int:pk>/deletar/', views.PetDeleteView.as_view(), name='pet_delete'),
    
    
    path('<int:pet_pk>/vacina/nova/', views.registrar_vacinacao, name='registrar_vacinacao'),
    path('<int:pet_pk>/consulta/nova/', views.registrar_consulta, name='registrar_consulta'),
    path('<int:pet_pk>/exame/novo/', views.registrar_exame, name='registrar_exame'),
    path('<int:pet_pk>/medicamento/novo/', views.registrar_medicamento, name='registrar_medicamento'),
    path('<int:pet_pk>/cirurgia/nova/', views.registrar_cirurgia, name='registrar_cirurgia'),
    
    
    path('avisos/vacinas/', views.avisos_vacinas, name='avisos_vacinas'),
]