from django.db import models
from accounts.models import User


choices = [
    ('pending', 'pending'),
    ('cancel', 'cancel'),
    ('complete', 'complete')
]


class Receive(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    order_by = models.ForeignKey(User, related_name='order_by', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=100, decimal_places=0)
    status = models.CharField(choices=choices,max_length=100)

    def __str__(self):
        return f"{self.pk} - {self.order_by}"

