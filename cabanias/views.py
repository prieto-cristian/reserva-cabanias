from multiprocessing import context

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Reserva, Cabania, Caracteristica
from .forms import ReservaForm

# Create your views here.

class CabaniaListView(ListView):
    model = Cabania
    template_name = "cabania_list.html"
    context_object_name = "cabanias"


class ReservaCreateView(CreateView):
    template_name = "reserva_detail.html"
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reserva_enviada")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cabania"] = get_object_or_404(Cabania, pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        cabania = get_object_or_404(Cabania, pk=self.kwargs["pk"])
        form.instance.cabania = cabania
        return super().form_valid(form)


def reserva_enviada(request):
    return render(request, "reserva_enviada.html")