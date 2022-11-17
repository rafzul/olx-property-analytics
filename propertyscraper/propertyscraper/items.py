# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class FactPropertyTransactions(scrapy.Item):
    datas = Field()
    # name = Field()
    # price = Field()
