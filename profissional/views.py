from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profissional
from .forms import ProfissionalForm

# CREATE
@login_required
def criar_profissional(request):
    if request.method == 'POST':
        form = ProfissionalForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('profissional:listar')
    else:
        form = ProfissionalForm()

    return render(
        request,
        'profissional/profissional_form.html',
        {'form': form}
    )


# LIST
@login_required
def listar_profissionais(request):
    profissionais = Profissional.objects.all()

    return render(
        request,
        'profissional/profissional_list.html',
        {'profissionais': profissionais}
    )


# DETAIL
@login_required
def detalhar_profissional(request, pk):
    profissional = get_object_or_404(
        Profissional,
        pk=pk
    )

    return render(
        request,
        'profissional/profissional_detail.html',
        {'profissional': profissional}
    )


# UPDATE
@login_required
def editar_profissional(request, pk):
    profissional = get_object_or_404(
        Profissional,
        pk=pk
    )

    if request.method == 'POST':
        form = ProfissionalForm(
            request.POST,
            instance=profissional
        )

        if form.is_valid():
            form.save()
            return redirect('profissional:listar')
    else:
        form = ProfissionalForm(
            instance=profissional
        )

    return render(
        request,
        'profissional/profissional_form.html',
        {'form': form}
    )


# DELETE
@login_required
def excluir_profissional(request, id):
    profissional = get_object_or_404(
        Profissional,
        id=id
    )

    if request.method == 'POST':
        profissional.delete()
        return redirect('profissional:listar')

    return render(
        request,
        'profissional/profissional_confirm_delete.html',
        {'profissional': profissional}
    )