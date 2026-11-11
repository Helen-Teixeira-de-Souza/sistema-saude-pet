from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from pet.access import filtrar_por_tutor, permissao_ou_tutor, restringir_form
from vacina.models import Vacina
from .models import AvisoVacinacao, Vacinacao
from .forms import VacinacaoForm

@login_required
def listar_vacinacoes(request):
    vacinacoes = filtrar_por_tutor(Vacinacao.objects.select_related("pet", "vacina"), request.user)
    return render(request, "vacinacao/vacinacao_list.html", {"vacinacao_list": vacinacoes})


@login_required
def detalhar_vacinacao(request, pk):
    vacinacao = get_object_or_404(filtrar_por_tutor(Vacinacao.objects.all(), request.user), pk=pk)
    return render(request, "vacinacao/vacinacao_detail.html", {"vacinacao": vacinacao})


@login_required
@permissao_ou_tutor('vacinacao.add_vacinacao')
def criar_vacinacao(request):
    if request.method == "POST":
        form = restringir_form(VacinacaoForm(request.POST), request.user)
        if form.is_valid():
            vacinacao = form.save()
            messages.success(request, f'Vacinação "{vacinacao.vacina.nome}" registrada para {vacinacao.pet.nome}!')
            return redirect("vacinacao:detalhar", pk=vacinacao.id)
        else:
            messages.error(request, 'Erro ao registrar a vacinação. Verifique os dados informados.')
    else:
        form = restringir_form(VacinacaoForm(), request.user)
    return render(request, "vacinacao/vacinacao_form.html", {"form": form, "sem_vacinas": not Vacina.objects.exists()})

@login_required
@permissao_ou_tutor('vacinacao.change_vacinacao')
def editar_vacinacao(request, pk):
    vacinacao = get_object_or_404(filtrar_por_tutor(Vacinacao.objects.all(), request.user), pk=pk)
    if request.method == "POST":
        form = restringir_form(VacinacaoForm(request.POST, instance=vacinacao), request.user)
        if form.is_valid():
            vacinacao = form.save()
            messages.success(request, f'Vacinação de {vacinacao.pet.nome} atualizada!')
            return redirect("vacinacao:detalhar", pk=vacinacao.id)
        else:
            messages.error(request, 'Erro ao atualizar. Corrija os campos abaixo.')
    else:
        form = restringir_form(VacinacaoForm(instance=vacinacao), request.user)
    return render(request, "vacinacao/vacinacao_form.html", {"form": form, "vacinacao": vacinacao, "sem_vacinas": not Vacina.objects.exists()})

@login_required
@permissao_ou_tutor('vacinacao.delete_vacinacao')
def excluir_vacinacao(request, pk):
    vacinacao = get_object_or_404(filtrar_por_tutor(Vacinacao.objects.all(), request.user), pk=pk)
    if request.method == "POST":
        descricao = f'{vacinacao.vacina.nome} de {vacinacao.pet.nome}'
        vacinacao.delete()
        messages.warning(request, f'A vacinação "{descricao}" foi removida do sistema.')
        return redirect("vacinacao:listar")
    return render(request, "vacinacao/vacinacao_confirm_delete.html", {"vacinacao": vacinacao})


@login_required
def listar_avisos(request):
    """Avisos de vacinação: o tutor vê só os dos seus pets; a equipe (staff) vê todos."""
    avisos = AvisoVacinacao.objects.select_related(
        'vacinacao__pet', 'vacinacao__vacina'
    ).filter(vacinacao__isnull=False)

    if not request.user.is_staff:
        avisos = avisos.filter(vacinacao__pet__tutor__pk=request.user.pk)

    context = {
        'avisos': avisos.order_by('data_aviso'),
        'hoje': date.today(),
    }
    return render(request, 'vacinacao/aviso_list.html', context)
