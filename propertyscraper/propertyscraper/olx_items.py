import scrapy
from scrapy import Item, Field

class PropertyItem(scrapy.Item):
    datas = Field()
    # name = Field()
    # price = Field()
