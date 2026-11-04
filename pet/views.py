
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Pet
from .forms import PetForm
from datetime import date


# --- GESTÃO DO PET ---

# READ
@login_required
def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'pet/pet_list.html', {'pets': pets})


@login_required
def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)

    # Cálculo da idade
    hoje = date.today()
    idade = hoje.year - pet.data_nascimento.year - (
        (hoje.month, hoje.day) < (pet.data_nascimento.month, pet.data_nascimento.day)
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


# CREATE
@login_required
@permission_required('pet.add_pet', login_url='/login/')
def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST)

        if form.is_valid():
            pet = form.save()
            messages.success(request, f'Pet "{pet.nome}" cadastrado com sucesso!')
            return redirect('pet_detail', pk=pet.pk)
        else:
            messages.error(request, 'Erro ao cadastrar o pet. Verifique os dados informados.')
    else:
        form = PetForm()

    return render(request, 'pet/pet_form.html', {'form': form})


# UPDATE
@login_required
@permission_required('pet.change_pet', login_url='/login/')
def pet_update(request, pk):
    pet = get_object_or_404(Pet, pk=pk)

    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)

        if form.is_valid():
            pet = form.save()
            messages.success(request, f'Dados do pet "{pet.nome}" atualizados com sucesso!')
            return redirect('pet_detail', pk=pet.pk)
        else:
            messages.error(request, 'Erro ao atualizar o pet. Verifique os dados informados.')
    else:
        form = PetForm(instance=pet)

    return render(request, 'pet/pet_form.html', {'form': form, 'pet': pet})


# DELETE
@login_required
@permission_required('pet.delete_pet', login_url='/login/')
def pet_delete(request, pk):
    pet = get_object_or_404(Pet, pk=pk)

    if request.method == 'POST':
        nome = pet.nome
        pet.delete()
        messages.success(request, f'Pet "{nome}" excluído com sucesso!')
        return redirect('pet_list')

    return render(
        request,
        'pet/pet_confirm_delete.html',
        {'pet': pet}
    )


# --- SEGUNDA VERSÃO DAS VIEWS ---

# CREATE
@login_required
@permission_required('pet.add_pet', login_url='/login/')
def cadastrar_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)

        if form.is_valid():
            pet = form.save()
            messages.success(request, f'Pet "{pet.nome}" cadastrado com sucesso!')
            return redirect('listar_pets')
        else:
            messages.error(request, 'Erro ao cadastrar o pet. Verifique os dados informados.')
    else:
        form = PetForm()

    return render(
        request,
        'pet/cadastrar.html',
        {'form': form}
    )


# READ
@login_required
def listar_pets(request):
    pets = Pet.objects.all()

    return render(
        request,
        'pet/listar.html',
        {'pets': pets}
    )


# UPDATE
@login_required
@permission_required('pet.change_pet', login_url='/login/')
def editar_pet(request, id):
    pet = get_object_or_404(Pet, id=id)

    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)

        if form.is_valid():
            pet = form.save()
            messages.success(request, f'Dados do pet "{pet.nome}" atualizados com sucesso!')
            return redirect('listar_pets')
        else:
            messages.error(request, 'Erro ao atualizar o pet. Verifique os dados informados.')
    else:
        form = PetForm(instance=pet)

    return render(
        request,
        'pet/editar.html',
        {'form': form, 'pet': pet}
    )


# DELETE
@login_required
@permission_required('pet.delete_pet', login_url='/login/')
def excluir_pet(request, id):
    pet = get_object_or_404(Pet, id=id)

    if request.method == 'POST':
        nome = pet.nome
        pet.delete()
        messages.success(request, f'Pet "{nome}" excluído com sucesso!')
        return redirect('listar_pets')

    return render(
        request,
        'pet/excluir.html',
        {'pet': pet}
    )
