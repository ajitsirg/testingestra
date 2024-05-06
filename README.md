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


Setup Environment:
    Set up a virtual environment to isolate dependencies: python -m venv env
    Activate the virtual environment: source env/bin/activate

Install required libraries: pip install django djangorestframework drf-yasg
    Create Django Project:
    Create a Django project: django-admin startproject testing_project

Navigate to project directory:
    cd testing_project
    
Create a apps: 
    python manage.py startapp invoice_items

Define Models:
    Define models in the models.py files of the invoice_items apps.

Create Serializers:
    Create serializers for models in the serializers.py files of both models.

Define Views:
    Define API views using Django Rest Framework's @api_view decorator.

Migrate Database:
    Run migrations: python manage.py makemigrations and python manage.py migrate

Create a superuser: 
    python manage.py createsuperuser (username: ajitsingh, password: 123)

Setup URLs:
    Create urls.py files in each app to define URL patterns and link them to view functions.

Integrate Swagger:
    Add rest_framework and drf_yasg to INSTALLED_APPS in settings.py.
    Define URL schemas in the project's urls.py, including URLs for Swagger and Redoc.

Run Server:
    Start the development server: python manage.py runserver

Admin Interface:
    Access the admin interface at: http://127.0.0.1:8000/admin/ (username: ajit, password: 123)

Testing:
    Test the APIs using Swagger documentation at: http://127.0.0.1:8000/swagger/
    Test the live version at: http://13.127.222.17:8080/ on aws
    Test the  admin side also by http://127.0.0.1:8000/admin/ use username ajit password 123
*** Notes:
     for intailly i also used .gitignore for pycache & migrations & other unrequired file from env

GIT LINK : https://github.com/ajitsirg/testingestra 


