from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_invoice_item),
    path('list/', views.get_invoice_items),
]