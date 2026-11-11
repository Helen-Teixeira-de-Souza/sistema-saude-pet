from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import TutorCreationForm, TutorForm
from .models import Tutor
from pet.models import Pet
from consulta.models import Consulta
from vacinacao.models import AvisoVacinacao, Vacinacao
from cirurgia.models import Cirurgia
from exame.models import Exame
from medicamento.models import Medicamento

# LISTAR
@staff_member_required(login_url='/login/')
def listar_tutores(request):
  tutores = Tutor.objects.all()
  return render(request, 'tutor/tutor_list.html', {'tutores': tutores})


# DETALHAR
@staff_member_required(login_url='/login/')
def detalhar_tutor(request, pk):
  tutor = get_object_or_404(Tutor, pk=pk)
  pets = tutor.pets.all()
  return render(request, 'tutor/tutor_detail.html', {'tutor': tutor, 'pets': pets})


# CADASTRAR (Criar)
def registrar_tutor(request):
  if request.method == 'POST':
    form = TutorCreationForm(request.POST)
    if form.is_valid():
      tutor = form.save()
      if request.user.is_authenticated and request.user.is_staff:
        return redirect('tutor:detalhar', pk=tutor.pk)
      messages.success(request, 'Cadastro realizado. Entre com seu usuário e senha.')
      return redirect('login')
  else:
    form = TutorCreationForm()

  return render(request, 'tutor/tutor_form.html', {
    'form': form,
    'titulo': 'Criar conta de tutor',
    'cadastro_publico': True,
  })


# EDITAR (Atualizar)
@login_required
def editar_tutor(request, pk):
  if not request.user.is_staff and request.user.pk != pk:
    return redirect('tutor:dashboard')
  tutor = get_object_or_404(Tutor, pk=pk)

  if request.method == 'POST':
    form = TutorForm(request.POST, instance=tutor)
    if form.is_valid():
      tutor = form.save()
      if request.user.is_staff:
        return redirect('tutor:detalhar', pk=tutor.pk)
      return redirect('tutor:dashboard')
  else:
    form = TutorForm(instance=tutor)

  return render(request, 'tutor/tutor_form.html', {
    'form': form,
    'tutor': tutor,
    'titulo': 'Editar tutor',
  })


# EXCLUIR (Deletar)
@staff_member_required(login_url='/login/')
def excluir_tutor(request, pk):
  tutor = get_object_or_404(Tutor, pk=pk)

  if request.method == 'POST':
    tutor.delete()
    return redirect('tutor:listar')

  return render(request, 'tutor/tutor_confirm_delete.html', {'tutor': tutor})

# Dashboard do tutor
@login_required(login_url='/login/')
def dashboard_tutor(request):

    if request.user.is_staff:
        # tutor/admin_dashboard.html não existe; a equipe vai direto para a lista de pets
        return redirect('pet:listar')

    # Filtra os pets pertencentes ao usuário logado
    meus_pets = Pet.objects.filter(tutor=request.user)
    
    # Busca o histórico de saúde completo associado a esses pets
    minhas_consultas = Consulta.objects.filter(pet__in=meus_pets)
    meus_exames = Exame.objects.filter(pet__in=meus_pets)
    meus_medicamentos = Medicamento.objects.filter(pet__in=meus_pets)
    minhas_vacinacoes = Vacinacao.objects.filter(pet__in=meus_pets)
    minhas_cirurgias = Cirurgia.objects.filter(pet__in=meus_pets)
    
    avisos = AvisoVacinacao.objects.filter(
        vacinacao__pet__in=meus_pets, vacinacao__isnull=False
    ).select_related('vacinacao__pet', 'vacinacao__vacina').order_by('data_aviso')

    context = {
        'avisos': avisos,
        'pets': meus_pets,
        'consultas': minhas_consultas,
        'exames': meus_exames,
        'medicamentos': meus_medicamentos,
        'vacinacoes': minhas_vacinacoes,
        'cirurgias': minhas_cirurgias,
    }
    return render(request, 'tutor/dashboard.html', context)