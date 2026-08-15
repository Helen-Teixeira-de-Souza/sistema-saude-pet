from django.urls import path
from . import views  

urlpatterns = [
   
    path('consultas/nova/', views.consulta_create, name='consulta_create'),
    path('consultas/<int:pk>/editar/', views.consulta_update, name='consulta_update'),
    path('consultas/<int:pk>/deletar/', views.consulta_delete, name='consulta_delete'),

    
    path('vacinas/nova/', views.vacina_create, name='vacina_create'),
    path('vacinas/<int:pk>/editar/', views.vacina_update, name='vacina_update'),
    path('vacinas/<int:pk>/deletar/', views.vacina_delete, name='vacina_delete'),

    
    path('cirurgias/nova/', views.cirurgia_create, name='cirurgia_create'),
    path('cirurgias/<int:pk>/editar/', views.cirurgia_update, name='cirurgia_update'),
    path('cirurgias/<int:pk>/deletar/', views.cirurgia_delete, name='cirurgia_delete'),

    path('avisos-vacinas/', views.avisos_vacinas, name='avisos_vacinas'),
]