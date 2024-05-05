from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_invoice),
    path('list/', views.get_invoices),
]
