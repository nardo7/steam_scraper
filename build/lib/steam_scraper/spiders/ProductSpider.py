# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ProductItem, ProductItemLoader


class ProductSpider(scrapy.spiders.CrawlSpider):
    name = 'products'
    allowed_domains = ['steampowered.com']
    start_urls = ['http://store.steampowered.com/search/?sort_by=Released_DESC']

    rules = [

        Rule(

            LinkExtractor(

                allow='/app/(.+)/',

                restrict_css='#search_result_container'),

            callback='parse_product'),

        Rule(

            LinkExtractor(

                allow='page=(\d+)',

                restrict_css='.search_pagination_right'))

    ]

    # Simplest version
    # def parse_product(self, response):
    #
    #     n_reviews = response.css('.responsive_hidden').re('\(([\d,]+) reviews\)')
    #     n_reviews = [int(r.replace(',', '')) for r in n_reviews]
    #     n_reviews = max(n_reviews)  # keep the review section, which has the more count of reviews
    #
    #     return {
    #         'app_name':response.css('apphub_AppName::text').extract_first(),
    #         'specs':  response.css('.game_area_details_specs a ::text').extract(),
    #         'n_reviews': n_reviews
    #     }

    # Cleanest Version
    def parse_product(self, response):
        loader=ProductItemLoader(item=ProductItem(),response=response)
        loader.add_css('app_name', '.apphub_AppName ::text')
        loader.add_css('specs', '.game_area_details_specs a ::text')
        loader.add_css('n_reviews', '.responsive_hidden', re='\(([\d,]+) reviews\)')
        return loader.load_item()



