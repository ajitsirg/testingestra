from django.db import models


class Invoice(models.Model):
    date = models.DateField()

    def __str__(self):
        return f"Invoice {self.id}"


class InvoiceItem(models.Model):
    description = models.CharField(max_length=100)
    units = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # DecimalField for both integer and decimal values
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items',null=False)

    def __str__(self):
        return self.description