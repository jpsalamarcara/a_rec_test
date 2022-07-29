import os

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    REQUIRED = f.read().split('\n')

with open('README.md') as f:
    readme = f.read()


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


resource_files = package_files('camera_simulator/resources')

setup(
    name='camera_simulator',
    version='0.1.0',
    description='Camera Simulator by Juan',
    long_description=readme,
    author='Juan Pablo Salamanca Ramirez',
    author_email='juan.salamanca.r@icloud.com',
    url='https://github.com/jpsalamarcara/a_rec_test',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=REQUIRED,
    package_data={'': resource_files},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pysensor=camera_simulator.core.commands.mymean:execute'
        ]
    },
)
