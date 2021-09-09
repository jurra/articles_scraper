# Coding session postgres, SQLAlchemy and python for a datapipeline

## Motivation
- Consultation project Public Discourse Miner. 

## Explain the use case
- How everything was setup in the project
- How it should be for more reusability and interoperability. The need for a database

## Stack selection and design
- postgresql
    1. **Full text search** Postgres can easily store vector representations of text you're storing and allow super fast queries on it. This is handy for things like autocompleting search fields in websites, as well as data science projects using natural language processing.
    2. **portable server**

- SQLAlchemy

- Alembic: is used as part of the iteration of modeling tables and relationships

- scrapy
- docker and docker-compose workflow

### Some mistakes I made in previous designs
- Trying to make a very complicated system with sqlite3 pointing to files, due to a previous project I worked on and an experiment I wanted to make. The learning is that you have to distantiate your agenda from the real need of the project, and find a middle ground, where you really need to apply whats needed.
- Learn the best practice of the particular thing and domain you are trying to do.

## Practicing for learning
SQLAlchemy abstract a lot of aspects of SQL to be more productive. For learning purposes is good to practice SQL language directly and then with psycog passing SQL strings, this will give an idea about the underlying processes and mechanism behind the scenes.

> SQA provides us with an abstraction layer above raw SQL and allows us to work with tables and queries as objects in Python. Usually, with SQA you don't write any raw SQL in Python anymore since SQA handles almost everything you would need as regular methods and functions.

> Unfortunately, this makes it not a great way to learn SQL. It's highly recommended you learn how SQL works before using an abstraction of it.

> Another downside is that it's sometimes hard to figure out how to achieve the same result with SQA as you would with a plain SQL query. Once you get the hang of the API, though, working with SQA is quite nice and all the code is very obvious and clean.


## Important learning about best practices
- You do everything in python except creating the server and the DB
- You work directly on SQLAlchemy with python
- environment variables (see how is done in the other project)
- Migrations

> When testing different models and relationships you'll often create and destroy databases until it's all sorted out. For this, we'll create a function to recreate the database:

- Using sessions to hold state in the ORM layer without changing data in the database
> Sessions also hold any data you've queried from the database as Python objects. You can make changes to the objects in the session and commit back to the database if needed. Having to do all of this with raw SQL and parsing would be quite a task, but sessions make it easy.

```py
### crud.py ###

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
```
### Conventions
#### Project structure
```
project
   config.py
   crud.py
   models.py
```

## Key concepts
- Engine
- Sessions
- Tables
- Relationships
- ORMs (Object relational mapping)

## Summary
- Learned how to do basic operations with SQLalchemy
- Got a perspective on how you work with SQLAlchemy and the workflow


## Troubleshooting
### Getting inside container and checking if db exists
```
docker exec -it <container-name> bash

# Inside the container:
:/# psql -U postgres

# Inside postgress check if database exists
postgres=# \c <db-name>

```