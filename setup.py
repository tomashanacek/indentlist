# -*- coding: utf-8 -*-

from distutils.core import setup
from indent_list import __version__

classifiers = ["Programming Language :: Python",
               "Intended Audience :: Developers",
               "License :: OSI Approved :: MIT License",
               "Topic :: Software Development :: Libraries :: Python Modules"]

setup(
    name="indentlist",
    version=__version__,
    description=("Indent list context manager"),
    author="Tomas Hanacek",
    author_email="tomas.hanacek1@gmail.com",
    url="https://github.com/tomashanacek/indentlist",
    license="MIT",
    packages=["indent_list"],
    classifiers=classifiers
)
