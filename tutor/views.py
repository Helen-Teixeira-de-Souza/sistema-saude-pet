from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tutor
from .forms import TutorForm


class TutorListView(ListView):
    model = Tutor
    template_name = 'tutor/tutor_list.html'
    context_object_name = 'tutores'


class TutorDetailView(DetailView):
    model = Tutor
    template_name = 'tutor/tutor_detail.html'
    context_object_name = 'tutor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Permite visualizar todos os pets cadastrados para este tutor
        context['pets'] = self.object.pets.all()
        return context


class TutorCreateView(CreateView):
    model = Tutor
    form_class = TutorForm
    template_name = 'tutor/tutor_form.html'
    success_url = reverse_lazy('tutor_list')


class TutorUpdateView(UpdateView):
    model = Tutor
    form_class = TutorForm
    template_name = 'tutor/tutor_form.html'
    success_url = reverse_lazy('tutor_list')


class TutorDeleteView(DeleteView):
    model = Tutor
    template_name = 'tutor/tutor_confirm_delete.html'
    success_url = reverse_lazy('tutor_list')