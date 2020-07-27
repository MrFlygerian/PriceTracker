# -*- coding: utf-8 -*-
import datetime

import scrapy


class LegendlondonSpider(scrapy.Spider):
    name = 'LegendLondon'
    allowed_domains = ['legendlondon.co']
    start_urls = ['https://www.legendlondon.co/collections/man-all']
    custom_settings = dict(FEED_URI="LL.csv", FEED_FORMAT='csv')

    def parse(self, response):
        products = response.xpath('//h4[@class = "product-list-item-title"]/a//text()').getall()
        price = response.xpath('//p[@class = "product-list-item-price"]/span[@class = "price money"]/text()').getall()

        row_data = zip(products, price)

        for item in row_data:
            # create a dictionary to store the scraped info
            scraped_info = {
                # key:value
                "page": response.url,
                "product": item[0],
                "price": item[1],
                "date": datetime.date.today().strftime("%d-%m-%Y")

            }

            yield scraped_info

            urls = []
            NEXT_PAGE_SELECTOR = 'ul.pagination a::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).get()

            if next_page is not None and response.urljoin(next_page) not in urls:
                urls.append(response.urljoin(next_page))
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse)
