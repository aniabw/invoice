from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListInvoice.as_view(), name="invoice_list"),
    path('invoice/company/create', views.CreateCompany.as_view(), name="company_create"),
    path('invoice/company/<int:company_id>', views.ListInvoice.as_view(), name="invoice_list_filtered_by_company"),
    path('invoice/create', views.CreateInvoice.as_view(), name="invoice_create"),
]
