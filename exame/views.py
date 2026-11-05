from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Exame
from .forms import ExameForm

@login_required
def listar_exames(request):
    exames = Exame.objects.select_related('pet', 'consulta').all()
    return render(request, 'exame/exame_list.html', {'exames': exames})

@login_required
def detalhar_exame(request, pk):
    exame = get_object_or_404(Exame, pk=pk)
    return render(request, 'exame/exame_detail.html', {'exame': exame})

@permission_required('exame.add_exame', login_url='/login/')
@login_required
def criar_exame(request):
    if request.method == 'POST':
        form = ExameForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Exame cadastrado com sucesso!')
            return redirect('exame:listar')
        else:
            messages.error(request, 'Erro ao cadastrar o exame. Verifique os dados informados.')
    else:
        form = ExameForm()
    return render(request, 'exame/exame_form.html', {'form': form, 'titulo': 'Cadastrar Exame'})

@permission_required('exame.change_exame', login_url='/login/')
@login_required
def editar_exame(request, pk):
    exame = get_object_or_404(Exame, pk=pk)

    # Verifica se passou de 30 dias da data de cadastro (RN001)
    dias_decorridos = (timezone.now().date() - exame.data).days
        
    if dias_decorridos > 30:
        messages.error(request, 'Operação negada: registros com mais de 30 dias não podem ser alterados ou excluídos por razões de segurança.')
        return redirect('exame:listar')

    if request.method == 'POST':
        form = ExameForm(request.POST, instance=exame)
        if form.is_valid():
            exame =form.save()
            messages.success(request, 'Exame atualizado com sucesso!')
            return redirect('exame:detalhar', pk=exame.pk)
        else:
            messages.error(request, 'Erro ao atualizar o exame. Verifique os dados informados.')
    else:
        form = ExameForm(instance=exame)
    return render(request, 'exame/exame_form.html', {'form': form, 'exame': exame})

@permission_required('exame.delete_exame', login_url='/login/')
@login_required
def excluir_exame(request, pk):
    exame = get_object_or_404(Exame, pk=pk)

    # Verifica se passou de 30 dias da data de cadastro (RN001)
    dias_decorridos = (timezone.now().date() - exame.data).days
        
    if dias_decorridos > 30:
        messages.error(request, 'Operação negada: registros com mais de 30 dias não podem ser alterados ou excluídos por razões de segurança.')
        return redirect('exame:listar')
    
    if request.method == 'POST':
        exame.delete()
        messages.warning(request, 'O registro de exame foi removido do histórico.')
        return redirect('exame:listar')
    return render(request, 'exame/exame_confirm_delete.html', {'exame': exame})