from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

article_author = Table(
    'article_author', 
    Base.metadata,
    Column('article_id', Integer, ForeignKey('article.id')),
    Column('author_id', Integer, ForeignKey('author.id'))
    )

collection_articles_collection = Table(
    'collection_articles_collection',
    Base.metadata,
    Column('collection_id', Integer, ForeignKey('collection.id')),
    Column('article_id', Integer, ForeignKey('article.id'))
    )

article_publisher = Table(
    'article_publisher',
    Base.metadata,
    Column('article_id', Integer, ForeignKey('article.id')),
    Column('publisher_id', Integer, ForeignKey('publisher.id'))
    )

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    datetime_created = Column(String)
    datetime_updated = Column(String)
    full_text = Column(String)
    authors = relationship(
        "Author",
        secondary=article_author,
        backref="publishers"
        )
    publishers = relationship(
        "Publisher",
        secondary=article_publisher,
        backref="authors"
        )

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    description = Column(String)
    articles = relationship(
        "Article",
        secondary=article_author,
        backref="authors"
    )

class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    articles = relationship(
        "Article",
        secondary=article_author,
        backref="publishers"
    )
    authors = relationship(
        "Author",
        secondary=article_publisher,
        backref="publishers"
    )

class Collection(Base):
    __tablename__ = 'collection'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    articles = relationship(
        "Article",
        secondary=collection_articles_collection,
        backref="collections"
    )