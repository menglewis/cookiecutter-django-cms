cookiecutter-django-cms
=======================

A cookiecutter_ template for Django CMS

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Features
---------

* Django CMS 2.4.2
* Twitter Bootstrap 3
* Registration via django-allauth
* Procfile for deploying to Heroku

Usage
------

Install Cookiecutter

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/menglewis/cookiecutter-django-cms.git

You'll be prompted for some questions, answer them, then it will create a Django CMS project for you.

To get it running locally, start by creating a virtualenv for the project and activating it

    $ mkvirtualenv django-cms-project

Or without using virtualenvwrapper

    $ virtualenv venv
    $ source venv/bin/activate

Install local dependencies

    $ pip install -r requirements/local.txt

Sync the database

    $ python manage.py syncdb --all

Run the initial migrations

    $ python manage.py migrate --fake

Run the webserver

    $ python manage.py runserver

At this point you should be able to go to your browser and it should show the default Django CMS page and allow you to login and start adding pages.
