from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vacina
from .forms import VacinaForm


@login_required
def listar_vacinas(request):
    vacinas = Vacina.objects.all()
    return render(request, "vacina/vacina_list.html", {"vacina_list": vacinas})


@login_required
def detalhar_vacina(request, pk):
    vacina = get_object_or_404(Vacina, pk=pk)
    return render(request, "vacina/vacina_detail.html", {"vacina": vacina})


@login_required
def criar_vacina(request):
    if request.method == "POST":
        form = VacinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vacina:listar")
    else:
        form = VacinaForm()
    return render(request, "vacina/vacina_form.html", {"form": form})


@login_required
def editar_vacina(request, pk):
    vacina = get_object_or_404(Vacina, pk=pk)
    if request.method == "POST":
        form = VacinaForm(request.POST, instance=vacina)
        if form.is_valid():
            form.save()
            return redirect("vacina:detalhar", pk=vacina.pk)
    else:
        form = VacinaForm(instance=vacina)
    return render(request, "vacina/vacina_form.html", {"form": form, "vacina": vacina})


@login_required
def excluir_vacina(request, pk):
    vacina = get_object_or_404(Vacina, pk=pk)
    if request.method == "POST":
        vacina.delete()
        return redirect("vacina:listar")
    return render(request, "vacina/vacina_confirm_delete.html", {"vacina": vacina})