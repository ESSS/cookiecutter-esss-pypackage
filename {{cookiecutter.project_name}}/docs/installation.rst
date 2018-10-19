.. highlight:: shell

============
Installation
============


Stable release
--------------

To install {{ cookiecutter.package_name | capitalize }}, run this command in your terminal:

.. code-block:: console

    $ pip install {{ cookiecutter.package_name }}

This is the preferred method to install {{ cookiecutter.package_name | capitalize }}, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for {{ cookiecutter.package_name | capitalize }} can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/ESSS/{{ cookiecutter.project_name.lower().replace('_', '-') }}

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/ESSS/{{ cookiecutter.project_name.lower().replace('_', '-') }}/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/ESSS/{{ cookiecutter.project_name.lower().replace('_', '-') }}
.. _tarball: https://github.com/ESSS/{{ cookiecutter.project_name.lower().replace('_', '-') }}/tarball/master
