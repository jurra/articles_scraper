# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from src.models import *

from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose

# import session maker from SQLAlchemy
from sqlalchemy.orm import sessionmaker


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

        # If article.name is not in database, add the article
        # if session.query(Article).filter(Article.title == item['title']).count() == 0:
        a.title = item['title']
        a.article_link = item['article_link']
        a.full_text = item['full_text']
        a.publishing_date = item['publishing_date']

        # Create author if it doesnt exist in the database
        au = Author()
        au.name = item['author_name']


        # Get the author name from the database
        # au.name = item['author']
        # query_author = session.query(Author).filter(Author.name == item['author_name']).one()
        
        # if query_author is None:
        #     a.authors.append(au)
        # else:
        #     au.name = query_author.name
        
        # Add authors to article
        a.authors.append(au)
        
        # Add article and author to session
        session.add(au)
        session.add(a)
        session.commit()

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

        try:
            print("Article and properties sucessfully added")
        except:
            session.rollback()
            print('Failed to add article')
            raise 
        finally:
            session.close()

        return item