# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from src.models import *

from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose
from scrapy.exceptions import DropItem

# import session maker from SQLAlchemy
from sqlalchemy.orm import session, sessionmaker


class ArticlesPipeline(object):
    def __init__(self):
        '''
        Initializes database connection and session maker
        Creates tables
        '''
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
        print("Connected successfully to database")

    def process_item(self, item, spider):
        '''
        Saves articles to database
        The method is called for every ArticleItem
        '''

        # Create article object
        session = self.Session()
        a = Article()

        try:
            # If article.name is not in database, add the article
            if session.query(Article).filter(Article.title == item['title']) is None:
                a.title = item['title']
                a.article_link = item['article_link']
                a.full_text = item['full_text']
                a.publishing_date = item['publishing_date']

                # Create author if it doesnt exist in the database
                au = Author()
                au.name = item['author_name']

                # Check if author exists in database, if not, add the author
                if session.query(Author).filter(Author.name == item['author_name']) is None:
                    session.add(au)
                    session.commit()

                # Append relationship between article and author
                a.authors.append(au)

                # Add article to database
                session.add(a)
                session.commit()
                print("Article and properties sucessfully added")
            
            else:
                print("Article already exists in database")

        # # Create collection object
        # if session.query(Collection).filter(Collection.name == item['collection']).count() == 0:
        #     co = Collection(
        #         name=item['collection'],
        #         description=item['collection_description'],
        #     )
        # else:
        #     co = session.query(Collection).filter(Collection.name == item['collection']).one()

        # # Add collection to article
        # a.collections.append(co)

        except:
            session.rollback()
            print('Failed to add article')
            raise
        finally:
            session.close()

        return item

class DuplicatesPipeline(object):
    def __init__(self):
        '''
        Initializes database connection and session maker
        Creates tables
        '''
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
        print("Connected successfully to database")
        
    def process_item(self, item, spider):
        session = self.Session()
        exist_article = session.query(Article).filter(Article.title == item['title']).count()
        if exist_article > 0:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            return item
