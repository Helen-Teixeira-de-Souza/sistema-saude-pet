from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vacinacao
from .forms import VacinacaoForm

@login_required
def listar_vacinacoes(request):
    vacinacoes = Vacinacao.objects.select_related("pet", "vacina").all()
    return render(request, "vacinacao/vacinacao_list.html", {"vacinacao_list": vacinacoes})


@login_required
def detalhar_vacinacao(request, pk):
    vacinacao = get_object_or_404(Vacinacao, pk=pk)
    return render(request, "vacinacao/vacinacao_detail.html", {"vacinacao": vacinacao})


@login_required
def criar_vacinacao(request):
    form = VacinacaoForm(request.POST or None)
    if form.is_valid():
        vacinacao = form.save()
        return redirect("vacinacao:detalhar", pk=vacinacao.id)
    return render(request, "vacinacao/vacinacao_form.html", {"form": form})

@login_required
def editar_vacinacao(request, pk):
    vacinacao = get_object_or_404(Vacinacao, pk=pk)
    form = VacinacaoForm(request.POST or None, instance=vacinacao)
    if form.is_valid():
        form.save()
        return redirect("vacinacao:detalhar", pk=vacinacao.id)
    return render(request, "vacinacao/vacinacao_form.html", {"form": form, "vacinacao": vacinacao})

@login_required
def excluir_vacinacao(request, pk):
    vacinacao = get_object_or_404(Vacinacao, pk=pk)
    if request.method == "POST":
        vacinacao.delete()
        return redirect("vacinacao:listar")
    return render(request, "vacinacao/vacinacao_confirm_delete.html", {"vacinacao": vacinacao})