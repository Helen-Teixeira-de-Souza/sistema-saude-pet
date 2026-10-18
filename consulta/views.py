from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Consulta
from .forms import ConsultaForm

# Listar todas as consultas
@login_required
def listar_consultas(request):
    consultas = Consulta.objects.select_related('pet', 'profissional').all()
    return render(request, 'consulta/consulta_list.html', {'consultas': consultas})

# Exibir detalhes da consulta
@login_required
def detalhar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    return render(request, 'consulta/consulta_detail.html', {'consulta': consulta})

# Criar uma nova consulta
@permission_required('consulta.add_consulta', login_url='/login/')
@login_required
def criar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consulta:listar')
    else:
        form = ConsultaForm()
    return render(request, 'consulta/consulta_form.html', {'form': form, 'titulo': 'Agendar Consulta'})

# Editar uma consulta existente
@permission_required('consulta.change_consulta', login_url='/login/')
@login_required
def editar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)

    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            consulta = form.save()
            return redirect('consulta:detalhar', pk=consulta.pk)
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'consulta/consulta_form.html', {'form': form, 'consulta': consulta})

# Excluir uma consulta
@permission_required('consulta.delete_consulta', login_url='/login/')
@login_required
def excluir_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == 'POST':
        consulta.delete()
        return redirect('consulta:listar')
    return render(request, 'consulta/consulta_confirm_delete.html', {'consulta': consulta})