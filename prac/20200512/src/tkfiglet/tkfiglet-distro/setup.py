#!bin/python3

from setuptools import setup, find_packages

setup(
        name="tkfiglet",
        version="0.1",
        author="Me",
        author_email="qwe@jkl.org",
        description="No descr",
        url="https://jkl.org",
        install_requires=["pyfiglet"],
        packages=find_packages()
)
