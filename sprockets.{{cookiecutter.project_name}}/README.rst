sprockets.{{ cookiecutter.project_name }}
{{ '=' * (10 + cookiecutter.project_name|length) }}
{{ cookiecutter.description }}

|Version| |Downloads| |Status| |Coverage| |License|

Installation
------------
``sprockets.{{ cookiecutter.project_name }}`` is available on the
`Python Package Index <https://pypi.python.org/pypi/sprockets.{{ cookiecutter.project_name }}>`_
and can be installed via ``pip`` or ``easy_install``:

.. code:: bash

  pip install sprockets.{{ cookiecutter.project_name }}

Documentation
-------------
https://sprockets{{ cookiecutter.project_name.replace('.', '') }}.readthedocs.org

Requirements
------------
-  `sprockets <https://github.com/sprockets/sprockets>`_

Example
-------
This examples demonstrates how to use ``sprockets.{{ cookiecutter.project_name }}`` by ...

.. code:: python

    from sprockets import {{ cookiecutter.project_name }}

    # Example here

Version History
---------------
Available at https://sprockets{{ cookiecutter.project_name.replace('.', '') }}.readthedocs.org/en/latest/history.html

.. |Version| image:: https://img.shields.io/pypi/v/sprockets.{{ cookiecutter.project_name }}.svg?
  :target: http://badge.fury.io/py/sprockets.{{ cookiecutter.project_name }}

.. |Status| image:: https://img.shields.io/travis/sprockets/sprockets.{{ cookiecutter.project_name }}.svg?
  :target: https://travis-ci.org/sprockets/sprockets.{{ cookiecutter.project_name }}

.. |Coverage| image:: https://img.shields.io/codecov/c/github/sprockets/sprockets.{{ cookiecutter.project_name }}.svg?
  :target: https://codecov.io/github/sprockets/sprockets.{{ cookiecutter.project_name }}?branch=master

.. |Downloads| image:: https://img.shields.io/pypi/dm/sprockets.{{ cookiecutter.project_name }}.svg?
  :target: https://pypi.python.org/pypi/sprockets.{{ cookiecutter.project_name }}

.. |License| image:: https://img.shields.io/pypi/l/sprockets.{{ cookiecutter.project_name }}.svg?
  :target: https://sprockets{{ cookiecutter.project_name.replace('.', '') }}.readthedocs.org
