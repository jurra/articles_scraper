from scrapy.item import Item, Field
from itemloaders.processors import MapCompose, TakeFirst
from datetime import datetime

# If author_name has an "and" or a comma, split and return array of authors

def split_authors(author_name):
    if "and" in author_name:
        return author_name.split("and")
    elif "," in author_name:
        return author_name.split(",")
    else:
        return [author_name]


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
