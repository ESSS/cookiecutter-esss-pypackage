======================================================================
{{ cookiecutter.package_name.lower().replace('_', ' ') | capitalize }}
======================================================================


.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_name.lower().replace('_', '-') }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.project_name.lower().replace('_', '-') }}

.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name.lower().replace('_', '-') }}.svg
    :target: https://pypi.org/project/{{ cookiecutter.project_name.lower().replace('_', '-') }}

.. image:: https://img.shields.io/travis/ESSS/{{ cookiecutter.project_name.lower().replace('_', '-') }}.svg
    :target: https://travis-ci.com/ESSS/{{ cookiecutter.project_name.lower().replace('_', '-') }}

.. image:: https://ci.appveyor.com/api/projects/status/github/ESSS/{{ cookiecutter.project_name.lower().replace('_', '-') }}?branch=master
    :target: https://ci.appveyor.com/project/ESSS/{{ cookiecutter.project_name.lower().replace('_', '-') }}/?branch=master&svg=true

.. image:: https://codecov.io/gh/ESSS/{{ cookiecutter.project_name.lower().replace('_', '-') }}/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/ESSS/{{ cookiecutter.project_name.lower().replace('_', '-') }}

.. image:: https://img.shields.io/readthedocs/pip.svg
    :target: https://{{ cookiecutter.project_name.lower().replace('_', '-') }}.readthedocs.io/en/latest/

What is {{ cookiecutter.package_name.lower().replace('_', ' ') | capitalize }} ?
================================================================================

{{ cookiecutter.package_description }}


Contributing
------------

For guidance on setting up a development environment and how to make a
contribution to {{ cookiecutter.package_name }}, see the `contributing guidelines`_.

.. _contributing guidelines: https://github.com/ESSS/{{ cookiecutter.project_name.lower().replace('_', '-') }}/blob/master/CONTRIBUTING.rst


Release
-------
A reminder for the maintainers on how to make a new release.

Note that the VERSION should folow the semantic versioning as X.Y.Z
Ex.: v1.0.5

1. Create a ``release-VERSION`` branch from ``upstream/master``.
2. Update ``CHANGELOG.rst``.
3. Push a branch with the changes.
4. Once all builds pass, push a ``VERSION`` tag to ``upstream``.
5. Merge the PR.
