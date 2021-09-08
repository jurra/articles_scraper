from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modules.models import *
from modules.add_article import *

import pandas

from datetime import *

from examples.my_articles_setup.config import config

# Postgres username, password, and database name
params = config()

postgres_str = ('postgresql+psycopg2://{username}:{password}@{ipaddress}:{port}/{dbname}'
.format(
    username=params["user"],
    password=params["password"],
    ipaddress=params["host"],
    dbname=params["database"],
    port=5432)
)

# Create the connection
cnx = create_engine(postgres_str)
Base.metadata.bind = cnx
Base.metadata.create_all(cnx)

Session = sessionmaker(bind=cnx)        
s = Session()  

def test_add_article():
    a = Article(
    title="Example Title",
    full_text="Example Text", 
    article_link="http://example.com",
    accessed_date=pandas.Timestamp("2018-01-01 00:00:00"),
    publishing_date=pandas.Timestamp("2018-01-01 00:00:00"),)

    # Add new simple article
    simply_add_new_article(s, title=a.title,
                           full_text=a.full_text,
                           article_link=a.article_link,
                           accessed_date=a.accessed_date,
                           publishing_date=a.publishing_date)

    # Get article from the databse
    try:
        article_from_db = s.query(Article).filter_by(title="Example Title").one()
    except:
        article_from_db = None
    
    assert a.title == article_from_db.title
    
    # Remove the article from the database and commit changes
    s.delete(article_from_db)
    s.commit()
    

# close sessions
s.close_all()

