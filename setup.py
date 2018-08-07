#!/usr/bin/env python

install_requires = ['pyotp']

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyotp_cli",
    version="0.1.1",
    url="https://github.com/jcjveraa/pyotp_cli",
    license="GNU GPLv3",
    author="Jelle Veraa",
    author_email="3942301+jcjveraa@users.noreply.github.com",
    description="A small example package",
    install_requires=install_requires,
    long_description=long_description,
    long_description_content_type="text/markdown",
    test_suite="test",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)