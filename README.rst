Sprockets Package Template
==========================

This is a cookiecutter_ template that generates a sprockets package that
is consistent with the rest of the eco-system and ready to go in a few
seconds.  You will need to install the cookiecutter_ utility, then point
it at this repository, answer a few questions, and start coding.

   $ cookiecutter https://github.com/sprockets/cookiecutter-sprockets
   project_name (default is "")? packagename
   full_name (default is "")? John Doe
   email (default is "")? john.doe@example.com
   description (default is "")? This goes into setup.py
   git_org (default is "sprockets")?
   year (default is "2014")?
   $ cd sprockets.packagename
   $ ls
   .travis.yml             dev-requirements.txt    setup.py
   LICENSE                 doc/                    sprockets/
   MANIFEST.in             requirements.txt        test-requirements.txt
   README.rst              setup.cfg               tests/

As you can see, there are a handful of files there for you already.

.. _cookiecutter:: http://cookiecutter.readthedocs.org/en/latest/index.html
