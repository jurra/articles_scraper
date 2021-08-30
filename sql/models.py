from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base

author = Table(
    'author', 
    Base.metadata,
    Column('author_id', Integer, ForeignKey('author.id')),
    Column('article', Integer, ForeignKey('article.id'))
)

source = Table(
    'source',
    Base.metadata,
    Column('source_id', Integer, ForeignKey('source.id')),
    Column('date', DateTime),
    Column('published_date', DateTime),
    Column('article', Integer, ForeignKey('article.id'))
)

article = Table(
    'article',
    Base.metadata,
)