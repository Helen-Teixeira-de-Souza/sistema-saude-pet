from django.urls import path
from . import views

urlpatterns = [
    path('', views.TutorListView.as_view(), name='tutor_list'),
    path('<int:pk>/', views.TutorDetailView.as_view(), name='tutor_detail'),
    path('novo/', views.TutorCreateView.as_view(), name='tutor_create'),
    path('<int:pk>/editar/', views.TutorUpdateView.as_view(), name='tutor_update'),
    path('<int:pk>/deletar/', views.TutorDeleteView.as_view(), name='tutor_delete'),
]