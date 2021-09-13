import scrapy
from scrapy.loader import ItemLoader

class ArticleSpider(scrapy.Spider):
    name = 'programming_historian'
    start_urls = ['https://programminghistorian.org/en/lessons/']

    

    def parse(self, response):
        self.logger.info(f'Parse funcion called on {response.url}')
        for article in response.css('div.lesson-description'):
            # loader = ItemLoader(item=Article(), selector=article)
            # loader.add_css('title', 'h2.title::text')
            # loader.add_css('date', 'time::text')
            # loader.add_css('description', 'p.description::text')
            # loader.add_css('url', 'a::attr(href)')
            # yield loader.load_item()
            article_url = article.css('a::attr(href)').get()
            yield response.follow(article_url, 
                    self.parse_article, 
                # meta={'article': article_item}
            )

        # BUILT FOR TESTING PURPOSES
        # query = response.css('div.lesson-description')
        # article_url = query.css('a::attr(href)').get()
        # yield response.follow(article_url, 
        #         self.parse_article, 
        #         # meta={'article': article_item}
        # )
            
    
    def parse_article(self, response):
        # article_item = response.meta['article']
        self.logger.info(f'Parse article funcion called on {response.url}')
        t = response.css('div.header-title')
        a = response.css('div.header-author')

        c = response.css('div.content')
        c = c.css('h1::text,h2::text,h3::text,a::text,p::text').getall()
        
        for i in range(len(c)):
            
            if c[i][-1] != '.' and c[i][0].isupper():
                c[i] += ' .'

        yield {
            'title': t.css('a::text').get(),
            'author_name': a.css('h2::text').get(),
            'text': ''.join(c),
        }


