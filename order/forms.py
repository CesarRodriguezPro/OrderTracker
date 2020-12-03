from django.forms import forms
from .models import Receive


class ReceiveForm(forms.Form):
    class Meta:
        model = Receive
        fields = ['name', 'quantity']
