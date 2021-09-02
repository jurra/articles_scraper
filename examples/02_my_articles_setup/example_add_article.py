from sqlalchemy.orm.session import sessionmaker
import modules.add_article as articles
from sqlalchemy import and_, create_engine, engine
from sqlalchemy.orm import sessionmaker
from config import config
import pandas

params = config()

postgres_str = ('postgresql://{username}:{password}@{ipaddress}:{port}/{database}'
.format(
    username=params["user"],
    password=params["password"],
    ipaddress=params["host"],
    database=params["database"],
    port=5332)
)

engine = create_engine(postgres_str)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

articles.add_new_article(
    session=session, 
    article_title="Example Title",
    article_text="Example Text", 
    article_link="http://example.com",
    accessed_date=pandas.Timestamp("2018-01-01 00:00:00"),
    publishing_date=pandas.Timestamp("2018-01-01 00:00:00"),
    author_name="Example Author",
    publisher_name="Example Publisher",
    publisher_url="http://example.publisher.org"
)