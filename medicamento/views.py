from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicamento
from .forms import MedicamentoForm
from datetime import date, timedelta

def listar_medicamentos(request):
    medicamentos = Medicamento.objects.select_related('pet', 'consulta').all()
    return render(request, 'medicamento/medicamento_list.html', {'medicamentos': medicamentos})

def detalhe_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    
    data_fim = medicamento.data_inicio + timedelta(days=medicamento.duracao_dias)
    hoje = date.today()
    status_tratamento = 'Concluído' if hoje > data_fim else 'Em andamento'
    
    context = {
        'medicamento': medicamento,
        'data_fim': data_fim,
        'status_tratamento': status_tratamento
    }
    return render(request, 'medicamento/medicamento_detail.html', context)

def criar_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicamento:listar')
    else:
        form = MedicamentoForm()
    return render(request, 'medicamento/medicamento_form.html', {'form': form, 'titulo': 'Cadastrar Medicamento'})

def editar_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('medicamento:detalhe', pk=pk)
    else:
        form = MedicamentoForm(instance=medicamento)
    return render(request, 'medicamento/medicamento_form.html', {'form': form, 'titulo': 'Editar Medicamento', 'medicamento': medicamento})

def deletar_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        medicamento.delete()
        return redirect('medicamento:listar')
    return render(request, 'medicamento/medicamento_confirm_delete.html', {'medicamento': medicamento})