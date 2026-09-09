from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Vacina


def listar_vacina(request):
    vacina_list = Vacina.objects.all()
    context = {"vacina_list": vacina_list}
    return render(request, "vacina/vacina_list.html", context)


def detalhe_vacina(request, vacina_id):
    vacina = get_object_or_404(Vacina, pk=vacina_id)
    context = {"vacina": vacina}
    return render(request, "vacina/vacina_detail.html", context)


def criar_vacina(request):
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


def editar_vacina(request, vacina_id):
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


def deletar_vacina(request, vacina_id):
    vacina = get_object_or_404(Vacina, pk=vacina_id)

    if request.method == "POST":
        vacina.delete()
        return HttpResponseRedirect(reverse("vacina_list"))

    context = {"vacina": vacina}
    return render(request, "vacina/vacina_confirm_delete.html", context)
