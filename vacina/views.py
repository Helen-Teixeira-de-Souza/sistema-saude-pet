from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Vacina


def vacina_list(request):
    vacina_list = Vacina.objects.all()
    context = {"vacina_list": vacina_list}
    return render(request, "vacina/vacina_list.html", context)


def vacina_detail(request, vacina_id):
    vacina = get_object_or_404(Vacina, pk=vacina_id)
    context = {"vacina": vacina}
    return render(request, "vacina/vacina_detail.html", context)


def vacina_create(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        quantidade_dose = request.POST["quantidade_dose"]
        intervalo_doses_dias = request.POST["intervalo_doses_dias"]
        descricao = request.POST.get("descricao", "")

        Vacina.objects.create(
            nome=nome,
            quantidade_dose=quantidade_dose,
            intervalo_doses_dias=intervalo_doses_dias,
            descricao=descricao,
        )
        return HttpResponseRedirect(reverse("vacina_list"))

    return render(request, "vacina/vacina_form.html")


def vacina_update(request, vacina_id):
    vacina = get_object_or_404(Vacina, pk=vacina_id)

    if request.method == "POST":
        vacina.nome = request.POST["nome"]
        vacina.quantidade_dose = request.POST["quantidade_dose"]
        vacina.intervalo_doses_dias = request.POST["intervalo_doses_dias"]
        vacina.descricao = request.POST.get("descricao", "")
        vacina.save()
        return HttpResponseRedirect(reverse("vacina_detail", args=(vacina.id,)))

    context = {"vacina": vacina}
    return render(request, "vacina/vacina_form.html", context)


def vacina_delete(request, vacina_id):
    vacina = get_object_or_404(Vacina, pk=vacina_id)

    if request.method == "POST":
        vacina.delete()
        return HttpResponseRedirect(reverse("vacina_list"))

    context = {"vacina": vacina}
    return render(request, "vacina/vacina_confirm_delete.html", context)
