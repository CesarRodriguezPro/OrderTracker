from django.db import models
from supplier.models import Supplier


class Material(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} by {self.supplier}"
