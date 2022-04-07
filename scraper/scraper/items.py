# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItem(scrapy.Item):
    keyword = scrapy.Field()
    link = scrapy.Field()
    judul = scrapy.Field()
    tanggal = scrapy.Field()
    artikel = scrapy.Field()