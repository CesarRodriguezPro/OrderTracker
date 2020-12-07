from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Location
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class LocationsCreateView(LoginRequiredMixin,CreateView):
    model = Location
    fields = '__all__'
    success_url = reverse_lazy('location:listView')


class LocationUpdate(LoginRequiredMixin,SuccessMessageMixin, UpdateView):
    model = Location
    fields = "__all__"
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('location:listView')


class LocationListView(LoginRequiredMixin,ListView):
    model = Location
    paginate_by = 100
    template_name = "location/listView.html"


class LocationDelete(LoginRequiredMixin, DeleteView):
    model = Location
    success_url = reverse_lazy('location:listView')
