# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Compose, TakeFirst
from .util import StripText, str_to_int

class SteamScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ProductItem(scrapy.Item):
    app_name = scrapy.Field()

    specs = scrapy.Field(
        output_processor=MapCompose(StripText())
    )

    n_reviews = scrapy.Field(
        output_processor=Compose(MapCompose(
            StripText(),
            lambda x:x.replace(',',''),
            str_to_int)
            , max
        )
    )

class ProductItemLoader(ItemLoader):

    default_output_processor=TakeFirst()