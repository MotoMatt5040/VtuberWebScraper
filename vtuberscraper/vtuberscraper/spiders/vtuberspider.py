import scrapy


class VtuberspiderSpider(scrapy.Spider):
    name = "vtuberspider"
    allowed_domains = ["virtualyoutuber.fandom.com"]
    start_urls = ["https://virtualyoutuber.fandom.com/wiki/NIJISANJI"]

    def parse(self, response):
        pass
