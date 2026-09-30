from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cirurgia
from .forms import CirurgiaForm

@login_required
def listar_cirurgias(request):
    cirurgias = Cirurgia.objects.select_related('pet', 'profissional').all()
    return render(request, "cirurgia/cirurgia_list.html", {"cirurgias": cirurgias})

@login_required
def detalhar_cirurgia(request, pk):
    cirurgia = get_object_or_404(Cirurgia, pk=pk)
    return render(request, "cirurgia/cirurgia_detail.html", {"cirurgia": cirurgia})

@login_required
def criar_cirurgia(request):
    form = CirurgiaForm(request.POST or None)
    if form.is_valid():
        cirurgia = form.save()
        return redirect("cirurgia:detalhar", pk=cirurgia.pk)
    return render(request, "cirurgia/cirurgia_form.html", {"form": form, "titulo": "Cadastrar Cirurgia"})

@login_required
def editar_cirurgia(request, pk):
    cirurgia = get_object_or_404(Cirurgia, pk=pk)
    form = CirurgiaForm(request.POST or None, instance=cirurgia)
    if form.is_valid():
        form.save()
        return redirect("cirurgia:detalhar", pk=pk)
    return render(request, "cirurgia/cirurgia_form.html", {"form": form, "titulo": "Editar Cirurgia", "cirurgia": cirurgia})

@login_required
def excluir_cirurgia(request, pk):
    cirurgia = get_object_or_404(Cirurgia, pk=pk)
    if request.method == "POST":
        cirurgia.delete()
        return redirect("cirurgia:listar")
    return render(request, "cirurgia/cirurgia_confirm_delete.html", {"cirurgia": cirurgia})