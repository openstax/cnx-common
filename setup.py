# -*- coding: utf-8 -*-
"""
Copyright (C) 2019 Rice University.

This software is subject to the provisions of the
GNU AFFERO GENERAL PUBLIC LICENSE Version 3.0 (AGPL).
See LICENSE.txt for details.
"""
from setuptools import setup, find_packages

install_requires = (
    )

setup(
    name='cnx-common',
    version='0.1.0',
    author='Connexions team',
    author_email='info@cnx.org',
    url="https://github.com/openstax/cnx-common",
    license='AGPL, See also LICENSE.txt',
    description='A library of utilities used across CNX applications.',
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
        },
    )
