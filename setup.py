# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in pni_only_customizations/__init__.py
from pni_only_customizations import __version__ as version

setup(
	name='pni_only_customizations',
	version=version,
	description='PNI Site Only Customizations',
	author='Jigar Tarpara',
	author_email='team@khatavahi.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
