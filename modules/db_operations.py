"""
This module provides functions to add new articles to the database.
postgresql database
"""

# Add new article
def add_new_article(title, author, url, source):
    """Add new article to the database
    Args:
        title: title of the article
        date: date of the article publication
        author: author of the article
        source: source of the article
        url: url of the article
    """
    db = get_db()
    db.execute('INSERT INTO articles (title, author, year, isbn) VALUES (?, ?, ?, ?)',
               (title, author, url, source))
    db.commit()
    print('article added')


# Add new source
def add_new_source(name, url):
    """Add new source to the database"""
    db = get_db()
    db.execute('INSERT INTO sources (name, url) VALUES (?, ?)',
               (name, url))
    db.commit()
    print('Source added')

