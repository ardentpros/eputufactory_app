from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in eputufactory_app/__init__.py
from eputufactory_app import __version__ as version

setup(
	name="eputufactory_app",
	version=version,
	description="ERPNext customization for eputufactory",
	author="Olukayode",
	author_email="papadock95@hotmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
