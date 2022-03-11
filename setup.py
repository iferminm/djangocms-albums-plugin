# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='djangocms-albums-plugin',
    version='0.1.0',
    author=u'Israel Fermín Montilla',
    author_email='iferminm@gmail.com',
    packages=find_packages(),
    install_requires=['Pillow==9.0.1'],
    url='https://github.com/iferminm/djangocms-albums-plugin',
    license='GPL 3.0',
    description='Adds photogallery functionality to your djangocms'
                + ' website',
    long_description='Adds photogallery and albums functionality to your '
                      + 'djangocms powered website',
    zip_safe=False,
)
