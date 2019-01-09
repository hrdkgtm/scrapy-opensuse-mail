# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MailItem(scrapy.Item):
    subject = scrapy.Field()
    origin = scrapy.Field()
    date = scrapy.Field()
    src_link = scrapy.Field()
    reference_link = scrapy.Field()
    msg_body = scrapy.Field(serializer=str)