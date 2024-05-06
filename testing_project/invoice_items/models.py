from django.db import models


class Invoice(models.Model):
    date = models.DateField()

    def __str__(self):
        return f"Invoice {self.id}"


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    units = models.IntegerField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item {self.id} - {self.description}"