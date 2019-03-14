import os
from setuptools import setup
from setuptools import find_packages


def readme():
    with open("README.md") as f:
        return f.read()


def requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


package = {
    "name": "start-my-project",
    "version": "0.0.1",
    "description": "start my project",
    "long_description": readme(),
    "long_description_content_type": "text/markdown",
    "keywords": "start my project",
    "author": "André P. Santos",
    "author_email": "andreztz@gmail.com",
    "url": "http://github.com/andreztz/start-my-project",
    "license": "MIT",
    "packages": find_packages(),
    "install_requires": requirements(),
    "entry_points": {"console_scripts": ["pyinit=src.__main__:main"]},
    "classifiers": [
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
}


setup(**package)
