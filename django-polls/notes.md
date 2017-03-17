python -c "import django; print(django.get_version())"

django-admin startproject mysite

python manage.py runserver

python manage.py runserver 8080

python manage.py runserver 0.0.0.0:8000

# Projects vs. apps
What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

# Create a new app
python manage.py startapp polls

# Create tables in DB from mysite/settings.py
python manage.py migrate

# Add installed apps by adding dir.apps.AppConfig
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Then migrate DB to include models
python manage.py makemigrations polls

# Display migrations in SQL
python manage.py sqlmigrate polls 0001

# Start shell for API
python manage.py shell

or

export DJANGO_SETTINGS_MODULE=/path/to/mysite/settings.py
python
import django
django.setup()

# To inspect models customize __str__ and __repr__
from django.utils.encoding import python_2_unicode_compatible

# If using the admin app -
python manage.py createsuperuser
python manage.py runserver
http://127.0.0.1:8000/admin/

add the models to the apps admin.py file

# Views and templates
- namespace templates by putting them in app_name/templates/app_name
- use from django.template import loader to load templates and template.render or
- use from django.shortcuts import render

# URLS can map to models
- see polls/views/details

# Namespace URLs by adding app_name

# To avoid database race conditions
https://docs.djangoproject.com/en/1.9/ref/models/expressions/#avoiding-race-conditions-using-f

# Use view classes and subclassing for views to avoid common code in view functions

# Add tests to apps and then run with:
python manage.py test polls

from django.test import Client

# Use the static files functionality
- STATICFILES_FINDERS

# Default (admin etc) templates can be overriden
- use TEMPLATES in settings.py