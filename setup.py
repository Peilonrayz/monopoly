#!/usr/bin/env python
from setuptools import find_packages, setup

with open("README.rst") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="monopoly",
    version="0.0.0",
    license="MIT",
    description="Skeleton for Python projects.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    author="Peilonrayz",
    author_email="peilonrayz@gmail.com",
    url="https://peilonrayz.github.io/community_challenge_monopoly",
    project_urls={
        "Bug Tracker": "https://github.com/Peilonrayz/community_challenge_monopoly/issues",
        "Documentation": "https://peilonrayz.github.io/community_challenge_monopoly",
        "Source Code": "https://github.com/Peilonrayz/community_challenge_monopoly",
    },
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="",
    entry_points={"console_scripts": ["monopoly=monopoly.__main__:main"]},
)
