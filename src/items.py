from scrapy.item import Item, Field
from itemloaders.processors import MapCompose, TakeFirst
from datetime import datetime

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
    
    author_name = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()    
        )     


