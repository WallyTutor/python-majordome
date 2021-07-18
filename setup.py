# -*- coding: utf-8 -*-
""" Setup support. """
from setuptools import setup
from setuptools import find_packages

version = {}
with open('majordome/version.py') as fp:
    exec(fp.read(), version)

setup(
    name=version['name'],
    packages=find_packages(),
    author=version['author'],
    description=version['description'],
    version=version['version'],
    install_requires=version['install_requires'],
    package_data=version['package_data'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ]
)
