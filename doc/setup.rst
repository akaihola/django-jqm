Django JQuery Mobile Setup
==========================

This document describes how to create a new Django project for use with the django-jqm quick-start templates.  If you have an existing Django project, the steps can be simplified to:

 * install django-jqm (and optionally django-html5 if you want to use HTML5 native widgets)
 * add "jqm" to your installed applications
 * add the standard auth, static and request template context handlers
 
You can then continue to :doc:`basicview`.

Host Setup
----------

Project setup (for an Ubuntu Server or Debian Host), obviously you'll need to be root to do this::

    $ aptitude install python-pip python-virtualenv git bzr

VirtualEnv Setup
----------------

Set up a virtualenv with django-html5, django-jqm, and, of course, django::

    $ virtualenv jqm-tutorial
    $ source jqm-tutorial/bin/activate
    $ pip install "django>=1.3"
    $ pip install -e "git+https://github.com/rhec/django-html5.git#egg=django-html5"
    $ pip install -e "bzr+http://bazaar.launchpad.net/~mcfletch/django-jqm/trunk/#egg=django-jqm"

Django Project Configuration
----------------------------

At this point you should have a virtualenv with Django installed, so let's create a very basic project::

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
        TEMPLATE_DIR,
    )
    
Common context processors (note, only auth, static and request are actually required by django-jqm)::

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

You should now be able to continue to :doc:`basicview`.
