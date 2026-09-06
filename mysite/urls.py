from django.contrib import admin
from django.urls import include, path
from consulta import views as consulta_views

urlpatterns = [
    path('', consulta_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('pet/', include('pet.urls')),
    path('vacinacao/', include('vacinacao.urls')),
    path('vacina/', include('vacina.urls')),
    path('cirurgia/', include('cirurgia.urls')),
    path('medicamento/', include('medicamento.urls')),
    path('consultas/', include('consulta.urls')),
]
