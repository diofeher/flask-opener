"""Flask-DbShell-------------
Django-like dbshell
"""
from setuptools import setup, find_packages


setup(
    name='Flask-Opener',
    version='0.1',
    url='http://github.com/diofeher/flask-opener/',
    license='BSD',
    author='diofeher',
    author_email='contato@diofeher.net',
    description='Letter Opener (Rails) for Flask',
    long_description=__doc__,
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
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