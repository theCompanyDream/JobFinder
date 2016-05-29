#coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "Job Search API"
VERSION = "0.0.1"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
REQUIRES = ['requests', 'yaml']


setup(
    name=NAME,
    author='Timothy Brantley II',
    keywords=['Indeed', 'Scraper'],
    install_requires = REQUIRES,
    include_package_data=True,
    version=VERSION,
    packages=['requests', 'yaml', 'grequests']
    )
