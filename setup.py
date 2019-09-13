#!/usr/bin/python

from distutils.core import setup, Extension

setup(
    name='cpydemo',
    version='0.0.1',
    author='',
    author_email='',
    url='',
    ext_modules=[Extension('cpydemo', sources=['cpydemo\cpydemo.c'])]
)

