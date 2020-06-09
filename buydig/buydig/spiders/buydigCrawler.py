# -*- coding: utf-8 -*-
from typing import Dict, Any

import scrapy


class BuydigcrawlerSpider(scrapy.Spider):

    name = 'buydigCrawler'
    allowed_domains = ['buydig.com']
    start_urls = ['https://www.buydig.com/shop/list/category/2142/Action-Cameras/']

    def parse(self, response):
        print ('processing ' + response.url)
        #Extracting product info using CSS
        price = response.css(".p-search__main__results__result__price__regular::text").getall()
        product = response.css("div.p-search__main__results__result__info__name a::attr(data-name)").getall()
        brand = response.css("div.p-search__main__results__result__info__name a::attr(data-brand)").getall()

        row_data = zip(product, price, brand)

        for item in row_data:
            # create a dictionary to store the scraped info
            scraped_info: Dict[str, Any] = {
                # key:value
                'page': response.url,
                'product_name': item[0],
                'price': item[1],
                'brand': item[2],
            }

            # yield or give the scraped info to scrapy
            yield scraped_info
