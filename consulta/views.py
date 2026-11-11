from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from pet.access import filtrar_por_tutor, permissao_ou_tutor, restringir_form
from .models import Consulta
from .forms import ConsultaForm

# Listar todas as consultas
@login_required
@permission_required('consulta.view_consulta')
def listar_consultas(request):
    consultas = filtrar_por_tutor(Consulta.objects.select_related('pet', 'profissional'), request.user)
    return render(request, 'consulta/consulta_list.html', {'consultas': consultas})

# Exibir detalhes da consulta
@login_required
@permission_required('consulta.view_consulta')
def detalhar_consulta(request, pk):
    consulta = get_object_or_404(filtrar_por_tutor(Consulta.objects.all(), request.user), pk=pk)
    return render(request, 'consulta/consulta_detail.html', {'consulta': consulta})

# Criar uma nova consulta
@login_required
@permission_required('consulta.add_consulta')
def criar_consulta(request):
    if request.method == 'POST':
        form = restringir_form(ConsultaForm(request.POST), request.user)
        if form.is_valid():
            consulta = form.save()
            messages.success(request, f'Consulta registrada com sucesso!')
            return redirect('consulta:listar')
        else:
            messages.error(request, 'Erro ao registrar a consulta. Verifique os dados informados.')
    else:
        form = restringir_form(ConsultaForm(), request.user)
    return render(request, 'consulta/consulta_form.html', {'form': form, 'titulo': 'Agendar Consulta'})

# Editar uma consulta existente
@login_required
@permission_required('consulta.change_consulta')
def editar_consulta(request, pk):
    consulta = get_object_or_404(filtrar_por_tutor(Consulta.objects.all(), request.user), pk=pk)

    # Verifica se passou de 30 dias da data de cadastro (RN001)
    dias_decorridos = (timezone.now().date() - consulta.data).days
        
    if dias_decorridos > 30:
        messages.error(request, 'Operação negada: registros com mais de 30 dias não podem ser alterados ou excluídos por razões de segurança.')
        return redirect('consulta:listar')
    
    if request.method == 'POST':
        form = restringir_form(ConsultaForm(request.POST, instance=consulta), request.user)
        if form.is_valid():
            consulta = form.save()
            messages.success(request, f'Consulta atualizada com sucesso!')
            return redirect('consulta:detalhar', pk=consulta.pk)
        else:
            messages.error(request, 'Erro ao atualizar a consulta. Verifique os dados informados.')
    else:
        form = restringir_form(ConsultaForm(instance=consulta), request.user)
    return render(request, 'consulta/consulta_form.html', {'form': form, 'consulta': consulta})


# Excluir uma consulta
@login_required
@permission_required('consulta.delete_consulta')
def excluir_consulta(request, pk):
    consulta = get_object_or_404(filtrar_por_tutor(Consulta.objects.all(), request.user), pk=pk)

    # Verifica se passou de 30 dias da data de cadastro (RN001)
    dias_decorridos = (timezone.now().date() - consulta.data).days
    
    if dias_decorridos > 30:
        messages.error(request, 'Operação negada: registros com mais de 30 dias não podem ser alterados ou excluídos por razões de segurança.')
        return redirect('consulta:listar')

    if request.method == 'POST':
        consulta.delete()
        messages.warning(request, 'O registro de consulta foi removido do histórico.')
        return redirect('consulta:listar')
    return render(request, 'consulta/consulta_confirm_delete.html', {'consulta': consulta})