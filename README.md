# Library Management API

A simple Django REST API for managing a library system with authors and books.

## Current Date
Today's date: **${new Date().toDateString()}**

## Setup and Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Install dependencies: `pip install django djangorestframework`
5. Run migrations: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
7. Start the server: `python manage.py runserver`

## API Endpoints

- **Home**: `/` - Welcome message
- **Admin**: `/admin/` - Django admin interface
- **Authors**:
  - GET/POST: `/api/authors/` - List all authors or create a new one
  - GET/PUT/DELETE: `/api/authors/<id>/` - Retrieve, update or delete an author
- **Books**:
  - GET/POST: `/api/books/` - List all books or create a new one
  - GET/PUT/DELETE: `/api/books/<id>/` - Retrieve, update or delete a book

## Models

- **Author**: Represents a book author with a name.
- **Book**: Represents a book with title, ISBN, and author.

## Technologies Used

- Django
- Django REST Framework
- SQLite
