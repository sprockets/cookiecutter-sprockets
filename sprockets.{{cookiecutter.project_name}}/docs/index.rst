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

Requirements
------------
@TODO: Put full requirements list here, should match requirements.txt
-  `sprockets <https://github.com/sprockets/sprockets>`_

API Documentation
-----------------
.. toctree::
   :maxdepth: 2

   api
   examples

Version History
---------------
See :doc:`history`

Issues
------
Please report any issues to the Github project at `https://github.com/sprockets/sprockets.{{ cookiecutter.project_name }}/issues <https://github.com/sprockets/sprockets.{{ cookiecutter.project_name }}/issues>`_

Source
------
``sprockets.{{ cookiecutter.project_name }}`` source is available on Github at `https://github.com/sprockets/sprockets.{{ cookiecutter.project_name }} <https://github.com/sprockets/sprockets.{{ cookiecutter.project_name }}>`_

License
-------
``sprockets.{{ cookiecutter.project_name }}`` is released under the `3-Clause BSD license <https://github.com/sprockets/sprockets.{{ cookiecutter.project_name }}/blob/master/LICENSE>`_.

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. |Version| image:: https://badge.fury.io/py/sprockets.{{ cookiecutter.project_name }}.svg?
   :target: http://badge.fury.io/py/sprockets.{{ cookiecutter.project_name }}

.. |Status| image:: https://travis-ci.org/sprockets/sprockets.{{ cookiecutter.project_name }}.svg?branch=master
   :target: https://travis-ci.org/sprockets/sprockets.{{ cookiecutter.project_name }}

.. |Coverage| image:: https://img.shields.io/coveralls/sprockets/sprockets.{{ cookiecutter.project_name }}.svg?
   :target: https://coveralls.io/r/sprockets/sprockets.{{ cookiecutter.project_name }}

.. |Downloads| image:: https://pypip.in/d/sprockets.{{ cookiecutter.project_name }}/badge.svg?
   :target: https://pypi.python.org/pypi/sprockets.{{ cookiecutter.project_name }}

.. |License| image:: https://pypip.in/license/sprockets.{{ cookiecutter.project_name }}/badge.svg?
   :target: https://sprockets{{ cookiecutter.project_name.replace('.', '') }}.readthedocs.org
