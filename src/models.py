from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from scrapy.utils.project import get_project_settings
from config import config, get_db_uri


# Postgres username, password, and database name
postgres_str = get_db_uri()

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(postgres_str)


def create_table(engine):
    Base.metadata.create_all(engine)


# Secondary table for many-to-many relationships
article_author = Table(
    'article_author',
    Base.metadata,
    Column('article_id', Integer, ForeignKey('article.id'), primary_key=True),
    Column('author_id', Integer, ForeignKey('author.id'), primary_key=True)
)

collection_articles = Table(
    'collection_articles',
    Base.metadata,
    Column('collection_id', Integer, ForeignKey(
        'collection.id'), primary_key=True),
    Column('article_id', Integer, ForeignKey('article.id'), primary_key=True)
)

article_publisher = Table(
    'article_publisher',
    Base.metadata,
    Column('article_id', Integer, ForeignKey('article.id'), primary_key=True),
    Column('publisher_id', Integer, ForeignKey(
        'publisher.id'), primary_key=True)
)

author_publisher = Table(
    'author_publisher',
    Base.metadata,
    Column('author_id', Integer, ForeignKey('author.id'), primary_key=True),
    Column('publisher_id', Integer, ForeignKey(
        'publisher.id'), primary_key=True)
)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    publishing_date = Column(String)
    full_text = Column(String)
    article_link = Column(String)

    authors = relationship("Author",
                           secondary=article_author,
                           back_populates="articles")

    publishers = relationship("Publisher",
                              secondary=article_publisher,
                              back_populates="articles")

    collections = relationship("Collection",
                               secondary=collection_articles,
                               back_populates="articles")


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    articles = relationship("Article",
                            secondary=article_author,
                            back_populates="authors")

    publishers = relationship("Publisher",
                              secondary=author_publisher,
                              back_populates="authors")


class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)

    articles = relationship("Article",
                            secondary=article_publisher,
                            back_populates="publishers")

    authors = relationship("Author",
                           secondary=author_publisher,
                           back_populates="publishers")


class Collection(Base):
    __tablename__ = 'collection'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    articles = relationship(
        "Article",
        secondary=collection_articles,
        back_populates="collections")
