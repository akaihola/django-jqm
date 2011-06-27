.. django-jqm documentation master file, created by
   sphinx-quickstart on Sat Jun 25 15:16:06 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Introduction to JQuery Mobile with Django
=========================================

This project is intended to let you quickly get "up and running" with a JQuery Mobile web application using Django to program the web application logic.  It is not intended to provide a framework for a "serious" JQuery Mobile application, just something to make playing with JQuery Mobile easier for Python programmers.

Contents:

.. toctree::
   :maxdepth: 2

Host Setup
----------

Project setup (for an Ubuntu Server or Debian Host), obviously you'll need to be root to do this::

    $ aptitude install python-pip python-virtualenv git bzr

VirtualEnv Setup
----------------

Set up a virtualenv with django-html, django-jqm, and, of course, django::

    $ virtualenv jqm-tutorial
    $ source jqm-tutorial/bin/activate
    $ pip install "django>=1.3"
    $ pip install -e "git+https://github.com/rhec/django-html5.git#egg=django-html5"
    $ pip install -e "bzr+http://bazaar.launchpad.net/~mcfletch/django-jqm/trunk/#egg=django-jqm"

Project Setup
-------------

At this point you should have a virtualenv with django installed, so let's create a very basic project::

    $ django-admin.py startproject tutorial

We'll now edit the auto-started project's settings.py to:
    
    * add jqm to the installed apps set (so that its templates will be available)
    * provide a basic database configuration
    * enable common context processors for templates
    * provide a default "on login" landing page (for now, '/')

Basic database configuration::

    DATABASES = {
        'default': {
            'ENGINE': 'sqlite3',
            'NAME': 'tutorial.db',
            # ...
        },
    }

A directory for our project-level templates::

    TEMPLATE_DIR = '/'.join([
        os.path.abspath( os.path.dirname( __file__ )),
        'templates',
    ])

    TEMPLATE_DIRS = (
        # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        TEMPLATE_DIR,
    )
    
Common context processors (note, only request is actually required by django-jqm)::

    TEMPLATE_CONTEXT_PROCESSORS = [
        "django.core.context_processors.auth", 
        "django.core.context_processors.debug", 
        "django.core.context_processors.i18n", 
        "django.core.context_processors.static",
        "django.core.context_processors.request",
    ]

Add the following to INSTALLED_APPS::

    "jqm",

Finally, provide a default landing-page URL for post-login views::

    LOGIN_REDIRECT_URL = '/'

Generic View
============

We have now completed our project setup, the next step is to actually use JQuery Mobile to create some views.  The jqm project simply provides a number of templates that can be used to quickly get your jqm site up and running with the content-distribution-network hosted jqm sources.  These templates are fairly basic in their design, they use the default jqm styles to produce a generic layout.

We'll set up the DB so that Django will start up::

    $ DJANGO_SETTINGS_MODULE=tutorial.settings django-admin.py syncdb
    $ DJANGO_SETTINGS_MODULE=tutorial.settings django-admin.py runserver 0:8080

Our first view will be a fairly generic landing page with a bit of text and a "call to arms" in the form of a button to view a login-protected page (since we only have a single page at the moment, this will currently be our front-page as well).  Since we need the page to show up as the root page, we'll add a reference to the project urls.py.  We'll also enable a login and logout page with a url mapping::

    from django.conf.urls.defaults import patterns, include, url
    urlpatterns = patterns('',
        # Examples:
        url(r'^/?$', 'tutorial.views.home', name='home'),
        
        url(
            r'^accounts/login/$','django.contrib.auth.views.login',
            dict(   
                template_name = 'jqm/login.html',
            ),
            name='login',
        ),
        url(
            r'^accounts/logout/$','django.contrib.auth.views.logout',
            dict(
                template_name = 'jqm/logout.html',
            ),
            name='logout', 
        ),
        
    )

And then we will add the home view to our views module (we could, instead, use a generic view here, but you are likely going to want to customize this view later)::

    from django.shortcuts import render_to_response
    from django.template import RequestContext as RC

    def home( request ):
        return render_to_response(
            'index.html',
            {},
            context_instance = RC( request, {} ),
        )
   
And create the templates folder for our project templates::

    $ mkdir tutorial/templates

our view is just rendering the template `index.html` which extends the `jqm/simple.html` base template::

    {% extends "jqm/simple.html" %}
    {% block title %}A Landing Page{% endblock %}
    {% block content %}
    {% if user.is_anonymous %}
        <p>Obviously you love this site, why don't you log in and stay a while?</p>
        <a data-role="button" href="{% url login %}">Log In</a>
    {% else %}
        <p>Contratulations on logging in, we love visitors, but we currently have nothing to show you!</p>
    {% endif %}
    {% endblock %}

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

