from django import forms

from .models import Company, Invoice
from .utils import Utils


class InvoiceSearchForm(forms.ModelForm):
    internal_reference = forms.CharField(label='',
                                         widget=forms.TextInput(attrs={'placeholder': 'Internal reference',
                                                                       'class': 'form-control'}))

    class Meta:
        model = Invoice
        fields = ['internal_reference']


class InvoiceCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(InvoiceCreateForm, self).__init__(*args, **kwargs)
        Utils.add_form_control_class(self)

    class Meta:
        model = Invoice
        fields = ['internal_reference', 'gross_amount', 'supplier_reference', 'company']


class CompanyCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CompanyCreateForm, self).__init__(*args, **kwargs)
        Utils.add_form_control_class(self)

    class Meta:
        model = Company
        fields = ['name', 'company_number']

        # You can specify styles for form also like that, instead of using add_form_control_class function:
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        # }
