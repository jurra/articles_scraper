## Next steps
- [ ] Add articles to items
- [ ] Add item to the pipeline and the database
- [ ] 

## Todo:
- [ ] write crud module properly
- [ ] Write the db properly from SQLAlchemy

## Feature: add_new_article to database
- [x] Done in a simply add article unit tests
- [] Consider all the checks to add an article
- [] Implement pipeline example with scrapy

## Bug: config parse working for root level, not for tutorial level
It works even when I run the config at the root level

## Remove config.py from .gitignore

## Fix names of examples to tutorials

## Create the real examples later

## Do the migration exercise

## (Fixed) Wrong relationships:
**Expected behavior** Commit changes to database
```
InvalidRequestError: One or more mappers failed to initialize - can't proceed with initialization of other mappers. Triggering mapper: 'mapped class Article->article'. Original exception was: Could not determine join condition between parent/child tables on relationship Article.publishers - there are no foreign keys linking these tables.  Ensure that referencing columns are associated with a ForeignKey or ForeignKeyConstraint, or specify a 'primaryjoin' expression.

```
## Fix the dockercompose file so that the tables are not created from the .sql scripts
- [x] Check how to recreate the same thing we did with pgadmin

## (Solved)Learn how to insert objects that have relations
