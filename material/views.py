
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from material.models import Material


class LocationsCreateView(LoginRequiredMixin, CreateView):
    model = Material
    fields = '__all__'
    success_url = reverse_lazy('material:listView')


class LocationUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Material
    fields = "__all__"
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('material:listView')


class LocationListView(LoginRequiredMixin, ListView):
    model = Material
    paginate_by = 100
    template_name = "material/listView.html"


class LocationDelete(LoginRequiredMixin, DeleteView):
    model = Material
    success_url = reverse_lazy('material:listView')