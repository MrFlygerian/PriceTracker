# -*- coding: utf-8 -*-
import scrapy
import time
import datetime

class CityplumbingSpider(scrapy.Spider):
    name = 'cityplumbing'
    allowed_domains = ['www.cityplumbing.co.uk']
    start_urls = ['http://www.cityplumbing.co.uk/Product/Heating/Hot-Water-Cylinders/Unvented-Cylinders/c/1806005/']
    custom_settings = dict(FEED_URI="CP.csv", FEED_FORMAT='csv')

    def parse(self, response):
        products = response.xpath('//h4[@class = "bold"]/a//text()').getall()
        price = response.xpath('//span[@class = "product_price_holder"]/span[@class = "price_value"]/text()').getall()
        product_code = response.xpath('//div[@class="product_code"]/span/text()').getall()


        row_data = zip(products, price, product_code)

        for item in row_data:
            #create a dictionary to store the scraped info
            scraped_info = {
                #key:value
                "page":response.url,
                'product' : item[0],
                "price": item[1],
                'product code' : item[2],
                "date": datetime.date.today().  strftime("%d-%m-%Y")

            }

            yield scraped_info
