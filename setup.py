#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open( 'README.md' ) as f:
    readme = f.read()

with open( 'LICENSE' ) as f:
    license = f.read()

setup(
    name = 'interstellar',
    version = '0.1.0',
    description = 'Dockerized script for pre-deploying Kafka topics',
    long_description = readme,
    author = 'Michael Reynolds',
    author_email = 'reynoldsm88@gmail.com',
    url = 'https://github.com/reynoldsm88/interstellar',
    license = license,
    packages = find_packages( exclude = ('tests', 'docs') )
)