from django.shortcuts import render, redirect, get_object_or_404
from .models import Consulta
from .forms import ConsultaForm

# Listar todas as consultas
def listar_consultas(request):
    consultas = Consulta.objects.select_related('pet', 'profissional').all()
    return render(request, 'consulta/consulta_list.html', {'consultas': consultas})

# Exibir detalhes da consulta
def detalhar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    return render(request, 'consulta/consulta_detail.html', {'consulta': consulta})

# Criar uma nova consulta
def criar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consulta:listar_consultas')
    else:
        form = ConsultaForm()
    return render(request, 'consulta/consulta_form.html', {'form': form, 'titulo': 'Agendar Consulta'})

# Editar uma consulta existente
def editar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('consulta:detalhar_consulta', pk=pk)
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'consulta/consulta_form.html', {'form': form, 'titulo': 'Editar Consulta'})

# Excluir uma consulta
def excluir_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == 'POST':
        consulta.delete()
        return redirect('consulta:listar_consultas')
    return render(request, 'consulta/consulta_confirm_delete.html', {'consulta': consulta})