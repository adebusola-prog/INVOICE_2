# invoices/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Customer, Invoice
from .forms import CustomerForm, InvoiceForm, InvoiceFormSet, TotalSubtotalFormSet,DepositFormSet, BalanceFormSet


#def create_customer(request):
#    return render(request, 'invoices/base.html')

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'invoices/customer_list.html', {'customers': customers})

def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    invoices = Invoice.objects.filter(customer=customer)
    return render(request, 'invoices/customer_detail.html', {'customer': customer, 'invoices': invoices})

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_invoice')
    else:
        form = CustomerForm()
    return render(request, 'invoices/create_customer.html', {'form': form})

def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail', customer_id=customer.id)
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'invoices/edit_customer.html', {'form': form, 'customer': customer})

def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)

    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')

    return render(request, 'invoices/delete_customer.html', {'customer': customer})



def create_invoice(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    
    if request.method == 'POST':
        print("Received POST request")
        invoice_form = InvoiceForm(request.POST)
        if invoice_form.is_valid():
            print("Forms are valid")
            invoice = invoice_form.save(commit=False)
            invoice.customer = customer
            invoice.save()

            print("Data saved successfully")
            return redirect('customer_detail', customer_id=customer.id)
        else:
            print("Forms are not valid")
            print(invoice_form.errors)
    else:
        invoice_form = InvoiceForm()
       # details_form = InvoiceDetailsForm()

    return render(request, 'invoices/create_invoice.html', {'invoice_form': invoice_form, 'customer': customer})



class InvoiceCreateView(View):
    template_name = 'invoices/create_invoice.html'

    def get(self, request, *args, **kwargs):
        invoice_formset = InvoiceFormSet(queryset=Invoice.objects.none())
        deposit_formset = DepositFormSet(queryset=Invoice.objects.none())
        balance_formset = BalanceFormSet(queryset=Invoice.objects.none())
        total_subtotal_formset = TotalSubtotalFormSet(queryset=Invoice.objects.none())

        return render(request, self.template_name, {
            'invoice_formset': invoice_formset,
            'deposit_formset': deposit_formset,
            'balance_formset': balance_formset,
            'total_subtotal_formset': total_subtotal_formset,
            'title': 'Create Invoice'
        })

    def post(self, request, *args, **kwargs):
        invoice_formset = InvoiceFormSet(request.POST)
        deposit_formset = DepositFormSet(request.POST)
        balance_formset = BalanceFormSet(request.POST)
        total_subtotal_formset = TotalSubtotalFormSet(request.POST)

        if (
            invoice_formset.is_valid() and
            deposit_formset.is_valid() and
            balance_formset.is_valid() and
            total_subtotal_formset.is_valid()
        ):
            # Your existing logic for saving instances

            return redirect('success')

        return render(request, self.template_name, {
            'invoice_formset': invoice_formset,
            'deposit_formset': deposit_formset,
            'balance_formset': balance_formset,
            'total_subtotal_formset': total_subtotal_formset,
            'title': 'Create Invoice'
        })



def invoice_detail(request, customer_id, invoice_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    return render(request, 'invoices/invoice_detail.html', {'customer': customer, 'invoice': invoice})


def edit_invoice(request, customer_id, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)

    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('invoice_detail', customer_id=customer_id, invoice_id=invoice.id)
    else:
        form = InvoiceForm(instance=invoice)

    return render(request, 'invoices/edit_invoice.html', {'form': form, 'invoice': invoice})

def delete_invoice(request, customer_id, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)

    if request.method == 'POST':
        invoice.delete()
        return redirect('customer_detail', customer_id=customer_id)

    return render(request, 'invoices/delete_invoice.html', {'invoice': invoice})
