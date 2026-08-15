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
    return render(request, 'clinica/consulta_form.html', {'form': form})


def vacina_create(request):
    if request.method == 'POST':
        form = VacinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('avisos_vacinas')
    else:
        form = VacinaForm()
    return render(request, 'clinica/vacina_form.html', {'form': form})


def cirurgia_create(request):
    if request.method == 'POST':
        form = CirurgiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('avisos_vacinas')
    else:
        form = CirurgiaForm()
    return render(request, 'clinica/cirurgia_form.html', {'form': form})


def avisos_vacinas(request):
    limite = date.today() + timedelta(days=30)
    
    vacinas_alerta = Vacina.objects.filter(data_reforco__lte=limite).order_by('data_reforco')
    return render(request, 'clinica/avisos_vacinas.html', {'vacinas_alerta': vacinas_alerta})