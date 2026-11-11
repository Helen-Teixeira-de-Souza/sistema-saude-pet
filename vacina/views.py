from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import ProtectedError
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vacina
from .forms import VacinaForm


@login_required(login_url='/login/')
def listar_vacinas(request):
    vacinas = Vacina.objects.all()
    return render(request, "vacina/vacina_list.html", {"vacina_list": vacinas})

@login_required(login_url='/login/')
def detalhar_vacina(request, pk):
    vacina = get_object_or_404(Vacina, pk=pk)
    return render(request, "vacina/vacina_detail.html", {"vacina": vacina})


@login_required(login_url='/login/')
def criar_vacina(request):
    if request.method == "POST":
        form = VacinaForm(request.POST)
        if form.is_valid():
            vacina = form.save()
            messages.success(request, f'Vacina "{vacina.nome}" cadastrada com sucesso!')
            return redirect("vacina:listar")
        else:
            messages.error(request, 'Erro ao cadastrar a vacina. Verifique os dados informados.')
    else:
        form = VacinaForm()
    return render(request, "vacina/vacina_form.html", {"form": form})


@staff_member_required(login_url='/login/')
def editar_vacina(request, pk):
    vacina = get_object_or_404(Vacina, pk=pk)
    if request.method == "POST":
        form = VacinaForm(request.POST, instance=vacina)
        if form.is_valid():
            vacina = form.save()
            messages.success(request, f'Dados da vacina "{vacina.nome}" atualizados!')
            return redirect("vacina:detalhar", pk=vacina.pk)
        else:
            messages.error(request, 'Erro ao atualizar. Corrija os campos abaixo.')
    else:
        form = VacinaForm(instance=vacina)
    return render(request, "vacina/vacina_form.html", {"form": form, "vacina": vacina})


@staff_member_required(login_url='/login/')
def excluir_vacina(request, pk):
    vacina = get_object_or_404(Vacina, pk=pk)
    if request.method == "POST":
        nome = vacina.nome
        try:
            vacina.delete()
        except ProtectedError:
      
            messages.error(request, f'Não é possível excluir a vacina "{nome}": existem vacinações registradas com ela.')
            return redirect("vacina:detalhar", pk=pk)
        messages.warning(request, f'A vacina "{nome}" foi removida do sistema.')
        return redirect("vacina:listar")
    return render(request, "vacina/vacina_confirm_delete.html", {"vacina": vacina})