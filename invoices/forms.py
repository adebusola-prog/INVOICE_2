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



class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['quantity', 'description', 'rate', 'amount']


class TotalSubtotalForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['total', 'sub_total']


class DepositForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['deposit']


class BalanceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['balance']


InvoiceFormSet = forms.modelformset_factory(
    model=Invoice,
    form=InvoiceForm,
    extra=1
)

TotalSubtotalFormSet = forms.modelformset_factory(
    model=Invoice,
    form=TotalSubtotalForm,
    extra=1
)

DepositFormSet = forms.modelformset_factory(
    model=Invoice,
    form=DepositForm,
    extra=1
)

BalanceFormSet = forms.modelformset_factory(
    model=Invoice,
    form=BalanceForm,
    extra=1
)
