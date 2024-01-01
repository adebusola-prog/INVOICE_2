# invoices/forms.py
from django import forms
from .models import Customer, Invoice

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer', 'quantity', 'description', 'rate', 'amount', 'total', 'sub_total', 'deposit', 'balance']

        

