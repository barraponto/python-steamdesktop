========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |codecov|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-steamdesktop/badge/?style=flat
    :target: https://readthedocs.org/projects/python-steamdesktop
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/barraponto/python-steamdesktop.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/barraponto/python-steamdesktop

.. |requires| image:: https://requires.io/github/barraponto/python-steamdesktop/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/barraponto/python-steamdesktop/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/barraponto/python-steamdesktop/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/barraponto/python-steamdesktop

.. |version| image:: https://img.shields.io/pypi/v/steamdesktop.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/steamdesktop

.. |downloads| image:: https://img.shields.io/pypi/dm/steamdesktop.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/steamdesktop

.. |wheel| image:: https://img.shields.io/pypi/wheel/steamdesktop.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/steamdesktop

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/steamdesktop.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/steamdesktop

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/steamdesktop.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/steamdesktop


.. end-badges

Python Steam .desktop file manager

Finds desktop entries for games installed through Steam and adds the `Steam` category.
Makes it possible to group the entries in some Desktop Environments.

* Free software: GPL3 License

Installation
============

::

    pip install steamdesktop

Documentation
=============

https://python-steamdesktop.readthedocs.org/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
