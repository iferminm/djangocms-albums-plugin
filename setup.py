# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='djangocms-albums-plugin',
    version='0.0.1',
    author=u'Israel Fermín Montilla',
    author_email='ferminster@gmail.com',
    packages=['Pillow'],
    url='https://github.com/iferminm/djangocms-albums-plugin',
    license='GPL 3.0',
    description='Adds photogallery functionality to your djangocms'
                + 'website',
    long_description=open('README.txt').read(),
    zip_safe=False,
)
