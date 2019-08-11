import zipfile

from pathlib import Path

import click

from quickstart.config import current_work_directory
from quickstart.config import sample_zip


def wizard():
    pass


def unzip_file(file, extract_to):
    with zipfile.ZipFile(file, "r") as zip:
        zip.extractall(extract_to)


def create_directory(path):
    path.mkdir()


def create_file(fname):
    open(fname, mode="a").close()


def create_package(path, name):
    path = Path(path) / name
    create_directory(path)
    create_file(path / "__init__.py")


def create_gitignore():
    pass


def create_setup():
    pass


def main():
    @click.group()
    def create():
        pass

    @create.command()
    @click.argument("path")
    @click.argument("name")
    def package(path, name):
        create_package(path, name)

    @create.command()
    @click.argument("name", nargs=1, default="sample")
    def project(name):
        path = current_work_directory / name
        unzip_file(sample_zip, path)

    cli = click.CommandCollection(sources=[create])
    cli()


if __name__ == "__main__":
    main()
