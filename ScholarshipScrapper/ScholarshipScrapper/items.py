# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScholarshipItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    stitle=scrapy.Field()
    suni=scrapy.Field()
    sdeadline=scrapy.Field()
    scountry=scrapy.Field()
    sdegree=scrapy.Field()
    scoursestart=scrapy.Field()
    surl=scrapy.Field()