from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
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
@permission_required('cirurgia.add_cirurgia', login_url='/login/')
def criar_cirurgia(request):
    if request.method == "POST":
        form = CirurgiaForm(request.POST)
        if form.is_valid():
            cirurgia = form.save()
            messages.success(request, f'Cirurgia "{cirurgia.procedimento}" registrada para {cirurgia.pet.nome}!')
            return redirect("cirurgia:detalhar", pk=cirurgia.pk)
        else:
            messages.error(request, 'Erro ao registrar a cirurgia. Verifique os dados informados.')
    else:
        form = CirurgiaForm()
    return render(request, "cirurgia/cirurgia_form.html", {"form": form, "titulo": "Cadastrar Cirurgia"})

@login_required
@permission_required('cirurgia.change_cirurgia', login_url='/login/')
def editar_cirurgia(request, pk):
    cirurgia = get_object_or_404(Cirurgia, pk=pk)
    if request.method == "POST":
        form = CirurgiaForm(request.POST, instance=cirurgia)
        if form.is_valid():
            cirurgia = form.save()
            messages.success(request, f'Cirurgia "{cirurgia.procedimento}" atualizada!')
            return redirect("cirurgia:detalhar", pk=pk)
        else:
            messages.error(request, 'Erro ao atualizar. Corrija os campos abaixo.')
    else:
        form = CirurgiaForm(instance=cirurgia)
    return render(request, "cirurgia/cirurgia_form.html", {"form": form, "titulo": "Editar Cirurgia", "cirurgia": cirurgia})

@login_required
@permission_required('cirurgia.delete_cirurgia', login_url='/login/')
def excluir_cirurgia(request, pk):
    cirurgia = get_object_or_404(Cirurgia, pk=pk)
    if request.method == "POST":
        descricao = f'{cirurgia.procedimento} de {cirurgia.pet.nome}'
        cirurgia.delete()
        messages.warning(request, f'A cirurgia "{descricao}" foi removida do sistema.')
        return redirect("cirurgia:listar")
    return render(request, "cirurgia/cirurgia_confirm_delete.html", {"cirurgia": cirurgia})