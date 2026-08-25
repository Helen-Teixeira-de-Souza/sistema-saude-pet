from datetime import date, timedelta
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pet, Consulta, Vacinacao, Exame, Medicamento, Cirurgia, AvisoVacinacao
from .forms import PetForm, ConsultaForm, VacinacaoForm, ExameForm, MedicamentoForm, CirurgiaForm

# --- GESTÃO DO PET ---

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'pet/pet_list.html', {'pets': pets})

def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)

    context = {
        'pet': pet,
        'consultas': pet.consultas.all(),
        'vacinacoes': pet.vacinacoes.all(),
        'exames': pet.exames.all(),
        'medicamentos': pet.medicamentos.all(),
        'cirurgias': pet.cirurgias.all(),
    }

    return render(request, 'pet/pet_detail.html', context)

def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST)

        if form.is_valid():
            pet = form.save()
            return redirect('pet_detail', pk=pet.pk)

    else:
        form = PetForm()

    return render(request, 'pet/pet_form.html', {'form': form})

def pet_update(request, pk):
    pet = get_object_or_404(Pet, pk=pk)

    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)

        if form.is_valid():
            pet = form.save()
            return redirect('pet_detail', pk=pet.pk)

    else:
        form = PetForm(instance=pet)

    return render(request, 'pet/pet_form.html', {'form': form, 'pet': pet})

def pet_delete(request, pk):
    pet = get_object_or_404(Pet, pk=pk)

    if request.method == 'POST':
        pet.delete()
        return redirect('pet_list')

    return render(
        request,
        'pet/pet_confirm_delete.html',
        {'pet': pet}
    )

# --- REGISTROS VINCULADOS AO PET ---

def registrar_vacinacao(request, pet_pk):
    pet = get_object_or_404(Pet, pk=pet_pk)
    if request.method == 'POST':
        form = VacinacaoForm(request.POST)
        if form.is_valid():
            vacinacao = form.save(commit=False)
            vacinacao.pet = pet
            vacinacao.save()
            return redirect('pet_detail', pk=pet.pk)
    else:
        form = VacinacaoForm()
    return render(request, 'pet/registro_form.html', {'form': form, 'pet': pet, 'titulo': 'Registrar Vacinação'})


def registrar_consulta(request, pet_pk):
    pet = get_object_or_404(Pet, pk=pet_pk)
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.pet = pet
            consulta.save()
            return redirect('pet_detail', pk=pet.pk)
    else:
        form = ConsultaForm()
    return render(request, 'pet/registro_form.html', {'form': form, 'pet': pet, 'titulo': 'Registrar Consulta'})


def registrar_exame(request, pet_pk):
    pet = get_object_or_404(Pet, pk=pet_pk)
    if request.method == 'POST':
        form = ExameForm(request.POST)
        if form.is_valid():
            exame = form.save(commit=False)
            exame.pet = pet
            exame.save()
            return redirect('pet_detail', pk=pet.pk)
    else:
        form = ExameForm()
    return render(request, 'pet/registro_form.html', {'form': form, 'pet': pet, 'titulo': 'Registrar Exame'})


def registrar_medicamento(request, pet_pk):
    pet = get_object_or_404(Pet, pk=pet_pk)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            medicamento = form.save(commit=False)
            medicamento.pet = pet
            medicamento.save()
            return redirect('pet_detail', pk=pet.pk)
    else:
        form = MedicamentoForm()
    return render(request, 'pet/registro_form.html', {'form': form, 'pet': pet, 'titulo': 'Registrar Medicamento'})


def registrar_cirurgia(request, pet_pk):
    pet = get_object_or_404(Pet, pk=pet_pk)
    if request.method == 'POST':
        form = CirurgiaForm(request.POST)
        if form.is_valid():
            cirurgia = form.save(commit=False)
            cirurgia.pet = pet
            cirurgia.save()
            return redirect('pet_detail', pk=pet.pk)
    else:
        form = CirurgiaForm()
    return render(request, 'pet/registro_form.html', {'form': form, 'pet': pet, 'titulo': 'Registrar Cirurgia'})

# --- DASHBOARD & ALERTAS ---

def avisos_vacinas(request):
    """View global para listar vacinas próximas do vencimento ou vencidas"""
    limite = date.today() + timedelta(days=30)
    vacinas_alerta = Vacinacao.objects.filter(proxima_dose__lte=limite).order_by('proxima_dose')
    return render(request, 'pet/avisos_vacinas.html', {'vacinas_alerta': vacinas_alerta})