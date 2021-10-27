'''
This scraper is used as part of the test suite to mock the pipeine
It is not intended to be used in production
It is also meant to be used with the docker-compose service static website
this is the website that will be crawled by this scraper on localhost:5080
'''
import scrapy
from scrapy.loader import ItemLoader
from src.items import ArticleItem


class Mock(scrapy.Spider):
    name = 'Mock'

    # Here I am not using at the moment the mock because its
    # being declared in the test file itself
    def parse_article(self):
        loader = ItemLoader(item=ArticleItem(), response=None)
        article_item = loader.load_item()
        yield article_item
