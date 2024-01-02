# invoices/urls.py
from django.urls import path
from .views import InvoiceCreateView, create_customer, customer_list, customer_detail, invoice_detail, edit_customer, delete_customer, edit_invoice, delete_invoice


urlpatterns = [
    path('create-customer/', create_customer, name='create_customer'),
    # path('create-invoice/<int:customer_id>/', create_invoice, name='create_invoice'),
    path('create-invoice/<int:customer_id>/', InvoiceCreateView.as_view(), name='create_invoice'),
    path('customer-list/', customer_list, name='customer_list'),
    path('customer-detail/<int:customer_id>/', customer_detail, name='customer_detail'),
    path('invoice-detail/<int:customer_id>/<int:invoice_id>/', invoice_detail, name='invoice_detail'),
    path('edit-customer/<int:customer_id>/', edit_customer, name='edit_customer'),
    path('delete-customer/<int:customer_id>/', delete_customer, name='delete_customer'),
    path('edit-invoice/<int:customer_id>/<int:invoice_id>/', edit_invoice, name='edit_invoice'),
    path('delete-invoice/<int:customer_id>/<int:invoice_id>/', delete_invoice, name='delete_invoice'),
]
