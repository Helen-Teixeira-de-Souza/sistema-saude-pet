from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import TutorForm
from .models import Tutor


# LISTAR
@login_required
def listar_tutores(request):
  tutores = Tutor.objects.all()
  return render(request, 'tutor/tutor_list.html', {'tutores': tutores})


# DETALHAR
@login_required
def detalhar_tutor(request, pk):
  tutor = get_object_or_404(Tutor, pk=pk)
  pets = tutor.pets.all()
  return render(request, 'tutor/tutor_detail.html', {'tutor': tutor, 'pets': pets})


# CADASTRAR (Criar)
@login_required
def criar_tutor(request):
  if request.method == 'POST':
    form = TutorForm(request.POST)
    if form.is_valid():
      tutor = form.save()
      return redirect('tutor:detalhar', pk=tutor.pk)
  else:
    form = TutorForm()

  return render(request, 'tutor/tutor_form.html', {'form': form})


# EDITAR (Atualizar)
@login_required
def editar_tutor(request, pk):
  tutor = get_object_or_404(Tutor, pk=pk)

  if request.method == 'POST':
    form = TutorForm(request.POST, instance=tutor)
    if form.is_valid():
      tutor = form.save()
      return redirect('tutor:detalhar', pk=tutor.pk)
  else:
    form = TutorForm(instance=tutor)

  return render(request, 'tutor/tutor_form.html', {'form': form, 'tutor': tutor})


# EXCLUIR (Deletar)
@login_required
def excluir_tutor(request, pk):
  tutor = get_object_or_404(Tutor, pk=pk)

  if request.method == 'POST':
    tutor.delete()
    return redirect('tutor:listar')

  return render(request, 'tutor/tutor_confirm_delete.html', {'tutor': tutor})