from django.shortcuts import render, get_object_or_404, redirect
from .models import Tutor
from .forms import TutorForm

# Detalhes do tutor
def tutor_detail(request, pk):
    tutor = get_object_or_404(Tutor, pk=pk)
    pets = tutor.pets.all() 
    return render(request, 'tutor/tutor_detail.html', {'tutor': tutor, 'pets': pets})

# Criar tutor
def tutor_create(request):
    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid():
            tutor = form.save()
            return redirect('tutor_detail', pk=tutor.pk)
    else:
        form = TutorForm()
    return render(request, 'tutor/tutor_form.html', {'form': form})

# Atualizar tutor
def tutor_update(request, pk):
    tutor = get_object_or_404(Tutor, pk=pk)
    if request.method == 'POST':
        form = TutorForm(request.POST, instance=tutor)
        if form.is_valid():
            form.save()
            return redirect('tutor_detail', pk=tutor.pk)
    else:
        form = TutorForm(instance=tutor)
    return render(request, 'tutor/tutor_form.html', {'form': form})

# Deletar tutor
def tutor_delete(request, pk):
    tutor = get_object_or_404(Tutor, pk=pk)
    if request.method == 'POST':
        tutor.delete()
        return redirect('pet_list') # ou home
    return render(request, 'tutor/tutor_confirm_delete.html', {'tutor': tutor})