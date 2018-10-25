Prior to the use of this cookiecutter,  make sure that you have an account on `PyPI`_


Quickstart
----------
 
1. Install Cookiecutter

Create and activate an environment for the package project.

.. code-block:: bash

    conda create -n <repo_name> python=<python_version> cookiecutter

Activate your environment.

.. code-block:: bash

    activate <repo_name>          #Windows
    source activate <repo_name>   #Linux
    

2. Create the package

Use cookiecutter, informing the address of `cookiecutter-esss-pypackage`

.. code-block:: bash

    cookiecutter https://github.com/ESSS/cookiecutter-esss-pypackage

Answer the questions in the prompt.


3. Create a GitHub Repo

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

Travis CI and AppVeyor are both continuous integration services configured to be executed on every commit to the master branch or when a pull request is opened.

Make sure to enabled both services to work with your repository.

Travis CI will be also used to deploy the application to `PyPI`_, for more details check the section `Release` on the README file from your project.
In order to set up this configuration, it's necessary to encrypt you PyPi password on `.travis.yml`

.. code-block:: bash

      1) travis encrypt --add deploy.password
      2) Type the password
      3) Press Enter
      4) On the new line Press CTRL+Z


5. Set Up ReadTheDocs

`ReadTheDocs`_ hosts documentation for the open source community.
Log into your account at `ReadTheDocs`_ . If you don't have one, create one and log into it.

Click in "My Projects" and choose the button to Import the repository and follow the directions.

Now your documentation will get rebuilt when you make documentation changes to your package.

Don't forget to add at least one technical leader as maintainers.

.. _`ReadTheDocs`: https://readthedocs.org/

6. Set up Codacy

7. Set up Codecov




.. _`PyPI`: https://pypi.python.org/pypi
.. _`PyPI Help`: http://peterdowns.com/posts/first-time-with-pypi.html



