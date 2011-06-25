#! /usr/bin/env python
"""Script to install pluggable JQuery Mobile templates for Django

pip install -e bzr+http://bazaar.launchpad.net/~mcfletch/django-jqm/trunk#egg=django-jqm

"""
import os,sys
from setuptools import setup

version = [
    (line.split('=')[1]).strip().strip('"').strip("'")
    for line in open(os.path.join('jqm', '__init__.py'))
    if line.startswith( '__version__' )
][0]

if __name__ == "__main__":
    setup( 
        name = 'django-jqm',
        version = version,
        description = 'Pluggable JQuery Mobile templates for Django',
        author = 'Mike C. Fletcher',
        author_email = 'mcfletch@vrplumber.com',
        license = "MIT",
        url = 'https://launchpad.net/django-jqm',
        packages = ['jqm'],
        package_dir = {
            'jqm':'jqm',
        },
        options = {
            'sdist':{
                'force_manifest':1,
                'formats':['gztar','zip'],},
        },
        zip_safe=False,
        install_requires = [
            'django >= 1.2',
        ]
    )
