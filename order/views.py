from django.views.generic import ListView
from .models import Receive


class ReceiveListView(ListView):
    model = Receive
    template_name = 'listView.html'
