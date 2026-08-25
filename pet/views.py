from datetime import date, timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pet, Consulta, Vacinacao, Exame, Medicamento, Cirurgia, AvisoVacinacao
from .forms import PetForm, ConsultaForm, VacinacaoForm, ExameForm, MedicamentoForm, CirurgiaForm

# --- GESTÃO DO PET (CBVs) ---

class PetListView(ListView):
    model = Pet
    template_name = 'pet/pet_list.html'
    context_object_name = 'pets'


class PetDetailView(DetailView):
    model = Pet
    template_name = 'pet/pet_detail.html'
    context_object_name = 'pet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = self.get_object()
        
        context['consultas'] = pet.consultas.all()
        context['vacinacoes'] = pet.vacinacoes.all()
        context['exames'] = pet.exames.all()
        context['medicamentos'] = pet.medicamentos.all()
        context['cirurgias'] = pet.cirurgias.all()
        return context


class PetCreateView(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pet/pet_form.html'
    
    def get_success_url(self):
        return reverse_lazy('pet_detail', kwargs={'pk': self.object.pk})


class PetUpdateView(UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'pet/pet_form.html'

    def get_success_url(self):
        return reverse_lazy('pet_detail', kwargs={'pk': self.object.pk})


class PetDeleteView(DeleteView):
    model = Pet
    template_name = 'pet/pet_confirm_delete.html'
    success_url = reverse_lazy('pet_list')


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