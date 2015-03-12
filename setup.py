#!/usr/bin/env python
from setuptools import setup

setup(name='wagtaildemo',
      version='0.1',
      packages=['wagtaildemo'],
      include_package_data=True,
      exclude_package_data={'wagtaildemo': ['*.pyc']},
      scripts=['manage.py'],
      zip_safe=False)
