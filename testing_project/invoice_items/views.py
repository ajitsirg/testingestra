from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import InvoiceItem, Invoice
from .serializers import InvoiceItemSerializer, InvoiceSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from datetime import date
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
# Endpoint to create a new invoice
@swagger_auto_schema(method='post', request_body=InvoiceSerializer)
@api_view(['POST'])
def create_invoice(request:HttpRequest): 
    """
    Create a new invoice.

    Parameters:
        - date: The date of the invoice in the format 'YYYY-MM-DD'.


    Returns:
        - 201 Created: If the invoice was successfully created.
        - 400 Bad Request: If the request body is invalid.
    """
    request.data['date'] = date.today()
    serializer = InvoiceSerializer(data=request.data)
    if serializer.is_valid(): 
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Endpoint to get all invoices
@swagger_auto_schema(method='get', responses={200: InvoiceSerializer(many=True)})
@api_view(['GET'])
def get_invoices(request):
    """
    Retrieve all invoices.

    Returns:
        - 200 OK: A list of all invoices.`
    """
    invoices = Invoice.objects.all()
    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data)

# Endpoint to create a new invoice item
@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['invoice_id', 'description', 'units', 'amount'],
        properties={
            'invoice_id': openapi.Schema(type=openapi.TYPE_INTEGER),
            'description': openapi.Schema(type=openapi.TYPE_STRING),
            'units': openapi.Schema(type=openapi.TYPE_INTEGER),
            'amount': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_DECIMAL),
        },
    ),
)
@api_view(['POST'])
def create_invoice_item(request: HttpRequest):
    """
    Create a new invoice item for the specified invoice.

    Parameters:
        - invoice_id: The ID of the invoice to which the item belongs.

    Request Body:
        json
            {
            "invoice_id": integer,
            "description": "string",
            "units": integer,
            "amount": numeric
        }

    Returns:
        - 201 Created: If the invoice item was successfully created.
        - 400 Bad Request: If the request body is invalid.
    """
    # Extract invoice_id from request data
    invoice_id = request.data.get('invoice_id')
    
    # Check if invoice_id is provided
    if invoice_id is None:
        return Response({'error': 'invoice_id is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Create InvoiceItem instance with invoice_id
    serializer = InvoiceItemSerializer(data=request.data,context={'invoice_id': invoice_id})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Endpoint to get all invoice items
@swagger_auto_schema(method='get', responses={200: InvoiceItemSerializer(many=True)})
@api_view(['GET'])
def get_invoice_items(request):
    """
    Retrieve all invoice items.

    Returns:
        - 200 OK: A list of all invoice items.
    """
    invoice_items = InvoiceItem.objects.all()
    serializer = InvoiceItemSerializer(invoice_items, many=True)
    return Response(serializer.data)

# Endpoint to get details of a specific invoice
@swagger_auto_schema(method='get', responses={200: InvoiceSerializer()})
@api_view(['GET'])
def get_invoice(request, invoice_id):
    """
    Retrieve details of a specific invoice.

    Parameters:
        - invoice_id: The ID of the invoice.

    Returns:
        - 200 OK: Details of the specified invoice.
        - 404 Not Found: If the invoice does not exist.
    """
    try:
        invoice = Invoice.objects.get(id=invoice_id)
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)
    except Invoice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

# Endpoint to get details of a specific invoice item
@swagger_auto_schema(method='get', responses={200: InvoiceItemSerializer()})
@api_view(['GET'])
def get_specific_invoice_item(request, invoice_item_id):
    """
    Retrieve details of a specific invoice item.

    Parameters:
        - invoice_item_id: The ID of the invoice item.

    Returns:
        - 200 OK: Details of the specified invoice item.
        - 404 Not Found: If the invoice item does not exist.
    """
    try:
        invoice_item = InvoiceItem.objects.get(id=invoice_item_id)
        serializer = InvoiceItemSerializer(invoice_item)
        return Response(serializer.data)
    except InvoiceItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
