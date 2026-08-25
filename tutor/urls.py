from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.TutorListView.as_view(), name='tutor_list'),
    path('<int:pk>/', views.TutorDetailView.as_view(), name='tutor_detail'),
    path('novo/', views.TutorCreateView.as_view(), name='tutor_create'),
    path('<int:pk>/editar/', views.TutorUpdateView.as_view(), name='tutor_update'),
    path('<int:pk>/deletar/', views.TutorDeleteView.as_view(), name='tutor_delete'),
=======
    path('<int:pk>/', views.tutor_detail, name='tutor_detail'),
    path('novo/', views.tutor_create, name='tutor_create'),
    path('<int:pk>/editar/', views.tutor_update, name='tutor_update'),
    path('<int:pk>/deletar/', views.tutor_delete, name='tutor_delete'),
>>>>>>> 69d85cd120c33d9eb80c9fb0b5e5f1b52e5271c9
]