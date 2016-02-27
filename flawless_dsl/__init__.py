# -*- coding: utf-8 -*-
# flawless_dsl/__init__.py
#
"""
only clean flawless DSL markup on output!

flawless DSL
============

fix any broken DSL in dictionary file.  this library can be imported and used in another project (like `pyglossary <https://github.com/ratijas/pyglossary>`_) or run from command line.

parses possibly broken DSL from stdin and prints out clean DSL to stdout.

usage
=====

- cli

.. code-block:: bash

    python -m flawless_dsl < broken.dsl > clean.dsl
    python -m flawless_dsl -h | --help     # display this help
    python -m flawless_dsl -v | --version  # print version

- import

.. code-block:: Python

    import flawless_dsl
    parse = flawless_dsl.FlawlessDSLParser().parse
    clean = parse(markup)
"""
#
# Copyright (C) 2016 Ratijas <ratijas.t@me.com>
#
# This program is a free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# You can get a copy of GNU General Public License along this program
# But you can always get it from http://www.gnu.org/licenses/gpl.txt
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

from . import layer
from . import tag
from .main import (
    FlawlessDSLParser,
    parse,
)
from .__main__ import cli

__version__ = '1.0'
