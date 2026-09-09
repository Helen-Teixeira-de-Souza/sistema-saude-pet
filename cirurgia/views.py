from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from pet.models import Pet
from profissional.models import Profissional
from .models import Cirurgia


def listar_cirurgia(request):
    cirurgia_list = Cirurgia.objects.all()
    context = {"cirurgia_list": cirurgia_list}
    return render(request, "cirurgia/cirurgia_list.html", context)


def detalhe_cirurgia(request, cirurgia_id):
    cirurgia = get_object_or_404(Cirurgia, pk=cirurgia_id)
    context = {"cirurgia": cirurgia}
    return render(request, "cirurgia/cirurgia_detail.html", context)


def criar_cirurgia(request):
    if request.method == "POST":
        pet = get_object_or_404(Pet, pk=request.POST["pet"])
        profissional_id = request.POST.get("profissional") or None
        profissional = get_object_or_404(Profissional, pk=profissional_id) if profissional_id else None
        data = request.POST["data"]
        local = request.POST["local"]
        procedimento = request.POST["procedimento"]
        cuidados_pos_operatorios = request.POST.get("cuidados_pos_operatorios", "")

        cirurgia = Cirurgia.objects.create(
            pet=pet,
            profissional=profissional,
            data=data,
            local=local,
            procedimento=procedimento,
            cuidados_pos_operatorios=cuidados_pos_operatorios,
        )
        return HttpResponseRedirect(reverse("cirurgia_detail", args=(cirurgia.id,)))

    context = {
        "pet_list": Pet.objects.all(),
        "profissional_list": Profissional.objects.all(),
    }
    return render(request, "cirurgia/cirurgia_form.html", context)


def editar_cirurgia(request, cirurgia_id):
    cirurgia = get_object_or_404(Cirurgia, pk=cirurgia_id)

    if request.method == "POST":
        cirurgia.pet = get_object_or_404(Pet, pk=request.POST["pet"])
        profissional_id = request.POST.get("profissional") or None
        cirurgia.profissional = get_object_or_404(Profissional, pk=profissional_id) if profissional_id else None
        cirurgia.data = request.POST["data"]
        cirurgia.local = request.POST["local"]
        cirurgia.procedimento = request.POST["procedimento"]
        cirurgia.cuidados_pos_operatorios = request.POST.get("cuidados_pos_operatorios", "")
        cirurgia.save()
        return HttpResponseRedirect(reverse("cirurgia_detail", args=(cirurgia.id,)))

    context = {
        "cirurgia": cirurgia,
        "pet_list": Pet.objects.all(),
        "profissional_list": Profissional.objects.all(),
    }
    return render(request, "cirurgia/cirurgia_form.html", context)


def deletar_cirurgia(request, cirurgia_id):
    cirurgia = get_object_or_404(Cirurgia, pk=cirurgia_id)

    if request.method == "POST":
        cirurgia.delete()
        return HttpResponseRedirect(reverse("cirurgia_list"))

    context = {"cirurgia": cirurgia}
    return render(request, "cirurgia/cirurgia_confirm_delete.html", context)
