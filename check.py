'''
This is a quick check to make sure the workflow is working as expected.
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modules.models import *
from modules.add_article import *
import pandas

from datetime import *

from config import config

# Postgres username, password, and database name
params = config()

postgres_str = ('postgresql+psycopg2://{username}:{password}@{ipaddress}:{port}'
.format(
    username=params["user"],
    password=params["password"],
    ipaddress=params["host"],
    port=params["port"])
)

# Create the connection
cnx = create_engine(postgres_str)
Base.metadata.bind = cnx
Base.metadata.create_all(cnx)

Session = sessionmaker(bind=cnx)        
s = Session()    # set  

# Add the two nodes on respective tables
article = Article(
    title="Example Title",
    full_text="Example Text", 
    article_link="http://example.com",
    accessed_date=pandas.Timestamp("2018-01-01 00:00:00"),
    publishing_date=pandas.Timestamp("2018-01-01 00:00:00"),
)

# Insert some data
author  = Author(
    first_name="Fidelia",
    last_name="Example Author"
)

publisher = Publisher(
    name="Example Publisher",
    url="http://example.publisher.org"
)

try:
    s.add(article)
    s.add(author)
    s.add(publisher)
    article.authors.append(author) # Add relationship to the children property
    article.publishers.append(publisher) # Add relationship to the children property
except:
    s.rollback()
    raise
else:
    s.commit()