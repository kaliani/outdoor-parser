import scrapy
from outdoorParse.items import Boards

class IdmediaSpyder(scrapy.Spider):
    name = 'itmedia'
    allowed_domains = ['www.idmedia.ua']
    start_urls = ['https://idmedia.ua/arka']

    # def parse(self, response):
    #
    #     main_link = response.css("li.formats__item a::attr(href)").getall()
    #     for link in main_link:
    #         url = response.urljoin(link)
    #         # print(url)
    #         yield scrapy.Request(url, callback = self.parse)

    def parse_dir_contents(self, response):

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

            next_page = response.css('a.pagination__item--next::attr(href)').get()

            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)

            # print(actual_link)
            # print(response)
    # response.css("li.formats__item").xpath('a')
    # def parse(self, response):
    #     # boards = Boards()
    #     main_link = response.css('li.result__item')
    #
    #     for board in main_link:
    #
    #         yield {
    #             'id': board.css('span.btn--xsm::text').get(),
    #             'title': board.css('h5.result__address::text').get(),
    #             'type': board.css('a.brand::text').getall()[0],
    #             'city': board.css('a.brand::text').getall()[1],
    #             'region': board.css('a.brand::text').getall()[2],
    #             'side': board.css('h6.mark::text').getall()[4],
    #             'format': board.css('h6.mark::text').getall()[6]
    #         }
    #     next_page = response.css('a.pagination__item--next::attr(href)').get()
    #
    #     if next_page is not None:
    #         next_page = response.urljoin(next_page)
    #         yield scrapy.Request(next_page, callback=self.parse)

