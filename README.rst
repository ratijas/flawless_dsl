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

