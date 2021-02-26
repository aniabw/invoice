# Invoice Manager
This is application that allows invoices to be stored in a database, with various pieces of functionality that allow 
a user to insert, search and list the invoices.

## How to run this project
``` python -m venv venv ``` \
``` source venv/bin/activate ``` \
``` pip install -r requirements.txt ``` \
``` python manage.py migrate ``` \
``` python manage.py runserver ``` 

## Application functionality includes:
* view a list of all invoices, and enter new invoices into the application,
* functionality that allows a user to search invoices, based on the ‘internal_reference’.i.e. /invoice?internal_reference=TEST
* invoices are assigned to a company, each invoice is allocated to a company,
* the company name and company number are stored in company,
* functionality that displays invoices that are allocated to a particular company.i.e. /invoice/company/1