from django.shortcuts import render, redirect, get_object_or_404
from .models import Cirurgia
from .forms import CirurgiaForm

def listar_cirurgias(request):
    cirurgias = Cirurgia.objects.select_related('pet', 'profissional').all()
    return render(request, "cirurgia/cirurgia_list.html", {"cirurgias": cirurgias})


def detalhar_cirurgia(request, pk):
    cirurgia = get_object_or_404(Cirurgia, pk=pk)
    return render(request, "cirurgia/cirurgia_detail.html", {"cirurgia": cirurgia})


def criar_cirurgia(request):
    form = CirurgiaForm(request.POST or None)
    if form.is_valid():
        cirurgia = form.save()
        return redirect("cirurgia:detalhar_cirurgia", pk=cirurgia.id)
    return render(request, "cirurgia/cirurgia_form.html", {"form": form, "titulo": "Cadastrar Cirurgia"})


def editar_cirurgia(request, pk):
    cirurgia = get_object_or_404(Cirurgia, pk=pk)
    form = CirurgiaForm(request.POST or None, instance=cirurgia)
    if form.is_valid():
        form.save()
        return redirect("cirurgia:detalhar_cirurgia", pk=pk)
    return render(request, "cirurgia/cirurgia_form.html", {"form": form, "titulo": "Editar Cirurgia", "cirurgia": cirurgia})


def excluir_cirurgia(request, pk):
    cirurgia = get_object_or_404(Cirurgia, pk=pk)
    if request.method == "POST":
        cirurgia.delete()
        return redirect("cirurgia:listar_cirurgias")
    return render(request, "cirurgia/cirurgia_confirm_delete.html", {"cirurgia": cirurgia})