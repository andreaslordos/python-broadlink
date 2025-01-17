#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


version = '0.13.0'

setup(
    name='broadlink',
    version=version,
    author='Andreas Lordos',
    author_email='andreasnohacks@gmail.com',
    url='http://github.com/andreaslordos/python-broadlink',
    packages=find_packages(),
    scripts=[],
    install_requires=['cryptography>=2.1.1', 'PyCRC'],
    description='Python API for controlling Broadlink IR controllers',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    include_package_data=True,
    zip_safe=False,
)
