import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='projects',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyyaml'
    ],
    license='BSD License',
    description='Handle projects initialization',
    long_description=README,
    author='Gosia Jurkiewicz',
    author_email='gosia.jurkiewicz@gmail.com',
    classifiers=[],
    entry_points={
        'console_scripts': [
            'proj = projects.proj:run',
        ]
    }
)
