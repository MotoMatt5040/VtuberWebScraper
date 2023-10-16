import scrapy


class VtuberspiderSpider(scrapy.Spider):
    name = "vtuberspider"
    allowed_domains = ["virtualyoutuber.fandom.com"]
    start_urls = ["https://virtualyoutuber.fandom.com/wiki/Special:AllPages"]

    def parse(self, response):
        data = response.css('div.mw-allpages-body li a')
        next_page = response.css('div.mw-allpages-nav a ::attr(href)').get()
        for item in data:
            yield {
                'name': item.css('a::text').get(),
                'url': item.css('a').attrib['href']
            }
