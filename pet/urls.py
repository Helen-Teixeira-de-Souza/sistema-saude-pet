from django.urls import path
from . import views

urlpatterns = [
    path('', views.pet_list, name='pet_list'),
    path('<int:pk>/', views.pet_detail, name='pet_detail'),
    path('novo/', views.pet_create, name='pet_create'),
    path('<int:pk>/editar/', views.pet_update, name='pet_update'),
    path('<int:pk>/deletar/', views.pet_delete, name='pet_delete'),

    path('<int:pet_pk>/vacinacao/', views.registrar_vacinacao, name='registrar_vacinacao'),
    path('<int:pet_pk>/consulta/', views.registrar_consulta, name='registrar_consulta'),
    path('<int:pet_pk>/exame/', views.registrar_exame, name='registrar_exame'),
    path('<int:pet_pk>/medicamento/', views.registrar_medicamento, name='registrar_medicamento'),
    path('<int:pet_pk>/cirurgia/', views.registrar_cirurgia, name='registrar_cirurgia'),
    path('avisos-vacinas/', views.avisos_vacinas, name='avisos_vacinas'),
]