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
        session = self.Session()
        a = Article()
        a.title = item['title']
        a.article_link = item['article_link']
        a.full_text = item['full_text']
        a.publishing_date = item['publishing_date']

        try:
            session.add(a)
            session.commit()
            print("Article sucessfully added")
        except:
            session.rollback()
            print('Failed to add article')
            raise 
        finally:
            session.close()

        return item