#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@paper.org>
# Copyright (C) 2019+ Gradiant, Vigo, Spain

from setuptools import setup, find_packages
from version import *

setup(
    name='bob.paper.icb2019.gradgpad',
    version=get_version(),
    description='Bob package to reproduce the ICB 2019 paper '
                'Generalized Presentation Attack Detection: a face anti-spoofing evaluation proposal',
    url='http://pypi.python.org/pypi/bob.paper.icb2019.gradgpad',
    license='GPLv3',
    author='Biometrics Team (Gradiant)',
    author_email='biometrics.support@paper.org',
    long_description='Bob package to reproduce the ICB 2019 paper '
                'Generalized Presentation Attack Detection: a face anti-spoofing evaluation proposal',
    keywords='paper icb2019 grad gpad generalized evaluation',

    # This line is required for any distutils based packaging.
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,

    install_requires=[
      "setuptools",
    ],

    entry_points={
        'console_scripts': [
            'create_summary_table.py = bob.paper.icb2019.gradgpad.scripts.create_summary_table:main',
            'download_resources.py = bob.paper.icb2019.gradgpad.scripts.download_resources:main',
        ],
    },
)
