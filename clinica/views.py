from django.shortcuts import render, get_object_or_404, redirect
from datetime import date, timedelta
from .models import Consulta, Vacina, Cirurgia
from .forms import ConsultaForm, VacinaForm, CirurgiaForm


def consulta_create(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('avisos_vacinas')
    else:
        form = ConsultaForm()
    return render(request, 'clinica/consulta_form.html', {'form': form, 'titulo': 'Cadastrar Consulta'})

def consulta_update(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('avisos_vacinas')
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'clinica/consulta_form.html', {'form': form, 'titulo': 'Editar Consulta'})

def consulta_delete(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == 'POST':
        consulta.delete()
        return redirect('avisos_vacinas')
    return render(request, 'clinica/confirm_delete.html', {'object': consulta, 'tipo': 'Consulta'})


def vacina_create(request):
    if request.method == 'POST':
        form = VacinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('avisos_vacinas')
    else:
        form = VacinaForm()
    return render(request, 'clinica/vacina_form.html', {'form': form, 'titulo': 'Cadastrar Vacina'})

def vacina_update(request, pk):
    vacina = get_object_or_404(Vacina, pk=pk)
    if request.method == 'POST':
        form = VacinaForm(request.POST, instance=vacina)
        if form.is_valid():
            form.save()
            return redirect('avisos_vacinas')
    else:
        form = VacinaForm(instance=vacina)
    return render(request, 'clinica/vacina_form.html', {'form': form, 'titulo': 'Editar Vacina'})

def vacina_delete(request, pk):
    vacina = get_object_or_404(Vacina, pk=pk)
    if request.method == 'POST':
        vacina.delete()
        return redirect('avisos_vacinas')
    return render(request, 'clinica/confirm_delete.html', {'object': vacina, 'tipo': 'Vacina'})


def cirurgia_create(request):
    if request.method == 'POST':
        form = CirurgiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('avisos_vacinas')
    else:
        form = CirurgiaForm()
    return render(request, 'clinica/cirurgia_form.html', {'form': form, 'titulo': 'Cadastrar Cirurgia'})

def cirurgia_update(request, pk):
    cirurgia = get_object_or_404(Cirurgia, pk=pk)
    if request.method == 'POST':
        form = CirurgiaForm(request.POST, instance=cirurgia)
        if form.is_valid():
            form.save()
            return redirect('avisos_vacinas')
    else:
        form = CirurgiaForm(instance=cirurgia)
    return render(request, 'clinica/cirurgia_form.html', {'form': form, 'titulo': 'Editar Cirurgia'})

def cirurgia_delete(request, pk):
    cirurgia = get_object_or_404(Cirurgia, pk=pk)
    if request.method == 'POST':
        cirurgia.delete()
        return redirect('avisos_vacinas')
    return render(request, 'clinica/confirm_delete.html', {'object': cirurgia, 'tipo': 'Cirurgia'})


def avisos_vacinas(request):
    limite = date.today() + timedelta(days=30)
    vacinas_alerta = Vacina.objects.filter(data_reforco__lte=limite).order_by('data_reforco')
    return render(request, 'clinica/avisos_vacinas.html', {'vacinas_alerta': vacinas_alerta})