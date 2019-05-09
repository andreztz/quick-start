import sys
import shutil
import zipfile

import click

from src.config import current_work_directory
from src.config import sample_zip


def wizard():
    pass


def unzip_file(file, extract_to):
    with zipfile.ZipFile(file, "r") as zip:
        zip.extractall(extract_to)


def rename_project(new_name):
    shutil.move("sample", new_name)


def main():
    unzip_file(sample_zip, current_work_directory)

    @click.command()
    @click.argument("project_name", nargs=1, default="sample")
    def add(project_name):
        rename_project(project_name)

    add()


if __name__ == "__main__":
    main()
