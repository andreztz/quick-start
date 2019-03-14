import os
import zipfile


# Config
root_dir = os.path.dirname(os.path.abspath(__file__))
sample_folder = os.path.join(root_dir, "sample")
sample_zip = os.path.join(root_dir, "sample.zip")
current_work_directory = os.getcwd()


def unzip_file(file, extract_to):
    with zipfile.ZipFile(file, "r") as zip:
        zip.extractall(extract_to)


def main():
    unzip_file(sample_zip, current_work_directory)


if __name__ == "__main__":
    main()
