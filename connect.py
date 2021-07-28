from sqlalchemy import create_engine
from config import config
import pandas
import json


# Postgres username, password, and database name
params = config()

postgres_str = ('postgresql://{username}:{password}@{ipaddress}:{port}'
.format(
    username=params["user"],
    password=params["password"],
    ipaddress=params["host"],
    port=5432)
)
# Create the connection
cnx = create_engine(postgres_str)
df = pandas.read_sql_query('''SELECT * FROM country''', con=cnx)
print(df)