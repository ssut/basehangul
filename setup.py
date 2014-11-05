#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='basehangul',
    version='1.0',
    description='Human-readable binary encoding, BaseHangul for Python',
    author='SuHun Han',
    author_email='ssut@ssut.me',
    url='https://github.com/ssut/basehangul',
    packages=setup.find_packages()
)
