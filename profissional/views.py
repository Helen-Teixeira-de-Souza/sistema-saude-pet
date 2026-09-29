from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Profissional
from .forms import ProfissionalForm

# CREATE
def cadastrar_profissional(request):
    if request.method == 'POST':
        form = ProfissionalForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_profissionais')
    else:
        form = ProfissionalForm()

    return render(
        request,
        'profissional/cadastrar.html',
        {'form': form}
    )


# READ
def listar_profissionais(request):
    profissionais = Profissional.objects.all()

    return render(
        request,
        'profissional/listar.html',
        {'profissionais': profissionais}
    )


# UPDATE
def editar_profissional(request, id):
    profissional = get_object_or_404(
        Profissional,
        id=id
    )

    if request.method == 'POST':
        form = ProfissionalForm(
            request.POST,
            instance=profissional
        )

        if form.is_valid():
            form.save()
            return redirect('listar_profissionais')
    else:
        form = ProfissionalForm(
            instance=profissional
        )

    return render(
        request,
        'profissional/editar.html',
        {'form': form}
    )


# DELETE
def excluir_profissional(request, id):
    profissional = get_object_or_404(
        Profissional,
        id=id
    )

    if request.method == 'POST':
        profissional.delete()
        return redirect('listar_profissionais')

    return render(
        request,
        'profissional/excluir.html',
        {'profissional': profissional}
    )
