from django.db import models


class Supplier(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    telephone = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    emails = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name
