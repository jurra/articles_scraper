# from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import *

import pandas

from datetime import *

from config import config
from src.add_article import *

# Postgres username, password, and database name
params = config()

postgres_str = ('postgresql+psycopg2://{username}:{password}@{ipaddress}:{port}'
.format(
    username=params["user"],
    password=params["password"],
    ipaddress=params["host"],
    dbname=params["database"],
    port=params["port"]))

# Connect to database and initialize a session
cnx = db_connect()
create_table(cnx)
Session = sessionmaker(bind=cnx)        
s = Session()  

def test_add_article():
    # Create Article object
    a = Article(
    title="Example Title",
    full_text="Example Text", 
    article_link="http://example.com",
    # accessed_date=pandas.Timestamp("2018-01-01 00:00:00"),
    publishing_date=pandas.Timestamp("2018-01-01 00:00:00"),
    )

    # Add Article object to session
    simply_add_new_article(s, title=a.title,
                           full_text=a.full_text,
                           article_link=a.article_link,
                           publishing_date=a.publishing_date,
                           author = "Felo Crawley"
                           )

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

