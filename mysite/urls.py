from django.contrib import admin
from django.urls import include, path
from consulta import views as consulta_views
# Usando consulta como página inicial TEMPORARIAMENTE

urlpatterns = [
    path('', consulta_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('consultas/', include('consulta.urls')),
]