from io import open
from setuptools import setup

version = "0.3.1"

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="check-password",
    version=version,

    author="pavelgs",
    author_email="p6282813@yandex.ru",

    description="lib for check password, email or date for validate",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/pavelglazunov/-check-password-",

    license="Apache License, Version 2.0, see LICENSE file",

    packages=["check-password"],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)