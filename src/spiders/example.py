import scrapy
from scrapy.loader import ItemLoader
from src.items import ArticleItem

class ArticleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['https://programminghistorian.org/en/lessons/']
    # collection = name
    # description = "A ver popular website for digital humanities"

    def parse(self, response):
        self.logger.info(f'Parse funcion called on {response.url}')
        for article in response.css('div.lesson-description'):
            article_url = article.css('a::attr(href)').get()
            yield response.follow(article_url, self.parse_article)

        # # BUILT FOR TESTING PURPOSES
        # q = response.css('div.lesson-description')
        # article_url = q.css('a::attr(href)').get()
        # yield response.follow(article_url, self.parse_article)
                
    def parse_article(self, response):
        # article_item = response.meta['article']
        self.logger.info(f'Parse article funcion called on {response.url}')
        
        # get article title
        t = response.css('div.header-title')
        t = t.css('a::text').get()

        # get the article author
        a = response.css('div.header-author')
        a = a.css('h2::text').get().strip()

        # get the article content
        c = response.css('div.content')
        c = c.css('h1::text,h2::text,h3::text,a::text,p::text').getall()
        
        # Add points at the end of the headers 
        for i in range(len(c)):
            if c[i][-1] != '.' and c[i][0].isupper():
                c[i] += '. ' 
        
        c = ''.join(c)

        
        # Publihsed date
        p = response.xpath('//div[@class="metarow"]').re_first(r'\d{4}\-\d{2}\-\d{2}')

        loader = ItemLoader(item=ArticleItem(), selector=response)
        loader.add_value('title', t)
        loader.add_value('author_name', a)
        loader.add_value('full_text', c)
        loader.add_value('publishing_date', p)
        # loader.add_value('collection', self.collection)
        # loader.add_value('collection_description', self.description)
        loader.add_value('article_link', response.url)
        article_item = loader.load_item()

        yield article_item


