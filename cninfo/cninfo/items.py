# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
import time
from scrapy import Field
class CninfoItem(scrapy.Item):
    # define the fields for your item here like:
    href = scrapy.Field()
    question = scrapy.Field()
    publish_data = scrapy.Field()
    answer = scrapy.Field()
    name = scrapy.Field()
    company_code = scrapy.Field()
    company_name = scrapy.Field()
    replay_data = scrapy.Field()
    questioner = scrapy.Field()

    date= datetime.date.today()
    date =date.strftime("%Y-%m-%d")
    collection = table = date

