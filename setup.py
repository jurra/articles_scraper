#! /usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="articles_mining",
    version="1.0",
    packages=find_packages(),
    entry_points = {'scrapy': ['settings = src.settings']},
    install_requires=[
        "pandas",
        "SQLAlchemy==1.3.13",
        "python-dateutil==2.8.1",
        "python-dotenv==0.10.5",
        "psycopg2-binary==2.9.1",
        "scrapy==2.5.0",
        "pytest==6.2.5"
    ],
)
