import scrapy

class BuyDigCrawler(scrapy.Spider):

    name = 'buydigCrawler'
    allowed_domains = ['buydig.com']
    start_urls = ['https://www.buydig.com/shop/list/category/1200/Video-Gaming?fc=1200&pn=1&lmt=20']
    custom_settings= dict(FEED_URI="buydig_%(time)s.csv", FEED_FORMAT='csv')

    def parse(self, response, start_urls = start_urls):

        print ("processing " + response.url)
        #Extracting product info using CSS
        price = response.css('.p-search__main__results__result__price__regular::text').getall()
        product = response.css('div.p-search__main__results__result__info__name a::attr(data-name)').getall()
        brand = response.css('div.p-search__main__results__result__info__name a::attr(data-brand)').getall()

        row_data = zip(product, price, brand)

        for item in row_data:
            # create a dictionary to store the scraped info
            scraped_info = {
                # key:value
                'page': response.url,
                'product_name': item[0],
                'price': item[1],
                'brand': item[2],
            }
            # yield or give the scraped info to scrapy
            yield scraped_info

            urls = start_urls
            NEXT_PAGE_SELECTOR = '.p-search__main__widgets__pagination a::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).get()
            if next_page is not None and response.urljoin(next_page) not in urls:
                urls.append(response.urljoin(next_page))
                yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse)
            else:
                pass

