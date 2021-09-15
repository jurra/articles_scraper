# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from tutorial.models import *

# import session maker from SQLAlchemy
from sqlalchemy.orm import sessionmaker


class TutorialPipeline:
    def process_item(self, item, spider):
        return item

class SavesArticlesPipeline(object):
    def __init__(self):
        '''
        Initializes database connection and session maker
        Creates tables
        '''
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

        
    def process_item(self, item, spider):
        '''
        Saves articles to database
        The method is called for every ArticleItem
        '''
        session = self.Session()
        article = Article(**item)

        try:
            session.add(article)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item