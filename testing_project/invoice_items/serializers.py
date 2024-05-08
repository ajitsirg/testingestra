from rest_framework import serializers
from .models import InvoiceItem , Invoice






class InvoiceItemSerializer(serializers.ModelSerializer):
    invoice_id = serializers.IntegerField(required=True)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, help_text="Amount as integer or decimal")

    class Meta:
        model = InvoiceItem
        fields = ['invoice_id', 'description', 'units', 'amount']

class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True, read_only=True)  

    class Meta:
        model = Invoice
        fields = ['id', 'date', 'items']         