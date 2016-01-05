#!/usr/bin/env python
from setuptools import setup


setup(
    name='virgin-money-giving',
    version='0.0',
    description='Virgin Money Giving API Client',
    author='James Bowden',
    author_email='james.bowden@bynd.com',
    url='',
    packages=['virgin_money_giving'],
    install_requires=[
        'requests==2.9.0'
    ]
)
