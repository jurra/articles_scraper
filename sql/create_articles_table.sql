-- Creation of publisher table
CREATE TABLE publisher (
    publisher_id INT NOT NULL,
    publisher_name TEXT NOT NULL,
    publisher_url TEXT NOT NULL,
    publisher_description TEXT NOT NULL,
    PRIMARY KEY (publisher_id)
);

-- Creation of article table
CREATE TABLE article (
    article_id INT NOT NULL,
    datetime_created TIMESTAMP,
    datetime_accessed TIMESTAMP,
    title TEXT NOT NULL,
    full_text TEXT NOT NULL,
    publisher_id INT NOT NULL,
    PRIMARY KEY (article_id),
    CONSTRAINT fk_publisher
        FOREIGN KEY (publisher_id)
      REFERENCES publisher(publisher_id)
);


-- Creation of author table
CREATE TABLE IF NOT EXISTS author (
    author_id INT NOT NULL,
    author_first_name TEXT NOT NULL,
    author_last_name TEXT NOT NULL,
    PRIMARY KEY (author_id)
);

-- Creation of collection table
CREATE TABLE IF NOT EXISTS articles_collection (
    collection_id INT NOT NULL,
    collection_name TEXT NOT NULL,
    collection_description TEXT NOT NULL,
    PRIMARY KEY (collection_id)
);

-- Create associative table for collection_articles_collection
CREATE TABLE IF NOT EXISTS collection_articles_collection (
    collection_id INT REFERENCES articles_collection(collection_id),
    article_id INT REFERENCES article(article_id),
    CONSTRAINT pk_collection_articles_collection 
        PRIMARY KEY (collection_id, article_id)    
);

-- Create associative table for article_author
CREATE TABLE IF NOT EXISTS article_author (
    article_id INT NULL REFERENCES article(article_id),
    author_id INT NULL REFERENCES author(author_id),
    CONSTRAINT pk_article_author
        PRIMARY KEY (article_id, author_id)
);