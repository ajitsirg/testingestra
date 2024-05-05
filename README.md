# testingestra 
## Task for Test
The project will have 2 models: "Invoice" and "InvoiceItem". They both
must have a unique 'id' column as well as be relationship using a
foreign key to the Invoice id on the InvoiceItem model, so the invoice
items are linked to their parent invoice. The invoice model should
have a date as well. The InvoiceItem model will have an integer column
"units", a string column "description" and a numeric column "amount".

Then utilize the classes/models you just created inside a web app
built using any Python web framework to expose a single "POST"
endpoint so that we can create an invoice via the exposed URL. Add
another "POST" endpoint to add an InvoiceItem. Add also some endpoints
to be able to GET the created data. We would prefer to see this as a
RESTful API.


For this task we are using python{Django},Database(Sqlite)
in That steps we are using 
1. virtrual env for isotaltion area not to impact other program 
2. python have 3.11.5 version
3. install required libraries
        --pip install django djangorestframework drf-yasg
4. Create a project 
    django-admin startproject testing_project
    cd testing_project
5. then create two apps in this directory:
     python manage.py startapp invoices
     python manage.py startapp invoice_items
6.     
    

    