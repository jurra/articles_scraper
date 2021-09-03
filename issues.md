## Todo:
- [ ] write crud module properly
- [ ] Write the db properly from SQLAlchemy

## Wrong relationships:
**Expected behavior** Commit changes to database
```
InvalidRequestError: One or more mappers failed to initialize - can't proceed with initialization of other mappers. Triggering mapper: 'mapped class Article->article'. Original exception was: Could not determine join condition between parent/child tables on relationship Article.publishers - there are no foreign keys linking these tables.  Ensure that referencing columns are associated with a ForeignKey or ForeignKeyConstraint, or specify a 'primaryjoin' expression.

```
## Feature: add_new_article
Consider all the checks to add an article

## Learn how to insert objects that have relations

## Remove config.py from .gitignore

## Fix names of examples 

## Do the migration exercise

## Fix the dockercompose file so that the tables are not created from the .sql scripts