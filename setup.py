from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in customer_ledger/__init__.py
from customer_ledger import __version__ as version

setup(
	name="customer_ledger",
	version=version,
	description="Customer Ledger Report",
	author="Smart Solutions",
	author_email="ahmed.younis_6@hotmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
