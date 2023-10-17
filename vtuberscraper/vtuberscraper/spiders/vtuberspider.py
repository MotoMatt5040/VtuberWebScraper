import scrapy
import logging
import urllib.parse

logging.getLogger('scrapy').propegate = False


class VtuberspiderSpider(scrapy.Spider):
    next_page = ''
    f = open(r'../../../utils/vtuber_names.txt', 'r')
    line = f.readline()
    name = "vtuberspider"
    allowed_domains = ["virtualyoutuber.fandom.com"]
    start_urls = [f"https://virtualyoutuber.fandom.com/wiki/{line}"]
    skip = [
        '%2ANamirin',
        'Lenaga_Mugi',
        'Kanada_Shoichi',
        'Fuwa',
        'Riksa',
        'Kurusu',
        'Enna_Alouetta',
        'kqsii',
        'Spendiferachie',
        'Kitsui_Akira',
        'Admiral_Bahroo',
        'Sunny'
    ]

    custom_settings = {  # this is used to overwrite the settings.py file
        'FEEDS': {
            'vtuberdata.json': {'format': 'json', 'overwrite': True}
        }
    }


    def parse(self, response):
        data = response.css('aside.portable-infobox')

        media = self.pull_media(data)

        for item in data:
           yield {
               "name": item.css('aside.portable-infobox h2::text')[0].get(),
               "agency": item.xpath(
                   '//div[@data-source="affiliation"]//div[@class="pi-data-value pi-font"]//a/text()').get(),
               "media": media,
               'gender': data.xpath('//div[@data-source="gender"]//div/text()').get(),
               'age': data.xpath('//div[@data-source="age"]//div/text()').get(),
               'birthday': data.xpath('//div[@data-source="birthday"]//div/text()').get(),
               'height': data.xpath('//div[@data-source="height"]//div/text()').get(),
               'zodiac': data.xpath('//div[@data-source="zodiac"]//div/text()').get(),
               'emoji': data.xpath('//div[@data-source="emoji"]//div/text()').get(),
           }

        while True:
            next_page = f"{self.f.readline()}"
            print('\n\n\n')
            print(next_page)
            print('\n\n\n')
            encode_url = str(urllib.parse.quote_plus(next_page)).replace('%0A', '')
            if encode_url in self.skip:
                continue
            break


        if next_page is not None:
            next_page_url = f'https://virtualyoutuber.fandom.com/wiki/{encode_url}'
            print('\n\n\n')
            print(next_page_url)
            print('\n\n\n')
            yield response.follow(next_page_url, callback=self.parse)





    @staticmethod
    def pull_media(data):
        channel_links = data.xpath('//div[@data-source="channel"]//a/text()')
        social_links = data.xpath('//div[@data-source="social_media"]//a/text()')
        official_website_links = data.xpath('//div[@data-source="official_website"]//a/text()')
        media = {
            'channels': {},
            'social links': {},
            'official websites': {}
        }
        i = 0
        for item in channel_links:
            media['channels'][item.get()] = data.xpath('//div[@data-source="channel"]//a/@href')[i].get()
            i += 1
        i = 0
        for item in social_links:
            media['social links'][item.get()] = data.xpath('//div[@data-source="social_media"]//a/@href')[i].get()
            i += 1
        i = 0
        for item in official_website_links:
            media['official websites'][item.get()] = data.xpath('//div[@data-source="official_website"]//a/@href')[
                i].get()
            i += 1
        return media