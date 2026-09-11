from django.shortcuts import render, redirect, get_object_or_404
from .models import Vacinacao
from .forms import VacinacaoForm

def listar_vacinacoes(request):
    vacinacoes = Vacinacao.objects.select_related("pet", "vacina").all()
    return render(request, "vacinacao/vacinacao_list.html", {"vacinacao_list": vacinacoes})

def detalhar_vacinacao(request, pk):
    vacinacao = get_object_or_404(Vacinacao, pk=pk)
    return render(request, "vacinacao/vacinacao_detail.html", {"vacinacao": vacinacao})

def criar_vacinacao(request):
    form = VacinacaoForm(request.POST or None)
    if form.is_valid():
        vacinacao = form.save()
        return redirect("vacinacao:detalhar_vacinacao", pk=vacinacao.id)
    return render(request, "vacinacao/vacinacao_form.html", {"form": form})

def editar_vacinacao(request, pk):
    vacinacao = get_object_or_404(Vacinacao, pk=pk)
    form = VacinacaoForm(request.POST or None, instance=vacinacao)
    if form.is_valid():
        form.save()
        return redirect("vacinacao:detalhar_vacinacao", pk=vacinacao.id)
    return render(request, "vacinacao/vacinacao_form.html", {"form": form, "vacinacao": vacinacao})

def excluir_vacinacao(request, pk):
    vacinacao = get_object_or_404(Vacinacao, pk=pk)
    if request.method == "POST":
        vacinacao.delete()
        return redirect("vacinacao:listar_vacinacoes")
    return render(request, "vacinacao/vacinacao_confirm_delete.html", {"vacinacao": vacinacao})