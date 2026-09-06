# Obs: revisar essa parte

from django.shortcuts import render, redirect, get_object_or_404
from .models import Consulta
from .forms import ConsultaForm

# consulta/views.py
from django.shortcuts import redirect

# View para redirecionar a home
def home(request):
    return redirect('consulta:listar')

# 1. List all consultations
def listar_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'consulta/consulta_list.html', {'consultas': consultas})

# 2. View consultation details
def detalhe_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    return render(request, 'consulta/consulta_detail.html', {'consulta': consulta})

# 3. Create a new consultation
def criar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consulta:listar')
    else:
        form = ConsultaForm()
    return render(request, 'consulta/consulta_form.html', {'form': form, 'titulo': 'Agendar Consulta'})

# 4. Edit an existing consultation
def editar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('consulta:detalhe', pk=pk)
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'consulta/consulta_form.html', {'form': form, 'titulo': 'Editar Consulta'})

# 5. Delete a consultation
def deletar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == 'POST':
        consulta.delete()
        return redirect('consulta:listar')
    return render(request, 'consulta/consulta_confirm_delete.html', {'consulta': consulta})