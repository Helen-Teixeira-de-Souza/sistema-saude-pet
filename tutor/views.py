from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Consulta  # Certifique-se de que o modelo Consulta existe em clinica/models.py

class ConsultaListView(ListView):
    model = Consulta
    template_name = 'clinica/consulta_list.html'
    context_object_name = 'consultas'

class ConsultaCreateView(CreateView):
    model = Consulta
    fields = ['tutor', 'data', 'motivo']  # Ajuste os campos conforme seu modelo Consulta
    template_name = 'clinica/consulta_form.html'
    success_url = reverse_lazy('consulta_list')

class ConsultaUpdateView(UpdateView):
    model = Consulta
    fields = ['tutor', 'data', 'motivo']
    template_name = 'clinica/consulta_form.html'
    success_url = reverse_lazy('consulta_list')

class ConsultaDeleteView(DeleteView):
    model = Consulta
    template_name = 'clinica/consulta_confirm_delete.html'
    success_url = reverse_lazy('consulta_list')
