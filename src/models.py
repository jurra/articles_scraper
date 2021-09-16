from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from scrapy.utils.project import get_project_settings
from config import config


# Postgres username, password, and database name
params = config()
postgres_str = ('postgresql+psycopg2://{username}:{password}@{ipaddress}:{port}'
.format(
    username=params["user"],
    password=params["password"],
    ipaddress=params["host"],
    dbname=params["database"],
    port=params["port"]))

Base = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(postgres_str)

def create_table(engine):
    Base.metadata.create_all(engine)


article_author = Table(
    'article_author',
    Base.metadata,
    Column('article_id', Integer, ForeignKey('article.id'), primary_key=True),
    Column('author_id', Integer, ForeignKey('author.id'), primary_key=True)
)

# collection_articles_collection = Table(
#     'collection_articles_collection',
#     Base.metadata,
#     Column('collection_id', Integer, ForeignKey('collection.id'), primary_key=True),
#     Column('article_id', Integer, ForeignKey('article.id'), primary_key=True)
# )

article_publisher = Table(
    'article_publisher',
    Base.metadata,
    Column('article_id', Integer, ForeignKey('article.id'), primary_key=True),
    Column('publisher_id', Integer, ForeignKey('publisher.id'), primary_key=True)
)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    # accessed_date = Column(String)
    publishing_date = Column(String)
    # description = Column(String)
    full_text = Column(String)
    # publishing_date=Column(String)
    article_link = Column(String)

    authors = relationship("Author",
                                secondary=article_author,
                                back_populates="articles")

    publishers = relationship("Publisher",
                                secondary=article_publisher, 
                                back_populates="articles")



class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # last_name = Column(String)
    # article_id = Column(Integer, ForeignKey('article.id'))
    # publisher_id = Column(Integer, ForeignKey('publisher.id'))

    articles = relationship("Article",
                            secondary=article_author, 
                            back_populates="authors")
    # publishers = relationship("Publisher",
    #                         secondary=article_publisher,
    #                         back_populates="authors")


class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
    articles = relationship("Article",
                            secondary=article_publisher, 
                            back_populates="publishers")

    # authors = relationship("Author", 
    #                         secondary=article_author,
    #                         back_populates="publishers")


# class Collection(Base):
#     __tablename__ = 'collection'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     articles = relationship(
#         "Article",
#         secondary=collection_articles_collection,
#         backref="collection")