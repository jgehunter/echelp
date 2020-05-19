from setuptools import setup, setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
	name = "Electronic Circuits Helper",
	version = "0.0.0",
	author = "Jorge Hunter",
	author_email = "jgehunter@gmail.com",
	license = "MIT",
	packages = setuptools.find_packages(),
	long_description = long_description,
	)