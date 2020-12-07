from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Supplier
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from material.models import Material


class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    fields = '__all__'
    success_url = reverse_lazy('supplier:listView')


class SupplierUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Supplier
    fields = "__all__"
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('supplier:listView')


class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    paginate_by = 100
    template_name = "supplier/listView.html"


class SupplierDelete(LoginRequiredMixin, DeleteView):
    model = Supplier
    success_url = reverse_lazy('supplier:listView')


class SupplierDetail(LoginRequiredMixin, DetailView):
    model = Supplier

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['materials'] = Material.objects.filter(supplier=context['supplier'])
        return context
