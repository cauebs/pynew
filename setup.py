from setuptools import setup, find_packages


setup(
    name='pynew',
    description='Automate Python project creation',
    version='0.1.2',
    author='Cauê Baasch de Souza',
    author_email='cauebs@pm.me',
    url='https://github.com/cauebs/pynew',
    license='MIT',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
    ],
    packages=find_packages(),
    install_requires=['click'],
    entry_points={
        'console_scripts': ['pynew = pynew.__main__:main'],
    },
)
