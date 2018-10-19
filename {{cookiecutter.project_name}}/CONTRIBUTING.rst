.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/ESSS/{{ cookiecutter.project_name.lower().replace('_', '-') }}/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

{{ cookiecutter.package_name }} could always use more documentation, whether as part of the
official Barril docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/ESSS/{{ cookiecutter.project_name.lower().replace('_', '-') }}/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `{{ cookiecutter.package_name }}` for local development.

#. Fork the `{{ cookiecutter.package_name }}` repo on GitHub.
#. Clone your fork locally::

    $ git clone git@github.com:your_github_username_here/{{ cookiecutter.project_name.lower().replace('_', '-') }}.git

#. Create a virtual environment and activate it::

    $ python -m virtualenv .env

    $ .env\Scripts\activate  # For Windows
    $ source .env/bin/activate  # For Linux

#. Install the development dependencies for setting up your fork for local development::

    $ cd {{ cookiecutter.package_name }}/
    $ pip install -e .[testing,docs]

   .. note::

       If you use ``conda``, you can install ``virtualenv`` in the root environment::

           $ conda install -n root virtualenv

       Don't worry as this is safe to do.

#. Install pre-commit::

    $ pre-commit install

#. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

#. When you're done making changes, run the tests::

    $ pytest

#. If you want to check the modification made on the documentation, you can generate the docs locally::

    $ tox -e docs

   The documentation files will be generated in ``docs/_build``.

#. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

#. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated.


Deploying
---------

See `HOWTORELEASE <https://github.com/ESSS/{{ cookiecutter.project_name.lower().replace('_', '-') }}/blob/master/HOWTORELEASE.rst>`_.
