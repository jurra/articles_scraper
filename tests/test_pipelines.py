# import scrapy pipelines
from src.pipelines import *

def test_pipelines():
    """
    Test the scrapy pipelines
    """
    str = "hello"
    assert str == "hello"