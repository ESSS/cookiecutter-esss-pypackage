Prior to the use of this cookiecutter,  make sure that you have an account on `PyPI`_

Quickstart
----------
 
1. Install Cookiecutter
.......................

Create and activate an environment for the package project.

.. code-block:: bash

    conda create -n <repo_name> python=<python_version> cookiecutter

Activate your environment.

.. code-block:: bash

    activate <repo_name>          #Windows
    source activate <repo_name>   #Linux
    

2. Create the package
.....................

Use cookiecutter, informing the address of `cookiecutter-esss-pypackage`

Before you start, make sure that you have a `PyPI`_ account, because the `username` will be requested.

.. code-block:: bash

    cookiecutter https://github.com/ESSS/cookiecutter-esss-pypackage

Answer the questions in the prompt.


3. Create a GitHub Repo
.......................

Go to GitHub and create a new repository, where the name of the repository must be the same that ``[project_slug]`` from your answers to running cookiecutter. 

When creating the repository, make sure to:
- Keep __unmarked__  the option `Initialize this repository with a README`
- Keep the option `Add .gitignore` as `None`
- Keep the option `Add a License` as `None`

After that, commit the package to GitHub:

.. code-block:: bash

    cd <package_name>
    git init .
    git add .
    git commit -m "Initial skeleton."
    git remote add origin git@github.com:ESSS/<package_name>.git
    git push -u origin master

4. Set Up Travis CI and AppVeyor
................................

Travis CI and AppVeyor are both continuous integration services configured to be executed on every commit to the master branch or when a pull request is opened.

Make sure to enabled both services to work with your repository.

4.1 Activating Travis:

1. Open https://travis-ci.org/ sign in with github account
2. Access https://travis-ci.org/ESSS/<package_name>
3. Click on Activate repository

4.2 Activating AppVeyor:

1. Open https://www.appveyor.com/ and sign in with github account
2. On the dashboard click on `New Project`
3. Wait (no kidding, takes a time to load all projects).
4. Search for the <project_name> and click on `Add`

5. Setup deploy to PyPI
.......................

Travis CI will be also used to deploy the application to `PyPI`_, for more details check the section ``Release`` on the README file from your project.
In order to set up this configuration, it's necessary to encrypt you `PyPI`_ password on ``.travis.yml``

Make sure that you have the ``Travis command line client`` installed. 


5.1 Instruction to install travis-cli
................................................

You need to have at least the ruby version 1.9.3 installed in your machine.

.. code-block:: bash
   
   Win:
   choco install ruby
   
   Linux
   apt install ruby
   
Using the package manager from ruby you can install de travis-cli tool

.. code-block:: bash
   
    gem install travis 

Run the commands below on the root directory of your project.

.. code-block:: bash

      1) travis encrypt --add deploy.password
      2) Type your PyPI password
      
      On Linux:
         3) Press CTRL+D
      Windows:
         3) Press Enter
         4) On the new line Press CTRL+Z

The command line from ``travis`` will create a new entry called "Deploy" on your ``.travis.yml``  file. 

.. code-block:: yaml

      deploy:
        provider: pypi
        distributions: sdist bdist_wheel
        user: <pypi user>
        password:
          secure: REPLACE
        on:
          tags: true
          repo: ESSS/<package name>
          python: 3.6
  branches:
    only:
    - master
    - "/v(\\d+\\.)*\\d/"
  deploy:
    password:
      secure: <encrypted password>


Copy the ``<encrypted password>`` and replace the ``REPLACE`` text with the encrypted password.

Do not forget to delete the deploy and password newly created tags

.. code-block:: yaml

      deploy:
        provider: pypi
        distributions: sdist bdist_wheel
        user: <pypi user>
        password:
          secure: <encrypted password>
        on:
          tags: true
          repo: ESSS/<package name>
          python: 3.6
  branches:
    only:
    - master
    - "/v(\\d+\\.)*\\d/"

The project will only be available at PyPI after the first release, for more details on how to make a release check the section ``Release`` on the README file from your project.

**Don't forget to add at least one technical leader as maintainers.**

6. Set Up ReadTheDocs
.....................

`ReadTheDocs`_ hosts documentation for the open source community.

1. Log into your account at `ReadTheDocs`_ 
2. Click in "My Projects" and choose the button to Import the repository 
3. Click on import manualy 
4. Activate the `ReadTheDocs`  to work with github.
5. On the dashboard from ``ReadTheDocs``, click on ``Admin``
6. Select ``Integrations`` -> ``GitHub incoming webhook``
7. Copy the link -> https://readthedocs.org/api/v2/webhook/<package name>/<some number>/

On Github

1. Go to your package repository -> https://github.com/ESSS/<package name>
2. Click on ``Settings`` -> ``WebHooks``
3. Click on ``Add Webhook``
4. On Payload URL  use the URL of the integration
5. For ``Content type``, select ``application/x-www-form-urlencoded``
6. On ``Which events would you like to trigger this webhook?`` select ``Let me select individual events.`` and check the folling items:

- Pushes
- Branch or tag creation
- Branch or tag deletion

Now your documentation will get rebuilt when you make documentation changes to your package.

Don't forget to add at least one technical leader as maintainers.

.. _`ReadTheDocs`: https://readthedocs.org/

6. Set up Codacy


7. Set up Codecov


.. _`PyPI`: https://pypi.python.org/pypi
.. _`PyPI Help`: http://peterdowns.com/posts/first-time-with-pypi.html
.. _`Instructions on how to install the travis command line client`: https://github.com/travis-ci/travis.rb#installation


