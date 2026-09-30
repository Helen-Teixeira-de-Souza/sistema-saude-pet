from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Exame
from .forms import ExameForm

@login_required
def listar_exames(request):
    exames = Exame.objects.select_related('pet', 'consulta').all()
    return render(request, 'exame/exame_list.html', {'exames': exames})


@login_required
def detalhar_exame(request, pk):
    exame = get_object_or_404(Exame, pk=pk)
    return render(request, 'exame/exame_detail.html', {'exame': exame})

@login_required
def criar_exame(request):
    if request.method == 'POST':
        form = ExameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exame:listar')
    else:
        form = ExameForm()
    return render(request, 'exame/exame_form.html', {'form': form, 'titulo': 'Cadastrar Exame'})

@login_required
def editar_exame(request, pk):
    exame = get_object_or_404(Exame, pk=pk)
    if request.method == 'POST':
        form = ExameForm(request.POST, instance=exame)
        if form.is_valid():
            form.save()
            return redirect('exame:detalhar', pk=pk)
    else:
        form = ExameForm(instance=exame)
    return render(request, 'exame/exame_form.html', {'form': form, 'titulo': 'Editar Exame', 'exame': exame})

@login_required
def excluir_exame(request, pk):
    exame = get_object_or_404(Exame, pk=pk)
    if request.method == 'POST':
        exame.delete()
        return redirect('exame:listar')
    return render(request, 'exame/exame_confirm_delete.html', {'exame': exame})