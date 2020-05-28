import scrapy

class redditSpider(scrapy.Spider):
    name = "reddit"
    start_url = "https://www.reddit.com/r/Python/"

    def parse(self, response):
        links = response.xpath('//img/@src')
        html = ""
        for link in links:
            url = link.get()
            if any(ext in url for ext in [".png",".jpg"]):
                html+=f"""<a href = "{url}"
                        target = "_blank>
                        <img src = "{url}" height = "33%"
                        width = "33%"/>
                        <a/>"""
                with open("frontpage.html", "a") as page:
                    page.write(html)
                    page.close()

