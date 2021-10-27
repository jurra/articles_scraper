# from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete, log

from src.models import *
from src.pipelines import ArticlesPipeline, DuplicatesPipeline
from src.spiders import spyder_mock as SpiderMock

from scrapy.exceptions import DropItem

import pandas
from datetime import *

from config import get_db_uri
from src.add_article import *

# Postgres username, password, and database name

postgres_str = get_db_uri()

# Connect to database and initialize a session
cnx = db_connect()
create_table(cnx)
Session = sessionmaker(bind=cnx)
s = Session()


def test_add_article():
    '''
    Check that article and relationship tables are created correctly
    '''
    a = Article(
        title="Example Title",
        full_text="Example Text",
        article_link="http://example.com",
        publishing_date=pandas.Timestamp("2018-01-01 00:00:00"),
    )

    # Add Article object to session
    simply_add_new_article(s, title=a.title,
                           full_text=a.full_text,
                           article_link=a.article_link,
                           publishing_date=a.publishing_date,
                           author="Felo Crawley"
                           )

    # Get article from the databse
    try:
        article_from_db = s.query(Article).filter_by(
            title="Example Title").one()
    except:
        article_from_db = None

    assert a.title == article_from_db.title

    au = s.query(Author).filter_by(name="Felo Crawley").first()
    a = s.query(Article).filter_by(title="Example Title").first()
    s.delete(au)
    s.delete(a)

    s.commit()


def test_add_article_from_pipeline():
    ''''
    Tests basic functionality of the add_article_from_pipeline function
    '''
    item = {
        'collection': 'Dummy collection',
        'collection_description': 'Dummy collection description',
        'title': 'Test title',
        'article_link': 'https://www.google.com',
        'publishing_date': '2020-01-01',
        'full_text': 'bla bla bla',
        'author_name': 'Test author'
    }

    # Here we use the article pipeline to add the article to the database
    pipe = ArticlesPipeline()

    # Here we use the SpiderMock to simulate the pipeline
    spider = SpiderMock

    # This should add the article to the database
    pipe.process_item(item, spider)

    # Query the database for the article
    article = s.query(Article).filter_by(title="Test title").first()
    assert article.title == 'Test title'

    # Test the duplicate pipeline
    pipe = DuplicatesPipeline()

    # if exception is raised, the article is not added to the database
    try:
        pipe.process_item(item, spider)

    except DropItem:
        pass

    # Remove author from the database
    au = s.query(Author).filter_by(name="Test author").first()
    s.delete(au)

    # Remove the article from the database and commit changes
    s.delete(article)
    s.commit()


def test_db_tables():
    '''
    Tests basic functionality relationsips between tables, it will create an Article 
    and relationships. Then it also tests the persistence of the relationships after the
    article is deleted
    '''
    # We create an article object
    a = Article()
    a.title = "Example Title"
    a.publishing_date = datetime.now()
    a.full_text = "Example Text"
    a.article_link = "http://example.com"

    # We create an author object and append the article to it
    au = Author()
    au.name = "Felo Crawley"
    a.authors.append(au)

    # We create a collection object and append it the collection to the article
    c = Collection()
    c.name = "Test collection"
    c.description = "Test collection description"
    a.collections.append(c)

    # We create a Publisher object and append it to the article
    p = Publisher()
    p.name = "Test publisher"
    p.url = "http://publisher.example.com"
    
    # Append the publisher to the article before adding it to db
    a.publishers.append(p)

    # Append publishers to author before adding the article to db
    au.publishers.append(p)

    # We add the article to the database once all relationships
    s.add(a)
    s.commit()

    # Now we want to test that the artcle has been created with all
    # the relationships

    # Make queries of all tables
    article = s.query(Article).filter_by(title="Example Title").first()
    collection = s.query(Collection).filter_by(name="Test collection").first()
    author = s.query(Author).filter_by(name="Felo Crawley").first()
    publisher = s.query(Publisher).filter_by(name="Test publisher").first()

    # Check for relationships between tables
    assert article.title == 'Example Title'
    assert article.collections[0].name == 'Test collection'
    assert article.publishers[0].name == 'Test publisher'
    assert article.authors[0].name == 'Felo Crawley'

    assert collection.name == 'Test collection'
    assert collection.articles[0].title == 'Example Title'

    assert author.name == 'Felo Crawley'
    assert author.articles[0].title == 'Example Title'
    assert author.publishers[0].name == 'Test publisher'

    assert publisher.name == 'Test publisher'
    assert publisher.articles[0].title == 'Example Title'
    assert publisher.authors[0].name == 'Felo Crawley'

    s.rollback()
    s.delete(article)
    s.delete(collection)
    s.delete(author)
    s.delete(publisher)
    s.commit()


# close sessions
s.close_all()
