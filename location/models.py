from django.db import models


class Location(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
