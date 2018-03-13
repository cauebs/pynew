from setuptools import setup, find_packages


setup(
    name='pynew',
    version='0.1.1',
    packages=find_packages(),
    install_requires=['click'],
    entry_points={
        'console_scripts': ['pynew = pynew.__main__:main'],
    },
)
