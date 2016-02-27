#!/usr/bin/env python

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

from os import path

import flawless_dsl


here = path.abspath(path.dirname(__file__))

setup(
    name='flawless_dsl',
    version=flawless_dsl.__version__,
    description=flawless_dsl.__doc__.strip().splitlines()[0],
    long_description=flawless_dsl.__doc__,
    url='https://github.com/ratijas/flawless_dsl',
    author='Ratijas',
    author_email='ratijas.t@me.com',
    license='GPL v3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Environment :: Plugins',
        'Topic :: Education',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='parse clean DSL Dictionary Structure Language',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'flawless_dsl=flawless_dsl:cli',
        ],
    },
)
