# -*- coding: utf-8 -*-
"""
Copyright (C) 2019 Rice University.

This software is subject to the provisions of the
GNU AFFERO GENERAL PUBLIC LICENSE Version 3.0 (AGPL).
See LICENSE.txt for details.
"""
import os

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


def read_from_requirements_txt(filepath):
    f = os.path.join(here, filepath)
    with open(f) as fb:
        return tuple([x.strip() for x in fb if not x.strip().startswith('#')])


install_requires = read_from_requirements_txt('requirements/main.txt')
tests_require = read_from_requirements_txt('requirements/test.txt')
extras_require = {
    'test': tests_require,
}

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='cnx-common',
    description='A library of utilities used across CNX applications.',
    long_description=long_description,
    version='0.1.0',
    author='Connexions team',
    author_email='info@cnx.org',
    url="https://github.com/openstax/cnx-common",
    license='AGPL, See also LICENSE.txt',
    packages=find_packages(),
    tests_require=tests_require,
    install_requires=install_requires,
    extras_require=extras_require,
    include_package_data=True,
)
