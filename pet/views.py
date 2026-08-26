from django.shortcuts import render, get_object_or_404, redirect
from .models import Pet
from .forms import PetForm

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