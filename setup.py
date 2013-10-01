#!/usr/bin/env python

"""
Flask-Sockets
-------------

Elegant WebSockets for your Flask app.
"""
from setuptools import setup


setup(
    name='Flask-WebSocket',
    version='0.1',
    url='https://github.com/kennethreitz/flask-sockets',
    license='See License',
    author='Kenneth Reitz',
    author_email='_@kennethreitz.com',
    description='Elegant WebSockets for your Flask app.',
    long_description=__doc__,
    py_modules=['flask_sockets'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'gevent'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)