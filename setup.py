from setuptools import setup, find_namespace_packages

__version__ = '0.0.1'

setup(
    name='request framework',
    description='reuest framework study',
    version=__version__,

    author='Volodymyr Tkachenko',
    author_email='volodymyr.tkachenko93@gmail.com',

    python_requires='>=3.8.7',

    install_requires=[
        'pytest',
        'flask',
        'requests'
    ],
)
