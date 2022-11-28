import os
from setuptools import setup

setup(
    name="my_app1",
    version="0.0.1",
    author="Jack Hong",
    author_email="jack.xu.hong@gmail.com",
    description="A simple python application",
    license="Public",
    keywords="simple python app",
    url="https://github.com/jackxuhong/python_template",
    packages=['my_app1', 'tests'],
    scripts=['bin/app1.sh', 'bin/app1.ps1'],
    data_files=[('etc', ['etc/app1.cfg.dev'])]
)
