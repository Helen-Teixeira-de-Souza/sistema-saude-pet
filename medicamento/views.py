from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Medicamento
from .forms import MedicamentoForm
from datetime import date, timedelta
from django.utils import timezone

@login_required
def listar_medicamentos(request):
    medicamentos = Medicamento.objects.select_related('pet', 'consulta').all()
    return render(request, 'medicamento/medicamento_list.html', {'medicamentos': medicamentos})

@login_required
def detalhar_medicamento(request, pk):
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

@permission_required('medicamento.add_medicamento', login_url='/login/')
@login_required
def criar_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicamento cadastrado com sucesso!')
            return redirect('medicamento:listar')
        else:
            messages.error(request, 'Erro ao cadastrar o medicamento. Verifique os dados informados.')
    else:
        form = MedicamentoForm()
    return render(request, 'medicamento/medicamento_form.html', {'form': form, 'titulo': 'Cadastrar Medicamento'})

@permission_required('medicamento.change_medicamento', login_url='/login/')
@login_required
def editar_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)

    # Verifica se passou de 30 dias da data de cadastro (RN001)
    dias_decorridos = (timezone.now().date() - medicamento.data).days
            
    if dias_decorridos > 30:
        messages.error(request, 'Operação negada: registros com mais de 30 dias não podem ser alterados ou excluídos por razões de segurança.')
        return redirect('medicamento:listar')

    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            medicamento = form.save()
            messages.success(request, 'Medicamento atualizado com sucesso!')
            return redirect('medicamento:detalhar', pk=pk)
        else:
            messages.error(request, 'Erro ao atualizar o medicamento. Verifique os dados informados.')
    else:
        form = MedicamentoForm(instance=medicamento)

    return render(request, 'medicamento/medicamento_form.html', {'form': form, 'medicamento': medicamento})

@permission_required('medicamento.delete_medicamento', login_url='/login/')
@login_required
def excluir_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)

    # Verifica se passou de 30 dias da data de cadastro (RN001)
    dias_decorridos = (timezone.now().date() - medicamento.data).days
            
    if dias_decorridos > 30:
        messages.error(request, 'Operação negada: registros com mais de 30 dias não podem ser alterados ou excluídos por razões de segurança.')
        return redirect('medicamento:listar')
    
    if request.method == 'POST':
        medicamento.delete()
        messages.warning(request, f'O medicamento "{medicamento.nome}" foi removido do sistema.')
        return redirect('medicamento:listar')
    return render(request, 'medicamento/medicamento_confirm_delete.html', {'medicamento': medicamento})