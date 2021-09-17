# Pipeline for articles scraping with scrapy, postgres and sqlalchemy
A simple customizable pipeline to capture articles in a specific format for text analysis. 

## Features
- Setup database easily with `docker-compose` 
- Define your own crawlers and pipelines
- Predefined database model to start collecting data


## Entity relationship diagram
![](./docs/img/DB_diagram.png)

## Usage
- We recommend to create a specific virtual environment for the project
- Run `pip install -e .` to develop and modify modules.
- Run `docker-compose up -d` to spin the postgres database instnace.
- Run `pytest` to check that everything is setup,
- Run `scrapy crawl example`
- Run the `example.ipynb` notebook to explore the database.
- Enjoy :)

## References
[1]“Common Text Mining Workflow - DZone Big Data,” dzone.com. https://dzone.com/articles/common-text-mining-workflow (accessed May 04, 2021).

[2]“Web crawler,” Wikipedia. Apr. 16, 2021. Accessed: May 04, 2021. [Online]. Available: https://en.wikipedia.org/w/index.php?title=Web_crawler&oldid=1018112513

[3]“Text Analysis: the only guide you’ll ever need,” MonkeyLearn. https://monkeylearn.com/text-analysis/ (accessed Jun. 23, 2021).

[4]“How to store articles or other large texts in a database,” Stack Overflow. https://stackoverflow.com/questions/1084506/how-to-store-articles-or-other-large-texts-in-a-database (accessed Aug. 03, 2021).

[5]R. Python, “Data Management With Python, SQLite, and SQLAlchemy – Real Python.” https://realpython.com/python-sqlite-sqlalchemy/ (accessed Aug. 27, 2021).

[6]H. Wang, “A Minimalist End-to-End Scrapy Tutorial (Part III),” Medium, Apr. 30, 2020. https://towardsdatascience.com/a-minimalist-end-to-end-scrapy-tutorial-part-iii-bcd94a2e8bf3 (accessed Sep. 09, 2021).

[7]M. Hoyos, “What is an ORM and Why You Should Use it,” Medium, Mar. 22, 2019. https://blog.bitsrc.io/what-is-an-orm-and-why-you-should-use-it-b2b6f75f5e2a (accessed Sep. 16, 2021).

[8]M. F. Zafra, “Web Scraping news articles in Python,” Medium, May 25, 2020. https://towardsdatascience.com/web-scraping-news-articles-in-python-9dd605799558 (accessed Sep. 16, 2021).

[9]Balaji, “Best Article Scraper Free Web Scraping Content Scraper tool,” CoderDuck. https://www.coderduck.com/article-scraper (accessed Sep. 16, 2021).



