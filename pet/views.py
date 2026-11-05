from datetime import date
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PetForm
from .models import Pet


def pet_list(request):
    pets = Pet.objects.all()
    return render(request, "pet/pet_list.html", {"pet_list": pets, "pets": pets})


def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
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
        "pet": pet,
        "idade": idade,
        "consultas": pet.consultas.all(),
        "vacinacoes": pet.vacinacoes.all(),
        "exames": pet.exames.all(),
        "medicamentos": pet.medicamentos.all(),
        "cirurgias": pet.cirurgias.all(),
    }
    return render(request, "pet/pet_detail.html", context)


def pet_create(request):
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save()
            return redirect("pet:detalhar", pk=pet.pk)
    else:
        form = PetForm()
    return render(request, "pet/pet_form.html", {"form": form})


def pet_update(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == "POST":
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            pet = form.save()
            return redirect("pet:detalhar", pk=pet.pk)
    else:
        form = PetForm(instance=pet)
    return render(request, "pet/pet_form.html", {"form": form, "pet": pet})


def pet_delete(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == "POST":
        pet.delete()
        return redirect("pet:listar")
    return render(request, "pet/pet_confirm_delete.html", {"pet": pet})
