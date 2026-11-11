from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from pet.access import filtrar_por_tutor, permissao_ou_tutor, restringir_form
from .models import Exame
from .forms import ExameForm

@login_required
@permission_required('exame.view_exame')
def listar_exames(request):
    exames = filtrar_por_tutor(Exame.objects.select_related('pet', 'consulta'), request.user)
    return render(request, 'exame/exame_list.html', {'exames': exames})

@login_required
@permission_required('exame.view_exame')
def detalhar_exame(request, pk):
    exame = get_object_or_404(filtrar_por_tutor(Exame.objects.all(), request.user), pk=pk)
    return render(request, 'exame/exame_detail.html', {'exame': exame})

@login_required
@permission_required('exame.add_exame')
def criar_exame(request):
    if request.method == 'POST':
        form = restringir_form(ExameForm(request.POST), request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Exame cadastrado com sucesso!')
            return redirect('exame:listar')
        else:
            messages.error(request, 'Erro ao cadastrar o exame. Verifique os dados informados.')
    else:
        form = restringir_form(ExameForm(), request.user)
    return render(request, 'exame/exame_form.html', {'form': form, 'titulo': 'Cadastrar Exame'})

@login_required
@permission_required('exame.change_exame')
def editar_exame(request, pk):
    exame = get_object_or_404(filtrar_por_tutor(Exame.objects.all(), request.user), pk=pk)

    # Verifica se passou de 30 dias da data de cadastro (RN001)
    dias_decorridos = (timezone.now().date() - exame.data_realizacao).days
        
    if dias_decorridos > 30:
        messages.error(request, 'Operação negada: registros com mais de 30 dias não podem ser alterados ou excluídos por razões de segurança.')
        return redirect('exame:listar')

    if request.method == 'POST':
        form = restringir_form(ExameForm(request.POST, instance=exame), request.user)
        if form.is_valid():
            exame =form.save()
            messages.success(request, 'Exame atualizado com sucesso!')
            return redirect('exame:detalhar', pk=exame.pk)
        else:
            messages.error(request, 'Erro ao atualizar o exame. Verifique os dados informados.')
    else:
        form = restringir_form(ExameForm(instance=exame), request.user)
    return render(request, 'exame/exame_form.html', {'form': form, 'exame': exame})

@login_required
@permission_required('exame.delete_exame')
def excluir_exame(request, pk):
    exame = get_object_or_404(filtrar_por_tutor(Exame.objects.all(), request.user), pk=pk)

    # Verifica se passou de 30 dias da data de cadastro (RN001)
    dias_decorridos = (timezone.now().date() - exame.data_realizacao).days
        
    if dias_decorridos > 30:
        messages.error(request, 'Operação negada: registros com mais de 30 dias não podem ser alterados ou excluídos por razões de segurança.')
        return redirect('exame:listar')
    
    if request.method == 'POST':
        exame.delete()
        messages.warning(request, 'O registro de exame foi removido do histórico.')
        return redirect('exame:listar')
    return render(request, 'exame/exame_confirm_delete.html', {'exame': exame})