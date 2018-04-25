import setuptools

setuptools.setup(
    name="{{ cookiecutter.project_name }}",
    version="0.1",
    url="http://github.com/ESSS/{{ cookiecutter.project_name }}",
    author='ESSS',
    author_email='foss@esss.co',
    license = 'MIT',
    description="{{ cookiecutter.package_description }}",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)