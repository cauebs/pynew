import json

from os import environ
from pathlib import Path

from .utils import run


try:
    CONFIG_DIR = Path(environ['XDG_CONFIG_HOME'], 'pynew')
except KeyError:
    CONFIG_DIR = Path.home() / '.config' / 'pynew'

try:
    with open(CONFIG_DIR / 'config.json') as f:
        config = json.load(f)
except FileNotFoundError:
    config = {}

USER_NAME = config.get('user_name') or run('git config --get user.name')
DEFAULT_LICENSE = config.get('default_license', 'mit')
DEFAULT_VERSION = config.get('default_version', '0.1.0')
DEV_PACKAGES = config.get('dev_packages', ['flake8', 'autopep8'])
