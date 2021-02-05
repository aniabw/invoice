from django.shortcuts import redirect, render
from django.views import generic

from .forms import CompanyCreateForm, InvoiceCreateForm, InvoiceSearchForm
from .models import Company, Invoice


class ListInvoice(generic.ListView):
    model = Invoice
    template_name = 'invoice_list.html'

    form_class = InvoiceSearchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if bool(self.request.GET.get('internal_reference')):
            self.kwargs['internal_reference'] = self.request.GET.get('internal_reference')

        context['invoice_list'] = Invoice.objects.filter(**self.kwargs).order_by('-created_at')
        context['invoice_search_form'] = InvoiceSearchForm()
        return context


class CreateInvoice(generic.CreateView):
    model = Invoice
    template_name = 'invoice_create.html'

    form_class = InvoiceCreateForm
    success_url = "/"


class CreateCompany(generic.CreateView):
    model = Company
    template_name = 'company_create.html'

    form_class = CompanyCreateForm
    success_url = "/"
