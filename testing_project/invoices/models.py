from django.db import models


class Invoice(models.Model):
    date = models.DateField()

    def __str__(self):
        return f"Invoice {self.id}"