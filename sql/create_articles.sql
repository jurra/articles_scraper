-- Creation of article table
CREATE TABLE articles (
    article_id SERIAL PRIMARY KEY NOT NULL,
    datetime_created TIMESTAMP,
    datetime_accessed TIMESTAMP,
    title SMALLTEXT NOT NULL,
    full_text TEXT NOT NULL,
    author_name TEXT NOT NULL,
    source_url TEXT NOT NULL,
);

--Creation of source table
CREATE TABLE sources (
    source_id INTEGER PRIMARY KEY,
    source_name TEXT NOT NULL,
);