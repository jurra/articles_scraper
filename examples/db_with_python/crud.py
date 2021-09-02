### crud.py ###
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from datetime import *

from examples.db_with_python.models import *
import examples.db_with_python.config as config


engine = create_engine(config.get_db_uri()) # this shouldnt be here
Session = sessionmaker(bind=engine)         # this shouldnt be here
s = Session()    # set                      # this shouldnt be here

# Create all tables from models
Base.metadata.create_all(engine)

'''
TODO: The creation of the engine and session should not be part of the crud
module, instead a session object should be passed to the functions
'''
def add_book(title, author, pages ,published):
    book = Book(title=title,author=author,
                pages=pages,published=published,)
    s.add(book)
    s.commit()


