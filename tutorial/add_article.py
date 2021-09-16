"""
This module provides functions to add new articles to the database.
postgresql database
"""
from importlib import resources
from sqlalchemy.sql import asc, desc, func, and_, or_
from tutorial.models import Article, Publisher, Author

def simply_add_new_article(
    session, 
    title,
    full_text,
    article_link,
    # accessed_date,
    publishing_date,):
    """Adds new article to the database"""
    # Check if article already exists
    article = (
        session.query(Article)
        .filter(Article.title == title)
        .one_or_none()
    )

    # Does the article already exist?
    if article is None:
        article = Article(
            title=title,
            full_text=full_text,
            article_link=article_link,
            # accessed_date=accessed_date,
            publishing_date=publishing_date
            )
        session.add(article)
        session.commit()
        print(f'Article "{title}" added to the database')
    else:
        print(f'Article "{title}" already exists in the database')
