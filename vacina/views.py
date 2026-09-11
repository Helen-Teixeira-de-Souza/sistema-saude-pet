from django.shortcuts import render, redirect, get_object_or_404
from .models import Vacina
from .forms import VacinaForm


def listar_vacinas(request):
    vacinas = Vacina.objects.all()
    return render(request, "vacina/vacina_list.html", {"vacina_list": vacinas})


def detalhar_vacina(request, pk):
    vacina = get_object_or_404(Vacina, pk=pk)
    return render(request, "vacina/vacina_detail.html", {"vacina": vacina})


def criar_vacina(request):
    if request.method == "POST":
        form = VacinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vacina:listar_vacinas")
    else:
        form = VacinaForm()
    return render(request, "vacina/vacina_form.html", {"form": form})


def editar_vacina(request, pk):
    vacina = get_object_or_404(Vacina, pk=pk)
    if request.method == "POST":
        form = VacinaForm(request.POST, instance=vacina)
        if form.is_valid():
            form.save()
            return redirect("vacina:detalhar_vacina", pk=vacina.id)
    else:
        form = VacinaForm(instance=vacina)
    return render(request, "vacina/vacina_form.html", {"form": form, "vacina": vacina})


def excluir_vacina(request, pk):
    vacina = get_object_or_404(Vacina, pk=pk)
    if request.method == "POST":
        vacina.delete()
        return redirect("vacina:listar_vacinas")
    return render(request, "vacina/vacina_confirm_delete.html", {"vacina": vacina})