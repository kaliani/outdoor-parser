# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Boards(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    type = scrapy.Field()
    city = scrapy.Field()
    region = scrapy.Field()
    side = scrapy.Field()
    format = scrapy.Field()
