from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from pet.models import Pet
from consulta.models import Consulta
from .models import Medicamento


def medicamento_list(request):
    medicamento_list = Medicamento.objects.all()
    context = {"medicamento_list": medicamento_list}
    return render(request, "medicamento/medicamento_list.html", context)


def medicamento_detail(request, medicamento_id):
    medicamento = get_object_or_404(Medicamento, pk=medicamento_id)
    context = {"medicamento": medicamento}
    return render(request, "medicamento/medicamento_detail.html", context)


def medicamento_create(request):
    if request.method == "POST":
        pet = get_object_or_404(Pet, pk=request.POST["pet"])
        consulta_id = request.POST.get("consulta") or None
        consulta = get_object_or_404(Consulta, pk=consulta_id) if consulta_id else None
        nome = request.POST["nome"]
        dosagem = request.POST["dosagem"]
        frequencia = request.POST["frequencia"]
        data_inicio = request.POST["data_inicio"]
        duracao_dias = request.POST["duracao_dias"]

        medicamento = Medicamento.objects.create(
            pet=pet,
            consulta=consulta,
            nome=nome,
            dosagem=dosagem,
            frequencia=frequencia,
            data_inicio=data_inicio,
            duracao_dias=duracao_dias,
        )
        return HttpResponseRedirect(reverse("medicamento_detail", args=(medicamento.id,)))

    context = {
        "pet_list": Pet.objects.all(),
        "consulta_list": Consulta.objects.all(),
    }
    return render(request, "medicamento/medicamento_form.html", context)


def medicamento_update(request, medicamento_id):
    medicamento = get_object_or_404(Medicamento, pk=medicamento_id)

    if request.method == "POST":
        medicamento.pet = get_object_or_404(Pet, pk=request.POST["pet"])
        consulta_id = request.POST.get("consulta") or None
        medicamento.consulta = get_object_or_404(Consulta, pk=consulta_id) if consulta_id else None
        medicamento.nome = request.POST["nome"]
        medicamento.dosagem = request.POST["dosagem"]
        medicamento.frequencia = request.POST["frequencia"]
        medicamento.data_inicio = request.POST["data_inicio"]
        medicamento.duracao_dias = request.POST["duracao_dias"]
        medicamento.save()
        return HttpResponseRedirect(reverse("medicamento_detail", args=(medicamento.id,)))

    context = {
        "medicamento": medicamento,
        "pet_list": Pet.objects.all(),
        "consulta_list": Consulta.objects.all(),
    }
    return render(request, "medicamento/medicamento_form.html", context)


def medicamento_delete(request, medicamento_id):
    medicamento = get_object_or_404(Medicamento, pk=medicamento_id)

    if request.method == "POST":
        medicamento.delete()
        return HttpResponseRedirect(reverse("medicamento_list"))

    context = {"medicamento": medicamento}
    return render(request, "medicamento/medicamento_confirm_delete.html", context)
