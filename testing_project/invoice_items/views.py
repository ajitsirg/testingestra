from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import InvoiceItem, Invoice
from .serializers import InvoiceItemSerializer,InvoiceSerializer
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(method='post', request_body=InvoiceSerializer)
@api_view(['POST'])
def create_invoice(request):
    serializer = InvoiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get', responses={200: InvoiceSerializer(many=True)})
@api_view(['GET'])
def get_invoices(request):
    invoices = Invoice.objects.all()
    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data)



@swagger_auto_schema(method='post', request_body=InvoiceItemSerializer)
@api_view(['POST'])
def create_invoice_item(request):
    serializer = InvoiceItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get', responses={200: InvoiceItemSerializer(many=True)})
@api_view(['GET'])
def get_invoice_items(request):
    invoice_items = InvoiceItem.objects.all()
    serializer = InvoiceItemSerializer(invoice_items, many=True)
    return Response(serializer.data)
