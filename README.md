# Pynew

Automate the creation of new Python projects.

+ Virtual environment (pipenv) with dev packages installed
+ Git repository with `.gitignore` and an initial commit
+ Package directory with `__init__.py` and `__main__.py` (if not `--lib`)
+ Basic `setup.py`
+ `Readme.md` and `LICENSE` (choose from 10 available, default is MIT)
+ Default license and dev packages can be set on the configuration file


## Requirements:

+ [Pipenv](https://pipenv.org)
+ [Git](https://git-scm.com)


## Installation

I recommend installing with [pipsi](https://github.com/mitsuhiko/pipsi), but pip is also ok.

```shell
~ $ pipsi install git+https://github.com/cauebs/pynew#egg=pynew
```


## Usage

```shell
Usage: pynew [OPTIONS] PROJECT_NAME

  Create a new Python project

Options:
  --lib            Create a library instead of an executable
  -l, --license    Specify license to be used. Default: mit
  --help           Show this message and exit.
```


## Example

```shell
~ $ pynew example-project
Initializing virtual environment...
Installing dev packages...
Created project at example-project

~ $ exa -T example-project
example-project
├── example_project
│  ├── __init__.py
│  └── __main__.py
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
└── setup.py

~ $ cat example-project/setup.py
from setuptools import setup, find_packages

setup(
    name='example_project',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points='''
        [console_scripts]
        example-project=example_project.__main__:main
    ''',
)
```


## Available licenses

+ `agpl-3.0`
+ `apache-2.0`
+ `bsd-2-clause`
+ `bsd-3-clause`
+ `epl-2.0`
+ `gpl-2.0`
+ `gpl-3.0`
+ `lgpl-2.1`
+ `lgpl-3.0`
+ `mit`
+ `mpl-2.0`
+ `unlicense`


## Configuration

You can create the configuration file at `$XDG_CONFIG_HOME/pynew/config.json` (`~/.config/pynew/config.json`).

```json
{
    "user_name": "default: git config --get user.name",
    "default_license": "mit",
    "default_version": "0.1.0",
    "dev_packages":  ["flake8", "autopep8"]
}
```
