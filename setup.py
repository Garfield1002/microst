# -*- coding: utf-8 -*-

from setuptools import setup


with open("Readme.md") as f:
    readme = f.read()


setup(
    name="microst",
    version="0.1.0",
    description="micro serial terminal",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Jack Royer",
    author_email="jack.royer.23@gmail.com",
    license="MIT",
    url="https://github.com/makerdiary/terminal-s",
    entry_points={
        "console_scripts": ["microst=microst.microst:main"],
    },
    packages=["microst"],
    include_package_data=False,
    install_requires=["pyserial"],
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["serial", "terminal"],
)
