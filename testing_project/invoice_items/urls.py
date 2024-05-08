from django.urls import path
from . import views

urlpatterns = [
    path('create_invoice_item/', views.create_invoice_item),
    path('list_invoice_items/', views.get_invoice_items),
    path('create_invoice/', views.create_invoice),
    path('list_invoice/', views.get_invoices),
]