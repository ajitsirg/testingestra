from django.urls import path
from . import views

urlpatterns = [
    path('invoices/', views.get_invoices, name='get_invoices'),
    path('invoices/<int:invoice_id>/', views.get_invoice, name='get_invoice'),
    path('invoice-items/', views.get_invoice_items, name='get_invoice_items'),
    path('invoice-items/<int:invoice_item_id>/', views.get_specific_invoice_item, name='get_specific_invoice_item'),
    path('create-invoice/', views.create_invoice, name='create_invoice'),
    path('create-invoice-item/', views.create_invoice_item, name='create_invoice_item'),
]