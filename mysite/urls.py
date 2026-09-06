from django.contrib import admin
from django.urls import include, path
from consulta import views as consulta_views
# Usando consulta como página inicial TEMPORARIAMENTE

urlpatterns = [
    path('', consulta_views.home, name='home'),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('pet/', include('pet.urls')),
    path('vacinacao/', include('vacinacao.urls')),
    path('vacina/', include('vacina.urls')),
    path('cirurgia/', include('cirurgia.urls')),
    path('medicamento/', include('medicamento.urls')),
=======
    path('consultas/', include('consulta.urls')),
>>>>>>> 25fb0ba02f8af4adb3414067a2d3773ccd0f07d1
]