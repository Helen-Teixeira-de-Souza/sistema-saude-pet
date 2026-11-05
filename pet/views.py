from django.contrib.auth.decorators import login_required
from datetime import date
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib import messages

from tutor.models import Tutor
from .forms import PetForm
from .models import Pet

# Restringe o campo de tutor no formulário para que o usuário comum só possa selecionar a si mesmo
def _form_pet(request, *args, **kwargs):
  form = PetForm(*args, **kwargs)
  if not request.user.is_staff:
    form.fields['tutor'].queryset = form.fields['tutor'].queryset.filter(pk=request.user.pk)
  return form 

# --- GESTÃO DO PET ---

# LISTAR
@login_required(login_url='/login/')

def listar_pets(request):
    if request.user.is_staff or request.user.is_superuser:
        pets = Pet.objects.all()
    else:
        pets = Pet.objects.filter(tutor_id=request.user.pk)

    return render(request, 'pet/pet_list.html', {'pet_list': pets})

# DETALHAR
@login_required(login_url='/login/')
def detalhar_pet(request, pk):
  pet = get_object_or_404(_pets_visiveis(request), pk=pk)

  # Cálculo da idade
  hoje = date.today()
  idade = (
      hoje.year
      - pet.data_nascimento.year
      - (
          (hoje.month, hoje.day)
          < (pet.data_nascimento.month, pet.data_nascimento.day)
      )
  )

  context = {
      'pet': pet,
      'idade': idade,
      'consultas': pet.consultas.all(),
      'vacinacoes': pet.vacinacoes.all(),
      'exames': pet.exames.all(),
      'medicamentos': pet.medicamentos.all(),
      'cirurgias': pet.cirurgias.all(),
  }

  return render(request, 'pet/pet_detail.html', context)


# CRIAR
@login_required(login_url='/login/')
def criar_pet(request):
  if request.method == 'POST':
    form = _form_pet(request, request.POST)

    if form.is_valid():
      pet = form.save()
      messages.success(request, f'Pet "{pet.nome}" cadastrado com sucesso!')
      return redirect('pet:detalhar', pk=pet.pk)
    else:
      messages.error(request, 'Erro ao cadastrar o pet. Verifique os dados informados.')
  else:
    form = _form_pet(request)

  return render(request, 'pet/pet_form.html', {'form': form})


# ATUALIZAR / EDITAR
@login_required(login_url='/login/')
def editar_pet(request, pk):
  pet = get_object_or_404(_pets_visiveis(request), pk=pk)

  if request.method == 'POST':
    form = _form_pet(request, request.POST, instance=pet)

    if form.is_valid():
      pet = form.save()
      messages.success(request, f'Pet "{pet.nome}" atualizado com sucesso!')
      return redirect('pet:detalhar', pk=pet.pk)
    else:
      messages.error(request, 'Erro ao atualizar o pet. Verifique os dados informados.')
  else:
    form = _form_pet(request, instance=pet)

  return render(request, 'pet/pet_form.html', {'form': form, 'pet': pet})


# DELETAR / EXCLUIR
@login_required(login_url='/login/')
def excluir_pet(request, pk):
  pet = get_object_or_404(_pets_visiveis(request), pk=pk)

  if request.method == 'POST':
    pet.delete()
    messages.warning(request, f'O pet {pet.nome} foi removido do sistema.')
    return redirect('pet:listar')

  return render(request, 'pet/pet_confirm_delete.html', {'pet': pet})


# HISTÓRICO DE SAÚDE
@login_required(login_url='/login/')
def historico_pet(request, pk):
  pet = get_object_or_404(_pets_visiveis(request), pk=pk)

  eventos = []

  for c in pet.consultas.select_related('profissional'):
    eventos.append({
      'data': c.data, 'tipo': 'Consulta', 'cor': 'primary', 'icone': 'fa-stethoscope',
      'titulo': f'Consulta{" com " + c.profissional.nome if c.profissional else ""}',
      'detalhe': c.diagnostico,
      'url': reverse('consulta:detalhar', args=[c.pk]),
    })

  for v in pet.vacinacoes.select_related('vacina'):
    detalhe = f'{v.dose_atual}ª dose'
    if v.proxima_dose:
      detalhe += f' - próxima dose em {v.proxima_dose.strftime("%d/%m/%Y")}'
    eventos.append({
      'data': v.data_aplicacao, 'tipo': 'Vacinação', 'cor': 'success', 'icone': 'fa-syringe',
      'titulo': v.vacina.nome, 'detalhe': detalhe,
      'url': reverse('vacinacao:detalhar', args=[v.pk]),
    })

  for e in pet.exames.all():
    eventos.append({
      'data': e.data_realizacao, 'tipo': 'Exame', 'cor': 'info', 'icone': 'fa-notes-medical',
      'titulo': e.nome, 'detalhe': e.resultado,
      'url': reverse('exame:detalhar', args=[e.pk]),
    })

  for m in pet.medicamentos.all():
    eventos.append({
      'data': m.data_inicio, 'tipo': 'Medicamento', 'cor': 'warning', 'icone': 'fa-pills',
      'titulo': m.nome,
      'detalhe': f'{m.dosagem}, {m.frequencia} por {m.duracao_dias} dia(s)',
      'url': reverse('medicamento:detalhar', args=[m.pk]),
    })

  for c in pet.cirurgias.all():
    eventos.append({
      'data': c.data, 'tipo': 'Cirurgia', 'cor': 'danger', 'icone': 'fa-procedures',
      'titulo': c.procedimento, 'detalhe': f'Local: {c.local}',
      'url': reverse('cirurgia:detalhar', args=[c.pk]),
    })

  eventos.sort(key=lambda evento: evento['data'], reverse=True)

  return render(request, 'pet/pet_historico.html', {'pet': pet, 'eventos': eventos})
