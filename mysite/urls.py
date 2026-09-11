from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

# View temporária para a home
def home_temporaria(request):
    return HttpResponse("<h1>Sistema Saúde Pet</h1><p>Em desenvolvimento. Acesse os módulos diretamente pelas URLs (ex: /consultas/, /vacinas/).</p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_temporaria, name='home'),
    path('pet/', include('pet.urls')),
    path('vacinacao/', include('vacinacao.urls')),
    path('vacina/', include('vacina.urls')),
    path('cirurgia/', include('cirurgia.urls')),
    path('medicamento/', include('medicamento.urls')),
    path('consultas/', include('consulta.urls')),
]
