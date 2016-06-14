#!/usr/bin/env python
#coding: utf-8

from setuptools import setup, find_packages

NAME = "Job Search API"
VERSION = "0.0.1"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
REQUIRES = ['requests', 'yaml', 'nose', 'rethinkdb']


setup(
    name=NAME,
    author='Timothy Brantley II',
    keywords=['Indeed', 'Scraper'],
    install_requires = REQUIRES,
    include_package_data=True,
    version=VERSION,
    packages=find_packages(exclude=['tests', 'tests.*']),
    entry_points ={
        'console_scripts': [
            'search:main'
        ]
    })
