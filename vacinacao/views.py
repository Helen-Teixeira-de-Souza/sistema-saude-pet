from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from pet.models import Pet
from vacina.models import Vacina
from .models import Vacinacao


def listar_vacinacao(request):
    vacinacao_list = Vacinacao.objects.all()
    context = {"vacinacao_list": vacinacao_list}
    return render(request, "vacinacao/vacinacao_list.html", context)


def detalhe_vacinacao(request, vacinacao_id):
    vacinacao = get_object_or_404(Vacinacao, pk=vacinacao_id)
    context = {"vacinacao": vacinacao}
    return render(request, "vacinacao/vacinacao_detail.html", context)


def criar_vacinacao(request):
    if request.method == "POST":
        pet = get_object_or_404(Pet, pk=request.POST["pet"])
        vacina = get_object_or_404(Vacina, pk=request.POST["vacina"])
        dose_atual = request.POST["dose_atual"]
        data_aplicacao = request.POST["data_aplicacao"]
        proxima_dose = request.POST.get("proxima_dose") or None
        observacoes = request.POST.get("observacoes", "")

        vacinacao = Vacinacao.objects.create(
            pet=pet,
            vacina=vacina,
            dose_atual=dose_atual,
            data_aplicacao=data_aplicacao,
            proxima_dose=proxima_dose,
            observacoes=observacoes,
        )
        return HttpResponseRedirect(reverse("vacinacao_detail", args=(vacinacao.id,)))

    context = {
        "pet_list": Pet.objects.all(),
        "vacina_list": Vacina.objects.all(),
    }
    return render(request, "vacinacao/vacinacao_form.html", context)


def editar_vacinacao(request, vacinacao_id):
    vacinacao = get_object_or_404(Vacinacao, pk=vacinacao_id)

    if request.method == "POST":
        vacinacao.pet = get_object_or_404(Pet, pk=request.POST["pet"])
        vacinacao.vacina = get_object_or_404(Vacina, pk=request.POST["vacina"])
        vacinacao.dose_atual = request.POST["dose_atual"]
        vacinacao.data_aplicacao = request.POST["data_aplicacao"]
        vacinacao.proxima_dose = request.POST.get("proxima_dose") or None
        vacinacao.observacoes = request.POST.get("observacoes", "")
        vacinacao.save()
        return HttpResponseRedirect(reverse("vacinacao_detail", args=(vacinacao.id,)))

    context = {
        "vacinacao": vacinacao,
        "pet_list": Pet.objects.all(),
        "vacina_list": Vacina.objects.all(),
    }
    return render(request, "vacinacao/vacinacao_form.html", context)


def deletar_vacinacao(request, vacinacao_id):
    vacinacao = get_object_or_404(Vacinacao, pk=vacinacao_id)

    if request.method == "POST":
        vacinacao.delete()
        return HttpResponseRedirect(reverse("vacinacao_list"))

    context = {"vacinacao": vacinacao}
    return render(request, "vacinacao/vacinacao_confirm_delete.html", context)
