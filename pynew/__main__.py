from os import chdir
from pathlib import Path

import click

from .config import DEFAULT_LICENSE, DEV_PACKAGES, DEFAULT_VERSION
from .file_contents import MAIN_PY, BIN_SETUP_PY, LIB_SETUP_PY, GITIGNORE
from .licenses import LICENSES
from .utils import run


@click.command(help='Create a new Python project')
@click.argument('project_name')
@click.option('--lib', is_flag=True, default=False,
              help='Create a library instead of an executable')
@click.option('--license', '-l', type=click.Choice(LICENSES.keys()),
              help='Specify license to be used. Default: mit')
def main(project_name, lib, license):
    project_name = project_name.replace('_', '-')
    package_name = project_name.replace('-', '_')

    project_dir = Path() / project_name
    project_dir.mkdir()

    package_dir = project_dir / package_name
    package_dir.mkdir()

    (package_dir / '__init__.py').touch()
    if not lib:
        with (package_dir / '__main__.py').open('w') as f:
            f.write(MAIN_PY)

    with (project_dir / 'LICENSE').open('w') as f:
        f.write(LICENSES[license or DEFAULT_LICENSE])

    with (project_dir / 'README.md').open('w') as f:
        f.write(f"# {project_name.replace('_', ' ').title()}\n")

    with (project_dir / '.gitignore').open('w') as f:
        f.write(GITIGNORE)

    with (project_dir / 'setup.py').open('w') as f:
        if not lib:
            f.write(BIN_SETUP_PY.format(package_name=package_name,
                                        version=DEFAULT_VERSION,
                                        project_dir=project_dir))
        else:
            f.write(LIB_SETUP_PY.format(package_name=package_name,
                                        version=DEFAULT_VERSION))

    chdir(project_dir)

    click.echo('Initializing virtual environment...')
    run('pipenv sync')

    click.echo('Installing dev packages...')
    run(f'pipenv install -d {" ".join(DEV_PACKAGES)}')
    run('pipenv lock')

    run('git init')
    run('git add *')
    run('git commit -m "Initial commit"')

    click.echo(f'Created project at {project_dir}')


if __name__ == '__main__':
    main()
