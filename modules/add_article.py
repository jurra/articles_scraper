"""
This module provides functions to add new articles to the database.
postgresql database
"""
from importlib import resources
from sqlalchemy.sql import asc, desc, func, and_, or_
from modules.models import Article, Publisher, Collection, Author

# Add new article
def add_new_article(
    session, 
    article_title,
    article_text, 
    article_link,
    accessed_date,
    publishing_date,
    author_name, 
    publisher_name,
    publisher_url):
    """Add new article to the database"""
    # Get author's first and last name
    first_name, last_name = author_name.partition(' ')[0], author_name.partition(' ')
    
    # Check if article already exists
    article = (
        session.query(Article)
        .filter(
            and_(
                Article.title == article_title, 
                Article.author_first_name == first_name, 
                Article.author_last_name == last_name
            )
        )
        .filter(Article.publishers.any(Publisher.name == publisher_name))
        .one_or_none()
    )

    # Does the article by the author and publisher already exist?
    if article is None:
        return  
    
    # Check if the article exists for the author
    article_by_author = (
        session.query(Article)
        .join(Author)
        .filter(Article.title == article_title)
        .filter( and_(
            Author.first_name == first_name,
            Author.last_name == last_name
        ))
        .one_or_none()
    )

    # Create new article if needed
    if article_by_author is None:
        article = Article(
            title=article_title,
            text=article_text,
            link=article_link,
            accessed_date=accessed_date,
            publishing_date=publishing_date
            )

    # Get the author 
    author = (
        session.query(Author)
        .filter(
            and_(
                Author.first_name == first_name, 
                Author.last_name == last_name)
        )
        .one_or_none()
    )

    # Do we need to create the author?
    if author is None:
        author = Author(first_name=first_name, last_name=last_name)
        session.add(author)

    # Get the publisher
    publisher = (
        session.query(Publisher)
        .filter(Publisher.name == publisher_name)
        .one_or_none()
    )

    # Do we need to create the publisher?
    if publisher is None:
        publisher = Publisher(name=publisher_name, url=publisher_url)
        session.add(publisher)

    # Add the article to the publisher
    publisher.articles.append(article)

    # Add the author to the article
    article.authors.append(author)

    # Add the publisher to the article
    article.publishers.append(publisher)

    # Commit the changes
    session.commit()
    print(f'Article "{article_title}" added to the database')

