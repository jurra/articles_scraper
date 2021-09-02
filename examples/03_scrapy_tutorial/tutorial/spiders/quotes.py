import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        quote_count = 0

        for quote in response.css('div.quote'):
            # write to file quote{count}.txt in the data/ directory
            filename = '../data/quote-{}.txt'.format(quote_count)
            with open(filename, 'w') as f:
                f.write(quote.css('span.text::text').get())
                f.write(quote.css('small.author::text').get())
                f.write(quote.css('div.tags::text').getall())
            quote_count += 1

    