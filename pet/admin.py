from django.contrib import admin
from .models import Pet, Vacinacao, Consulta, Medicamento, Exame, Cirurgia

admin.site.register(Pet)
admin.site.register(Vacinacao)
admin.site.register(Consulta)
admin.site.register(Medicamento)
admin.site.register(Exame)
admin.site.register(Cirurgia)