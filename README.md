# Django Calculator

A simple Django-based calculator web app that performs basic arithmetic operations: addition, subtraction, multiplication, and division.

## Features

- Add two numbers
- Subtract two numbers
- Multiply two numbers
- Divide two numbers
- Handles division by zero

## Project Structure

- `manage.py` - Django management entry point
- `calculator/` - Main app with views, URLs, templates, and tests
- `calculator_project/` - Project settings and root URL configuration
- `db.sqlite3` - Default SQLite database

## Requirements

- Python 3.x
- Django 6.x

## Setup

1. Open a terminal in the project root.
2. Create and activate a virtual environment if needed.

On Windows PowerShell:

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install django
```

## Run the App

Start the development server:

```powershell
python manage.py runserver
```

Then open the app in your browser at:

```text
http://127.0.0.1:8000/
```

## Usage

- Enter the first number
- Choose an operation
- Enter the second number
- Click Calculate to see the result

## Admin

The admin site is available at:

```text
http://127.0.0.1:8000/admin/
```

If you want to use the admin interface, create a superuser first:

```powershell
python manage.py createsuperuser
```
