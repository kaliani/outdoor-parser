import scrapy
from outdoorParse.items import Boards


class IdmediaSpyder(scrapy.Spider):
    name = 'itmedia'

    start_urls = ['https://idmedia.ua/billboard',
                  'https://idmedia.ua/citylight',
                  'https://idmedia.ua/backlight',
                  'https://idmedia.ua/roof',
                  'https://idmedia.ua/scroll',
                  'https://idmedia.ua/digital',
                  'https://idmedia.ua/troll',
                  'https://idmedia.ua/brandmauer',
                  'https://idmedia.ua/ostanovka',
                  'https://idmedia.ua/indoor',
                  'https://idmedia.ua/arka',
                  'https://idmedia.ua/turniket',
                  'https://idmedia.ua/holder',
                  'https://idmedia.ua/metrodigiltal',
                  'https://idmedia.ua/metro'
                  ]

    def parse(self, response):

        main_link = response.css('li.result__item')
        for board in main_link:
            new_data = Boards()
            new_data['id'] = board.css('span.btn--xsm::text').get()
            new_data['title'] = board.css('h5.result__address::text').get()
            new_data['type'] = board.css('a.brand::text').getall()[0]
            new_data['city'] = board.css('a.brand::text').getall()[1]
            new_data['region'] = board.css('a.brand::text').getall()[2]
            new_data['side'] = board.css('h6.mark::text').getall()[4]
            new_data['format'] = board.css('h6.mark::text').getall()[6]
            yield new_data

        next_page = response.css('a.pagination__item--next::attr(href)').get()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
