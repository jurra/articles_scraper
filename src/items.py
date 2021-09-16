from scrapy.item import Item, Field
from itemloaders.processors import MapCompose, TakeFirst
from datetime import datetime

'''
/home/jurra/work/projects/docker_postgres_with_data/examples/03_scrapy_tutorial/tutorial/items.py:8: ScrapyDeprecationWarning: 
scrapy.loader.processors.MapCompose is deprecated,
 instantiate itemloaders.processors.MapCompose instead.

'''
class ArticleItem(Item):
    title = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
        )
    article_link = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
        )
    publishing_date = Field(
        input_processor=MapCompose(str.strip),
        outut_processor=TakeFirst()
    )

    full_text = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
        )
    name = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()    
        )     


