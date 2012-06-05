#! /usr/bin/env python
"""Script to install pluggable JQuery Mobile templates for Django
"""
from setuptools import setup, find_packages

setup(
    name='django-jqm',
    version='1.1.0',
    description='Pluggable JQuery Mobile templates for Django',
    author='Mike C. Fletcher',
    author_email='mcfletch@vrplumber.com',
    license="MIT",
    url='https://launchpad.net/django-jqm',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)