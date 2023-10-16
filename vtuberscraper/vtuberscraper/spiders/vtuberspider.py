import scrapy
import logging

logging.getLogger('scrapy').propegate = False


class VtuberspiderSpider(scrapy.Spider):
    name = "vtuberspider"
    allowed_domains = ["virtualyoutuber.fandom.com"]
    start_urls = ["https://virtualyoutuber.fandom.com/wiki/Special:AllPages"]
    first = True

    def parse(self, response):
        data = response.css('div.mw-allpages-body li a')

        for item in data:
            yield {
                'name': item.css('a::text').get(),
                'url': item.css('a').attrib['href']
            }

        if not self.first:
            next_page = response.css('div.mw-allpages-nav a ::attr(href)')[1].get()
        else:
            next_page = response.css('div.mw-allpages-nav a ::attr(href)').get()
            self.first = False

        if next_page is not None:
            next_page_url = f'https://virtualyoutuber.fandom.com{next_page}'
            yield response.follow(next_page_url, callback=self.parse)