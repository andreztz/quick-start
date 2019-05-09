# Arquivo responsável por gerenciar as configurações do usuário.

from configparser import ConfigParser
from pathlib import Path

from appdirs import user_config_dir
from appdirs import user_data_dir


base_dir = Path(__file__).parent
project_root = base_dir.parent

sample_folder = base_dir / "sample"
sample_zip = base_dir / "sample.zip"
config_ini = project_root / "config.ini"
current_work_directory = Path.cwd()
workspace = Path.home() / "WORKSPACE"

config_default = {"WORKSAPCE": workspace}

config = ConfigParser(config_default)
config.read(config_ini)
default_config = dict(config["default"])
