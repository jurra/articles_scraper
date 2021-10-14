#!/usr/bin/python
from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def get_db_uri():
    params = config()
    db_uri = "postgresql+psycopg2://{}:{}@{}:{}".format(params['user'], params['password'], params['host'], params['port'], params['database'])
    return db_uri
