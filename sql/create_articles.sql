--Creation of source table
CREATE TABLE source (
    source_id SERIAL,
    source_name TEXT NOT NULL,
    source_url TEXT NOT NULL,
    PRIMARY KEY (source_id)
);

-- Creation of article table
CREATE TABLE article (
    article_id SERIAL,
    datetime_created TIMESTAMP,
    datetime_accessed TIMESTAMP,
    title TEXT NOT NULL,
    full_text TEXT NOT NULL,
    source_id SERIAL NOT NULL,
    PRIMARY KEY (article_id),
    CONSTRAINT fk_source
        FOREIGN KEY (source_id)
      REFERENCES source(source_id)
);


--Creation of author table
CREATE TABLE IF NOT EXISTS author (
    author_id SERIAL,
    author_first_name TEXT NOT NULL,
    author_last_name TEXT NOT NULL,
    PRIMARY KEY (author_id)
);

--Creation of collection table
CREATE TABLE IF NOT EXISTS articles_collection (
    collection_id SERIAL,
    collection_name TEXT NOT NULL,
    collection_description TEXT NOT NULL,
    PRIMARY KEY (collection_id)
);

--Create associatibe table for collection_articles_collection
CREATE TABLE IF NOT EXISTS collection_articles_collection (
    collection_id SERIAL REFERENCES articles_collection(collection_id),
    article_id SERIAL REFERENCES article(article_id),
    CONSTRAINT pk_collection_articles_collection 
        PRIMARY KEY (collection_id, article_id)    
);

-- Create associative table for article_author
CREATE TABLE IF NOT EXISTS article_author (
    article_id SERIAL REFERENCES article(article_id),
    author_id SERIAL REFERENCES author(author_id),
    CONSTRAINT pk_article_author
        PRIMARY KEY (article_id, author_id)
);