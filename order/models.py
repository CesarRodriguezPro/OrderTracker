from django.db import models
from accounts.models import User
from material.models import Material


class Receive(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    order_by = models.ManyToManyField(User)
    material = models.ManyToManyField(Material)

    def __str__(self):
        return f"{self.pk} - {self.date_created} order by {self.order_by.name}"

