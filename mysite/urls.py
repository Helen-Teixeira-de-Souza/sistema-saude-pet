from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pet/', include('pet.urls')),
    path('vacinacao/', include('vacinacao.urls')),
    path('vacina/', include('vacina.urls')),
    path('cirurgia/', include('cirurgia.urls')),
    path('medicamento/', include('medicamento.urls')),
]