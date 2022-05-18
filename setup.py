import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='timestamps',
      description='Python backend for scripts to generate timestamps',
      classifiers=[
        'Programming Language :: Python :: 3.7',
      ],
      keywords='python, flask',
      url='',
      author='Merishka Lalla',
      author_email='merish.lalla@gmail.com',
      packages=find_packages(),
      install_requires=required)
