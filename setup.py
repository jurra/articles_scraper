#! /usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="articles_mining",
    version="1.0",
    packages=find_packages(),
    entry_points = {'scrapy': ['settings = tutorial.settings']},
    install_requires=[
        "pandas",
        "Flask==1.1.1",
        "SQLAlchemy==1.3.13",
        "Flask-SQLAlchemy==2.4.1",
        "Flask-Cors==3.0.8",
        "Flask-Bootstrap4==4.0.2",
        "Flask-WTF==0.14.3",
        "python-dateutil==2.8.1",
        "python-dotenv==0.10.5",
        "treelib"
    ],
)
