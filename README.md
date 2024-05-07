# Testingestra

## Problem Statement

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

## Setup

### Installation

1. Clone the repository:
   git clone https://github.com/ajitsirg/testingestra.git

2. Set up a virtual environment to isolate dependencies:
    python -m venv env

3. Activate the virtual environment:
    For Windows:
            .\env\Scripts\activate
    For macOS and Linux:
            source env/bin/activate    

4. Install dependencies using the requirements file:
    pip install -r requirements.txt            

5. Navigate to the project directory:
    cd testing_project

## Running the Server
6. Run migrations to create database tables:
    python manage.py makemigrations
    python manage.py migarte

7. Create a superuser for accessing the admin interface:
    python manage.py createsuperuser

8. Create a superuser for accessing the admin interface:
    python manage.py createsuperuser
    user name
    password
9. Start the development server:
    python manage.py runserver

## Testing

Access the admin interface at http://127.0.0.1:8000/admin/ using the superuser credentials.
 id :ajit(or created)
 password 123(as created )
Test the APIs using Swagger documentation at http://127.0.0.1:8000/swagger/.

## API Endpoints
#   Create Invoice
    URL: POST /invoices/
    Description: Creates a new invoice with the specified date.
    Payload Structure:
       json
            {
                "date": "YYYY-MM-DD"
            }
    HTTP Method: POST
# Create Invoice Item
    URL: POST /invoices/<invoice_id>/items/
    Description: Adds an item to the specified invoice.
    Payload Structure:
        json
            {
                "description": "string",
                "units": "integer",
                "amount": "numeric"
            }
    HTTP Method: POST

# Retrieve Invoice
    URL: GET /invoices/<invoice_id>/
    Description: Retrieves details of the specified invoice.
    HTTP Method: GET

# Retrieve Invoice Item
    URL: GET /invoices/<invoice_id>/items/<item_id>/
    Description: Retrieves details of the specified invoice item.
    HTTP Method: GET

## Notes
    The .gitignore file excludes .pycache, migrations, and other unnecessary files from version control.
    Live Version
    You can access the live version of the application at http://13.127.222.17:8080/ on AWS.

# GitHub Repository
    You can find the project repository on GitHub: https://github.com/ajitsirg/testingestra



