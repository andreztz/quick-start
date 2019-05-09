from setuptools import setup
from setuptools import find_packages


def readme():
    with open("README.md") as f:
        return f.read()


def requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


package = {
    "name": "start-project",
    "version": "0.0.1",
    "description": "start project",
    "long_description": readme(),
    "long_description_content_type": "text/markdown",
    "keywords": "start project",
    "author": "André P. Santos",
    "author_email": "andreztz@gmail.com",
    "url": "http://github.com/andreztz/start-project",
    "license": "MIT",
    "packages": find_packages(),
    "install_requires": requirements(),
    "include_package_data": True,
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
